'''
~ Learning Journal / Programming Diary with Python & SQLite

Python file that contains all the application logic.
'''

# 03-04 Using Python lists as a database | The Complete Python/PostgreSQL Course 2.0
# https://pysql.tecladocode.com/section03/lectures/04_python_lists_as_database/

# ~ Using the database in app.py

# Make use of the data store.
# We need to use the data store instead of print "Adding..." or "Viewing...".
from database import add_entry, get_entries

WELCOME = "Welcome to the Learning Journal!"
print('\n' + WELCOME)

MENU = """\nPlease select one of the following options:

1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """


# ~ Modify `app.py` so that it does the user interaction only

# We could improve the code inside `app.py` further by splitting it into functions:
def prompt_new_entry():
    '''Function for interacting with the user in order to add new entry.'''
    entry_content = input("\nWhat have you learned today? ")
    entry_date = input("Enter the date: ")

    add_entry(entry_content, entry_date)


def view_entries(entries):
    '''Funcion for viewing all entries from the data store.'''
    for entry in entries:
        print(f"\n{entry['date']}\n{entry['content']}")


# Using Python 3.8's Walrus Operator (`walrus` | морж)
while (user_input := input(MENU)) != "3":
    # We'll deal with user input here...
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("Invalid option, please try again!")

print("\nGoodbye! See you next time! ;-)\n")
