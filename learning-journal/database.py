'''
~ Creating a database file

Python file that contains the logic that interacts with the data store.
For now the data store is a list, but later on it'll be a database.
'''
import sqlite3  # use this built-in module to interact with SQLite from within Python

# connection object here is more useful, then inside the function
connection = sqlite3.connect('data.db')


# Whenever SQLite executes a query and builds a result set, it puts each resultant row
# of data into the cursor as a tuple. But we can tell it to create an object instead.

# If we tell it to create an object, we can make that object allow us to access each
# column by its name instead of by index.

# Fortunately, we don't have to code these objects ourselves.
# SQLite comes with one that does it all for us.
# To tell SQLite to use it when fetching results, all we have to do is this:
connection.row_factory = sqlite3.Row
# What that'll do is for each row of data, SQLite will put the data into a `sqlite3.Row`
# object that allows us to access the data by the name of the column.


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
    '''Select all inputs from the `entry` table.
    This will return the cursor, and then we can iterate over the cursor inside `app.py`.
    '''
    return connection.execute("SELECT * FROM entry;")


def close_connection():
    """
    ALWAYS close connection, when you've finished working with DB!
    """
    connection.close()
    print("Connection to the DB is closed!")
