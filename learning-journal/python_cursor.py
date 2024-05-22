'''
~ Python's cursor for `sqlite3`

▪ What is a cursor?
- A cursor is a structure that allows us to traverse a result set.

When you have a result set loaded into a cursor, you can usually go forward and
backward in the results.
Cursors help improve `performance` by not requiring us to fetch all the rows in
a result set at once. Instead, we can ask for rows in small groups or one by one.
'''
import sqlite3  # use this built-in module to interact with SQLite from within Python

# connection object here is more useful, then inside the function
connection = sqlite3.connect('data.db')

# You can think of the *cursor* as the arrow that moves from row to row.
# We use it to point at each row as we process it (or in this case, access it):
cursor = connection.cursor()
cursor.execute("SELECT * FROM user;")

for row in cursor:
    print(row)  # tuple of one row

# However it makes less sense with code like this:
cursor.execute("DROP TABLE IF EXISTS account;")
cursor.execute("CREATE TABLE IF NOT EXISTS account (name TEXT, number TEXT);")
cursor.execute("INSERT INTO account VALUES ('John Smith', '35');")

# I believe that this is just to make the code more consistent.
# Every query uses a cursor, and that's it! ;-)

# close connection to the DB when you have finished working with DB! ;-)
connection.close()
