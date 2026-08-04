# Level 1

1. Cloned the repository using the terminal
2. Navigated into the project directory
3. Explored available files and folders
4. Entered the `GrandLine` directory
5. Inspected its contents
6. Navigated further into the `LougetownReef` directory
7. Identified the `cat.sh` script, which hinted at the execution mechanism
8. Analyzed the crates:
   * The riddle indicated that *fake files are sealed* (i.e., non-executable)
   * Focused only on executable files
9. Located the correct file:

   * `crate_C/devil_fruit_6.txt` (6th file in crate_C)

./eat.sh sector_C/devil_fruit_6.txt

Successful execution confirmed:

![Level 1 Success](images_TASK_02/level-1.png)

# LEVEL-2

1. Entered `whiskey_Peak` folder
2. Explored files and folders
3. Opened `feast_manifest.txt`
4. Checked file history:
git log --follow -p feast_manifest.txt

* Only one commit found suspected another branch

5. Listed branches: git branch -a

* Found `whiskey_peak_investigation` branch

    -> git checkout whiskey_peak_investigation

6. Checked files again:
        ls -la
        cat feast_manifest.txt
* Item 01 changed from `"Bink's Sake"` → `"Sleep Powder Infused Sake"`

7. Entered hidden folder:

```bash
cd .baroque_works_cache
ls -la
cat unlock_vault.sh
```

8. Script required environment variable:

```bash
export AWAKENING_SIGNATURE="ONE_PIECE{GITO_GITO_NO_AWAKENING}"
./unlock_vault.sh
```

9. Compared generated logs:

```bash
diff marine_intercept.log bounty_hunter_feed.log
```

10. Faced macOS issue , used manual decryption:

```bash
echo "U2FsdGVkX18eGXT7fCm/5zmZmejGVicPYQQLji9cigHrIyxzalWleyVW+k3X6rBlS3baMgfv0DVe24ILF5v+rw==" | openssl enc -aes-256-cbc -d -a -pbkdf2 -iter 100000 -pass pass:"$AWAKENING_SIGNATURE"
```

* Level 2 Flag:`BAROQUE_DIAL{SPLIT_TIMELINE_MISDIRECTION}`
 
workflow:
cd ../Whiskey_Peak
cat feast_manifest.txt

git log --follow -p feast_manifest.txt   # only one commit, no hidden edits here
git branch -a                            # reveals extra branch: whiskey_peak_investigation

git checkout whiskey_peak_investigation
cat feast_manifest.txt          # Item 01 now reads "Sleep Powder Infused Sake" the hidden truth

ls -la                           # reveals hidden folder .baroque_works_cache
cd .baroque_works_cache
cat unlock_vault.sh             # script needs env var AWAKENING_SIGNATURE to match a SHA-256 hash

export AWAKENING_SIGNATURE="ONE_PIECE{GITO_GITO_NO_AWAKENING}"
./unlock_vault.sh                # [SIGNATURE MATCH] confirmed

![Level 2](images_TASK_02/level-2.png)

# LEVEL-3

1. `git branch -a` , switched to the little garden branch using `git switch`.

2. According to the instructions the transmission code we recieved we needed to convert it into broadcast representation so i tried converting it to base64.

3. Converted the Level 2 code into base64 using: `echo -n "BAROQUE_DIAL{SPLIT_TIMELINE_MISDIRECTION}" | base64`

4. Then i used the above obtained string to search for it in the log file using `grep -rn` but it was not showing anything after some testing i only searched the firest few letters and then i got the file which had the same base64 string with a k at the end instead of =.

5. Then i copied the path of where the file was at `./sector_beta/outpost/watchtower/storage/archive/agent_manifest.log`

6. Then i used cat to execute that particular log `cat sector_beta/outpost/watchtower/storage/archive/agent_manifest.log` to read the true report and get the hidden flag.

-------------------------------------------------
STATUS: METALLIC WAX SUIT ACTIVE

SECURITY_TAG:
QkFST1FVRV9ESUFMe1NQTElUX1RJTUVMSU5FX01JU0RJUkVDVElPTn0K

-------------------------------------------------

BAROQUE WORKS EXECUTIVE REPORT

PONEGLYPH_FRAGMENT_I = "KjY2MjF4bW0lKzYqNyBsIS0vbTAtJTcnL"

-------------------------------------------------

![Level 3](images_TASK_02/level-3.png)

# LEVEL-4

1. Switched to the alternate_timeline branch, where the Water_7 content lives.

2. Navigated into Water_7/galley_la_company and tried reading the file puffing_tom_blueprints directly — the output was unreadable binary garbage, since the file had no proper  extension hiding what it actually was.

3. Used the file command to check the file's true type instead of trusting its name. This revealed it was actually a gzip-compressed tar archive, just saved without the usual .tar.gz extension.

4. Copied the file with the correct extension and extracted it using tar, which revealed a nested archive inside called step1_blueprints.zip.

