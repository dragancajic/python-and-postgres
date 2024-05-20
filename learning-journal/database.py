'''
~ Creating a database file

Python file that contains the logic that interacts with the data store.
For now the data store is a list, but later on it'll be a database.
'''
import sqlite3  # use this built-in module to interact with SQLite from within Python

# connection object here is more useful, then inside the function
connection = sqlite3.connect('data.db')

# You can think of the *cursor* as the arrow that moves from row to row.
# We use it to point at each row as we process it (or in this case, access it):
cursor = connection.cursor()
cursor.execute("SELECT * FROM user;")

for row in cursor:
    print(row)

# However it makes less sense with code like this:
cursor.execute("DROP TABLE IF EXISTS account;")
cursor.execute("CREATE TABLE IF NOT EXISTS account (name TEXT, number TEXT);")
cursor.execute("INSERT INTO account VALUES ('John Smith', '35');")

# I believe that this is just to make the code more consistent.
# Every query uses a cursor, and that's it! ;-)

# close connection to the DB when you have finished working with DB! ;-)
#connection.close()


def create_table():
    """
    Function that will be in charge of creating the table.

    ~ What is a transaction?

    A **transaction** is a sequence of operations performed
    (using one or more SQL statements) on a database as a `single logical unit of work`.

    The effects of all the SQL statements in a **transaction** can be either ALL
    *committed* (applied to the database) OR all *rolled back* (undone from the database).
    """
    # The easiest way to handle both *committing* and *rolling back*
    # in one go is by using the **context manager**:
    with connection:  # committing and/or rolling back using `context manager`!
        connection.execute("CREATE TABLE IF NOT EXISTS entry (content TEXT, date TEXT);")
    # When you use the **context manager***, `with connection`, it'll automatically
    # *commit* for you at the end of the *context manager*, or *roll back* if an error
    # was encountered.

# Didn't we skip cursors before?

# But actually, the `connection.execute` method creates a cursor for you, so it really is
# the same thing as creating the cursor manually. However, it is a little bit shorter so
# you can use this when you don't need to make it explicit that a cursor is being used.

# The `connection.execute` method returns the **cursor** for you, so you can always
# use it to go through rows if you were executing a `SELECT` statement.


### Decoupling data from display ###

entries = []  # list of dictionaries is not used anymore!

# put data into SQLite DB, instead of using `entries` list data store
def add_entry(content, date):
    '''Insert new entry into `SQLite` DB's `entry` table.'''
    with connection:
        connection.execute(
            "INSERT INTO entry VALUES (?, ?);",
            (content, date)
        )


# Get entries from the data store
def get_entries():
    '''Get all content from the `entries` list of dictionaries'''
    print('\nYour entry is in the DB, ...')
    print("Sorry! It'll be shown later.")
    return entries  # `entries` list is empty now, use DB table!


def close_connection():
    """
    ALWAYS close connection, when you've finished working with DB!
    """
    connection.close()
    print("Connection to the DB is closed!")
