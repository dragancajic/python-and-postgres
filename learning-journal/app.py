'''
~ Learning Journal / Programming Diary with Python & SQLite
'''

# 03-02 Creating our user menu | The Complete Python/PostgreSQL Course 2.0
# https://pysql.tecladocode.com/section03/lectures/02_creating_user_menu/

WELCOME = "Welcome to the Learning Journal!"
print('\n' + WELCOME + '\n')

MENU = """Please select one of the following options:

1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

# user_input = input(MENU)
# while user_input != "3":
#     # We'll deal with user input here...
#     if user_input == "1":
#         print("Adding...")
#     elif user_input == "2":
#         print("Viewing...")
#     else:
#         print("Invalid option, please try again!")

#     user_input = input('\n' + MENU)


# Using Python 3.8's Walrus Operator (`walrus` | морж)
while (user_input := input(MENU)) != "3":
    # We'll deal with user input here...
    if user_input == "1":
        print("Adding...")
    elif user_input == "2":
        print("Viewing...")
    else:
        print("Invalid option, please try again!")
    print()  # empty line
