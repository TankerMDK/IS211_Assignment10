import sqlite3
#Assignment question is answered near the bottom.

"""This is to create an interactive prompt"""

def main():
    conn = sqlite3.connect("pets.db")
    cursor = conn.cursor()

    # Requesting the person_id input
    while True:
        try:
            person_id = int(input("Please enter person ID OR (-1 to EXIT): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if person_id == -1:
            break

        # Fetches the person
        cursor.execute("Select first_name, last_name, age FROM person WHERE id = ?", (person_id,))
        person = cursor.fetchone()

        if person is None:
            print("Person not found.")
            continue

        # Assignments
        first_name, last_name, age = person
        print(f"\n{first_name} {last_name}, age {age}, owns the following pets:")

        # Fetching pets
        cursor.execute("""
            SELECT pet.name, pet.breed, pet.age, pet.dead
            FROM pet
            INNER JOIN person_pet ON pet.id = person_pet.pet_id
            WHERE person_pet.person_id = ?
        """, (person_id,))

        pets = cursor.fetchall()
        if not pets:
            print(" No pets were found.")
        else:
            for name, breed, age, dead in pets:
                status = "dead" if dead else "alive"
                print(f"  - {name}, a {breed}, of age {age}, is {status}.")

        print()

    conn.close()
    print("Goodbye.")

# The person_pet table handles the many-to-many relationship between people and pets.
# It allows multiple people to be linked to multiple pets, and vice versa.
# This way, the database can accurately represent shared pet ownership or pets that have had different owners over time.
# For example, (1, 1) and (1, 2) mean that Person 1 owns both Pet 1 and Pet 2.
# If we also had (2, 2), it would show Pet 2 is shared by Person 1 and Person 2

if __name__ == "__main__":
    print("Running query_pets.py")
    main()