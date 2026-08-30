import sqlite3
from typing import Optional, List, Tuple

DB_NAME = "berry_broker.db"

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database schema and populates initial shop items."""
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Pirates table (Users, Wallets, and Banks)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pirates (
            user_id INTEGER PRIMARY KEY,
            wallet INTEGER NOT NULL DEFAULT 100,
            bank INTEGER NOT NULL DEFAULT 0
        )
        """)

        # Shop Items table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS shop_items (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            cost INTEGER NOT NULL,
            effect TEXT NOT NULL
        )
        """)

        # Inventory table (Tracks user-owned items)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            item_id INTEGER NOT NULL,
            status TEXT CHECK(status IN ('active', 'spent')) DEFAULT 'active',
            FOREIGN KEY (user_id) REFERENCES pirates(user_id),
            FOREIGN KEY (item_id) REFERENCES shop_items(item_id)
        )
        """)

        # Populate default shop items if empty
        cursor.execute("SELECT COUNT(*) FROM shop_items")
        if cursor.fetchone()[0] == 0:
            default_items = [
                ("Rumble Ball", 250, "Temporary power boost during raids"),
                ("Den Den Mushi", 500, "Receive early warnings on incoming raids"),
                ("Log Pose Upgrade", 1000, "Increases raid success rate by 10%"),
                ("Klabautermann Doll", 2500, "Protects 20% of lost Berries during a failed raid")
            ]
            cursor.executemany(
                "INSERT INTO shop_items (name, cost, effect) VALUES (?, ?, ?)",
                default_items
            )
        conn.commit()
# --- Database Helper Functions ---

def get_or_create_pirate(user_id: int) -> sqlite3.Row:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pirates WHERE user_id = ?", (user_id,))
        pirate = cursor.fetchone()
        if not pirate:
            cursor.execute("INSERT INTO pirates (user_id, wallet, bank) VALUES (?, 100, 0)", (user_id,))
            conn.commit()
            cursor.execute("SELECT * FROM pirates WHERE user_id = ?", (user_id,))
            pirate = cursor.fetchone()
        return pirate

def update_wallet(user_id: int, amount: int):
    """Adjust wallet by `amount` (can be positive or negative)."""
    get_or_create_pirate(user_id)
    with get_connection() as conn:
        conn.execute("UPDATE pirates SET wallet = wallet + ? WHERE user_id = ?", (amount, user_id))
        conn.commit()

def transfer_berries(sender_id: int, receiver_id: int, amount: int) -> bool:
    sender = get_or_create_pirate(sender_id)
    if sender["wallet"] < amount:
        return False
    
    get_or_create_pirate(receiver_id)
    with get_connection() as conn:
        conn.execute("UPDATE pirates SET wallet = wallet - ? WHERE user_id = ?", (amount, sender_id))
        conn.execute("UPDATE pirates SET wallet = wallet + ? WHERE user_id = ?", (amount, receiver_id))
        conn.commit()
    return True

def get_top_pirates(limit: int = 5) -> List[sqlite3.Row]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT user_id, (wallet + bank) as total_bounty FROM pirates ORDER BY total_bounty DESC LIMIT ?",
            (limit,)
        )
        return cursor.fetchall()

def fetch_shop_items() -> List[sqlite3.Row]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM shop_items")
        return cursor.fetchall()

def get_shop_item_by_name(name: str) -> Optional[sqlite3.Row]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM shop_items WHERE LOWER(name) = LOWER(?)", (name,))
        return cursor.fetchone()

def purchase_item(user_id: int, item_id: int, cost: int) -> bool:
    pirate = get_or_create_pirate(user_id)
    if pirate["wallet"] < cost:
        return False

    with get_connection() as conn:
        conn.execute("UPDATE pirates SET wallet = wallet - ? WHERE user_id = ?", (cost, user_id))
        conn.execute("INSERT INTO inventory (user_id, item_id, status) VALUES (?, ?, 'active')", (user_id, item_id))
        conn.commit()
    return True

def get_user_inventory(user_id: int) -> List[sqlite3.Row]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT i.inventory_id, s.name, s.effect, i.status 
            FROM inventory i
            JOIN shop_items s ON i.item_id = s.item_id
            WHERE i.user_id = ?
        """, (user_id,))
        return cursor.fetchall()