5. Extracted that zip file too, which produced two files: a decoy file with fake structural data, and the real find — secret_link.txt.

6. Read that file's contents, which revealed the second cipher fragment for this level.

Result:
PONEGLYPH_FRAGMENT_II="SwnbzptDiM3JSpvFiMuJ28PJzAlJ28VIzA="
----------------------------------------------------------------------------------------------
drwxr-xr-x  6 mlakshyardhaabhiram  staff  192 31 Jul 22:53 .
drwxr-xr-x  3 mlakshyardhaabhiram  staff   96 31 Jul 22:46 ..
drwxr-xr-x  4 mlakshyardhaabhiram  staff  128 20 Jul 22:32 blueprints_extracted
-rw-r--r--  1 mlakshyardhaabhiram  staff  503 31 Jul 22:46 puffing_tom_blueprints
-rw-r--r--  1 mlakshyardhaabhiram  staff  935 20 Jul 22:32 step1_blueprints.zip
-rw-r--r--  1 mlakshyardhaabhiram  staff  503 31 Jul 22:50 step2_blueprints.tar
mlakshyardhaabhiram@LAKSHYARDHA galley_la_company % cat blueprints_extracted/secret_link.txt

PONEGLYPH_FRAGMENT_II="SwnbzptDiM3JSpvFiMuJ28PJzAlJ28VIzA="
----------------------------------------------------------------------------------------------

![Level 4](images_TASK_02/level-4.png)

# LEVEL-5



1. Navigating Git History: git log --oneline -- Enies_Lobby.

2. Checked out the earliest commit (d4e7bf5) to restore the missing vault directory and its contents: git checkout d4e7bf5
ls -la .cp9_secure_vault
cd Enies_Lobby
ls -la
ls -la .cp9_secure_vault

3. Inspected the source code (cat .cp9_secure_vault/poneglyph.py) to analyze the logic:

import base64
ENCODED = input("Enter code : ")
KEY = 0x42
decoded = base64.b64decode(ENCODED)
flag = bytes(b ^ KEY for b in decoded).decode()
print("Prize : ")
print(flag)

4. Confirmed that the script expects the Base64-encoded combined Poneglyph string as input rather than the Level 2 flag, running a byte-wise XOR against key 0x42.

5. Executed python3 .cp9_secure_vault/poneglyph.py.
Supplied the combined Poneglyph string:
KjY2MjF4bW0lKzYqNyBsIS0vbTAtJTcnLSwnbzptDiM3JSpvFiMuJ28PJzAlJ28VIzA=

Successfully extracted the repository URL for Level 6:
https://github.com/rogueone-x/Laugh-Tale-Merge-War

![Level 5](images_TASK_02/level-5.png)

# LEVEL-6

1. cloned the new repo and changed directory

2. inspect the layout:git log --oneline --graph --all

3. Start the merge process
git merge origin/pirate_king_path

4. Inspect conflict files:

  cat treasure/key_part_1.txt
  cat treasure/key_part_2.txt

5. Resolve key_part_1.txt by combining "TheGrand" and "Line"
cat << 'EOF' > treasure/key_part_1.txt
PONEGLYPH FRAGMENT α

Recovered Inscription:

TheGrandLine
EOF

Resolve key_part_2.txt by combining "Remem" and "bers"
cat << 'EOF' > treasure/key_part_2.txt
PONEGLYPH FRAGMENT β

Recovered Inscription:

Remembers
EOF
6. Stage the resolved files and complete the merge commit
       git add treasure/key_part_1.txt treasure/key_part_2.txt
       git commit -m "Resolve merge conflicts for Laugh Tale key"

7. Run the victory script and pass the combined password
./victory.sh

----------------------------------X--------------------------------
mlakshyardhaabhiram@LAKSHYARDHA Laugh-Tale-Merge-War % git add treasure/key_part_1.txt treasure/key_part_2.txt
git commit -m "Resolve merge conflicts for Laugh Tale key"
./victory.sh
[ancient_history 96f99c9] Resolve merge conflicts for Laugh Tale key

==============================
 Verifying Timeline Integrity
==============================

Enter the Pirate King's Password: TheGrandLineRemembers
Timeline Integrity ............. OK
Merge Conflict ................. Resolved
Repository ..................... Restored
History ........................ Preserved

====================================================

        THE ONE PIECE HAS BEEN FOUND

====================================================

Congratulations, Captain.

The greatest treasure was never gold.

It was the ability to understand,
recover,
and preserve history.

Today you have mastered:

⚓ Linux
⚓ Git
⚓ Problem Solving

FLAG{The_Grand_Line_Remembers_Your_Commit}

====================================================

🏴 REWARD UNLOCKED

Title:
    Pirate King of Git

Badge:
    👑 Keeper of History

Your bounty has increased to

    5,600,000,000 ฿

The Thousand Sunny will always have a place for you.

Now go write your own history.









