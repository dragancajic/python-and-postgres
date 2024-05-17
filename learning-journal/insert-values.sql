-- clean data by dropping/deleting table(s)
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS account;

-- create dropped/deleted table(s) again
CREATE TABLE IF NOT EXISTS user (first_name TEXT, surname TEXT);
CREATE TABLE IF NOT EXISTS account (name TEXT, number TEXT);

-- insert some data into newly created table(s)
-- INSERT INTO table_name VALUES (value1, value2, ...)
INSERT INTO account VALUES ('John Smith', '35');
INSERT INTO user VALUES ('Dragan', 'Cajic');
INSERT INTO user VALUES ('Драган', 'Ћајић');
INSERT INTO user VALUES ('Dragan', 'Ćajić');

-- select/show all data from `user` table
SELECT * FROM user;
