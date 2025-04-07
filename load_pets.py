import sqlite3

from pyodbc import connect

# connect to the database
conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

# insert people
people = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara','White', 27),
    (4, 'William','Gibson', 23)
]
cursor.executemany("Insert Into person Values (?, ?, ?, ?)", people)

# insert the pets
pets = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2,'Bella', 'Alaskan Malamute', 3, 0),
    (3,'Max', 'Cocker Spaniel', 1, 0),
    (4,'Rocky', 'Beagle', 7, 0),
    (5,'Rufus', 'Cocker Spaniel', 1, 0),
    (6,'Spot', 'Bloodhound', 2, 1)
]
cursor.executemany("Insert Into pet Values (?, ?, ?, ?, ?)", pets)

# insert the relations between people and pets.
person_pet = [
    (1,1),
    (1,2),
    (2,3),
    (2,4),
    (3,5),
    (4,6)
]
cursor.executemany("Insert Into person_pet Values (?, ?)", person_pet)

# save and close.
conn.commit()
conn.close()

print("✅ Data inserted into pets.db successfully.")

if __name__ == "__main__":
    print("Running load_pets.py")
