# Berry Broker — Discord Bot (TASK-07)

Berry Broker is an interactive One Piece-themed economy and utility Discord bot built using `discord.py` and `sqlite3`. It allows server members to build their bounty, raid rival crews, trade currency, and fetch live Grand Line intel from an external API.

# Features

* Bounty Ledger (`!bounty`): View your current wallet balance, bank reserves, and total accumulated bounty.
* Daily Loot (`!setsail`): Set sail once every 24 hours to raid a merchant vessel and earn between 200–500 Berries (includes a built-in cooldown handler).
* Player Trading (`!trade @user <amount>`): Safely transfer Berries from your wallet stash to another server member.
* Crew Raids (`!raid @user`): Attempt to ambush a rival pirate's wallet. Has a 45% success rate to steal 10%–30% of their wallet, or a fail penalty that awards Berries to the defender.
* Leaderboard (`!worstgeneration`): Displays the top 5 highest-bounty pirates across the server.
* Grand Line Intel (`!logpose`): Fetches dynamic One Piece lore/data asynchronously using the API helper.

# Project Architecture

```text
TASK-07/
├── bot.py                # Main bot entry point & cog loader
├── database.py           # SQLite connection & CRUD operations
├── one_piece_api.py      # Async API handler for !logpose
├── cogs/
│   └── economy.py        # Discord command interface & cooldowns
├── berry_broker.db       # Local SQLite database (auto-generated)
└── requirements.txt      # Python dependencies
```

# Setup & Installation

# 1. Prerequisites

Ensure you have Python 3.10+ installed on your system.

# 2. Environment Setup

Clone the repository and navigate into the `TASK-07` directory:

```bash
cd TASK-07
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# 3. Configure Discord Bot Token

Obtain your token from the Discord Developer Portal and export it to your environment:

```bash
export DISCORD_BOT_TOKEN="your_discord_bot_token_here"
```

> Note: Enabling Message Content Intent under the Bot tab in the Developer Portal is required for prefix commands to function.

# Running the Bot

Start the bot execution process:

```bash
python3 bot.py
```

Upon successful connection, your terminal will display:

```text
Berry Broker logged in as Berry Broker#4617 (ID: 1543647575394230423)
--------------------------------------------------
```
