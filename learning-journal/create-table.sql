CREATE TABLE IF NOT EXISTS user (first_name TEXT, surname TEXT);
CREATE TABLE IF NOT EXISTS account (name TEXT, number TEXT);
CREATE TABLE IF NOT EXISTS entry (content TEXT, date TEXT);


-- check if the table with name `entry` exists in SQLite DB
SELECT name FROM sqlite_master WHERE type='table' AND name='entry';
-- This query will return the `name` of the table if it exists in the database.
-- If no rows are returned, then the table does not exist.
