import sqlite3

with open("pets.sql", "r") as file:
    sql_script = file.read()

conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

cursor.executescript(sql_script)
conn.commit()
conn.close()

print("✅ pets.db created successfully.")
