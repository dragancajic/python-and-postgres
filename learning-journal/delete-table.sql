-- delete an entire table and all its data
DROP TABLE user;

-- You'll get an error if you try to drop a table that doesn't exist!
-- So, to avoid the error, try this:
DROP TABLE IF EXISTS user;
