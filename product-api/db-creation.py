import sqlite3
import random
from datetime import datetime, timedelta

# Connect to a database (creates the file if it doesn't exist)
conn = sqlite3.connect('product.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('DROP TABLE IF EXISTS shoppinglist')
cursor.execute('DROP TABLE IF EXISTS shoppinglist_user')

# (Optional) Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        balance REAL DEFAULT 0.0
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS shoppinglist (
        id INTEGER PRIMARY KEY,
        itemname TEXT NOT NULL,
        price REAL NOT NULL,
        category TEXT NOT NULL
    )
''')

# New: Create shoppinglist_user table for user-item relations
cursor.execute('''
    CREATE TABLE IF NOT EXISTS shoppinglist_user (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        item_id INTEGER NOT NULL,
        purchased_date TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        purchase_mode TEXT NOT NULL CHECK(purchase_mode IN ('inperson', 'online')),
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(item_id) REFERENCES shoppinglist(id)
    )
''')

users = [
    ('Alice', 'alice@example.com', 100.0),
    ('Bob', 'bob@example.com', 200.0),
    ('Charlie', 'charlie@example.com', 300.0),
    ('David', 'david@example.com', 400.0),
    ('Eve', 'eve@example.com', 500.0),
    ('Frank', 'frank@example.com', 600.0),
    ('Grace', 'grace@example.com', 700.0),
    ('Heidi', 'heidi@example.com', 800.0),
    ('Ivan', 'ivan@example.com', 900.0),
    ('Judy', 'judy@example.com', 1000.0),
    ('Karl', 'karl@example.com', 1100.0),
    ('Laura', 'laura@example.com', 1200.0),
    ('Mallory', 'mallory@example.com', 1300.0),
    ('Niaj', 'niaj@example.com', 1400.0),
    ('Olivia', 'olivia@example.com', 1500.0),
    ('Peggy', 'peggy@example.com', 1600.0),
    ('Quentin', 'quentin@example.com', 1700.0),
    ('Rupert', 'rupert@example.com', 1800.0),
    ('Sybil', 'sybil@example.com', 1900.0),
    ('Trent', 'trent@example.com', 2000.0)
]

cursor.executemany('INSERT INTO users (name, email, balance) VALUES (?, ?, ?)', users)

shoppinglist_items = [
    ('Milk', 2.5, 'Grocery'),
    ('Bread', 1.5, 'Grocery'),
    ('Shampoo', 5.0, 'Personal Care'),
    ('Notebook', 3.0, 'Stationery'),
    ('Apple', 0.5, 'Grocery'),
    ('Pen', 0.8, 'Stationery'),
    ('Soap', 1.2, 'Personal Care'),
    ('Eggs', 2.0, 'Grocery'),
    ('Juice', 3.5, 'Grocery'),
    ('Toothpaste', 2.2, 'Personal Care')
]

cursor.executemany('INSERT INTO shoppinglist (itemname, price, category) VALUES (?, ?, ?)', shoppinglist_items)

# Insert sample data into shoppinglist_user
# First, fetch user and item ids
cursor.execute('SELECT id, name FROM users')
user_map = {name: uid for uid, name in cursor.fetchall()}
cursor.execute('SELECT id, itemname FROM shoppinglist')
item_map = {name: iid for iid, name in cursor.fetchall()}

sample_shoppinglist_user = []
purchase_modes = ['inperson', 'online']

# Example: Each user purchases 2 random items
for user in user_map:
    items = random.sample(list(item_map.keys()), 2)
    for item in items:
        purchased_date = (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')
        quantity = random.randint(1, 5)
        purchase_mode = random.choice(purchase_modes)
        sample_shoppinglist_user.append((user_map[user], item_map[item], purchased_date, quantity, purchase_mode))

cursor.executemany('INSERT INTO shoppinglist_user (user_id, item_id, purchased_date, quantity, purchase_mode) VALUES (?, ?, ?, ?, ?)', sample_shoppinglist_user)

# Commit changes and close the connection
conn.commit()
conn.close()