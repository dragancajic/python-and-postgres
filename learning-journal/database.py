'''
~ Creating a database file

Python file that contains the logic that interacts with the data store.
For now the data store is a list, but later on it'll be a database.
'''
import sqlite3  # use this built-in module to interact with SQLite from within Python

# connection object here is more useful, then inside the function
connection = sqlite3.connect('data.db')

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
        connection.execute("CREATE TABLE entry (content TEXT, date TEXT);")
    # When you use the **context manager***, `with connection`, it'll automatically
    # *commit* for you at the end of the *context manager*, or *roll back* if an error
    # was encountered.


def close_connection():
    """
    ALWAYS close connection, when you've finished working with DB!
    """
    connection.close()
    print("Connection to the DB is closed!")


entries = []

# Decoupling data from display

# Add an entry to the data store
def add_entry(entry_content, entry_date):
    '''Add/Append new entry into `entries` list of dictionaries.'''
    entries.append({"content": entry_content, "date": entry_date})


# Get entries from the data store
def get_entries():
    '''Get all content from the `entries` list of dictionaries'''
    return entries
