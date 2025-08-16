import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Drop each table
for table_name in tables:
    print(f"Dropping table: {table_name[0]}")
    cursor.execute(f"DROP TABLE IF EXISTS {table_name[0]}")

conn.commit()
conn.close()
print("All tables dropped from school.db.")