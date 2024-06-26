'''
~ Learning Journal / Programming Diary with Python & SQLite

Python file that contains all the application logic.
'''
from database import add_entry, get_entries
from database import create_table, close_connection

WELCOME = "Welcome to the Learning Journal!"
print('\n' + WELCOME)

MENU = """\nPlease select one of the following options:

1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

def prompt_new_entry():
    '''Function for interacting with the user in order to add new entry.'''
    entry_content = input("\nWhat have you learned today? ")
    entry_date = input("Enter the date: ")

    # FIRST, you have to create table `entry` into wich you want to INSERT data!
    create_table()  # create `entry` table, then insert `content` and `date`!
    add_entry(entry_content, entry_date)


def view_entries(entries):
    '''Funcion for viewing all entries from the data store.
    But the cursor will use indexes instead of keys to access values.
    '''
    for entry in entries:
        print(f"\n{entry['date']}\n{entry['content']}")


# Using Python 3.8's Walrus Operator (`walrus` [wol-rus] | морж) √
while (user_input := input(MENU)) != "3":
    # We'll deal with user input here...
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("Invalid option, please try again!")


# Now, in `app.py` we must call `close_connection()` when the user exits the application.
# This is only called when the `while` loop ends.
close_connection()

print("\nGoodbye! See you next time! ;-)\n")
