import sqlite3

with open("music.sql", "r") as file:
    sql_script = file.read()

conn = sqlite3.connect("music.db")
cursor = conn.cursor()

cursor.executescript(sql_script)
conn.commit()
conn.close()

print("✅ music.db created successfully.")
