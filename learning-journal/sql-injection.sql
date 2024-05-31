-- ~ What is a SQL Injection Attack? ~

SELECT * FROM user WHERE first_name = ?;
/*
GET_USER = "SELECT * FROM users WHERE first_name = {};"

def get_user(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_USER.format(username))
        return cursor.fetchall()
*/

/*
Welcome to the username searching app!

Enter your username:
*/

/*
Welcome to the username searching app!

Enter your username: ''; DROP TABLE users;
*/

-- PROBLEM! LOOK! :eyes:
SELECT * FROM users WHERE first_name = ''; DROP TABLE user;

-- If you had used `?` instead of string formatting, you wouldn't have this problem
-- because `sqlite3` will automatically prevent this stuff from happening if you use
-- arguments in the `.execute()` method, as we've learned.

-- This would save you:
/*
GET_USER = "SELECT * FROM users WHERE first_name = ?;"

def get_user(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(GET_USER, (username,))
        return cursor.fetchall()
*/

-- SQL Injection attacks can happen when developers are not careful.
-- Now you know what they are, so remember to use arguments in `sqlite3`
-- and NEVER construct your queries by FORMATTING STRINGS!
