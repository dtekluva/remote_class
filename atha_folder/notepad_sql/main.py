from note_pad import *


print("Welcome to Our Notes App\n")

has_account = input("Please Do you have an account (y/n) ? > ")

if has_account == "y":
    get_all_users()

    print("Please enter the name related to you from the list below  \n\n")
    selected_name = input("NAME > ")

    user = get_user(name = selected_name)[0]
    name = user.get("name")
    id = user.get("id")

    print(f"Welcome {name}")
    notes = get_note(id)
    display_notes(notes)
    chosen_note = (input("\nPlease enter note (ID) to display \n or Enter (ADD) to add a new note > ") )

    if chosen_note.upper() == "ADD":
        note_title = input("Enter note title : ")
        note_body = input("Enter note body : ")
        write_note(user_id=id, title=note_title, body=note_body)
    else:

        display_one_note(notes, int(chosen_note))

    

else:
    create_account = input("Would You like to create an account (y/n) ? > ")

    if create_account == "y":

        name = input("Please enter Name > ")
        age = input("Please enter Age > ")

        write_user(name, age)
    else:
        print("Bye For now.")