#This is a list to remember peoples birthdays bc you forget

import json

def load_birthdays(filename="birthdays.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_birthdays(birthdays, filename="birthdays.json"):
    with open(filename, "w") as file:
        json.dump(birthdays, file, indent=4)

def add_birthday(birthdays):
    name = input("Enter the person's name: ")
    birthday = input("Enter their birthday (YYYY-MM-DD): ")
    birthdays[name] = birthday
    save_birthdays(birthdays)
    print(f"Birthday for {name} added successfully!")

def view_birthdays(birthdays):
    if not birthdays:
        print("No birthdays saved yet.")
    else:
        for name, birthday in birthdays.items():
            print(f"{name}: {birthday}")
def update_birthday(birthdays):
    name = input("Enter the name of the person whose birthday you want to update: ")
    if name in birthdays:
        new_birthday = input("Enter the new birthday (YYYY-MM-DD): ")
        birthdays[name] = new_birthday
        save_birthdays(birthdays)
        print(f"Birthday for {name} updated successfully!")
    else:
        print("Name not found in the list.")

def main():
    birthdays = load_birthdays()
    while True:
        print("\nBirthday Reminder")
        print("1. Add Birthday")
        print("2. View Birthdays")
        print("3. Update Birthday")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_birthday(birthdays)
        elif choice == "2":
            view_birthdays(birthdays)
        elif choice == "3":
            update_birthday(birthdays)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()

