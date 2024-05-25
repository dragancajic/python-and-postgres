-- ~ WHERE: filter through data ~

SELECT * FROM user WHERE first_name = 'John';
-- ... WHERE age > 18;
-- ... WHERE salary < 35000;
-- ... WHERE surname != 'Smith';


-- Multiple comparisons

-- find employees that should be considered for promotion
-- ... WHERE years_experience > 10 AND salary < 35000;

-- find those people who might not be in working age
-- ... WHERE age <= 18 OR age >= 65;


-- More than one chaining keyword

-- return rows where at least one of the comparisons match:
-- ▪ if the person is 18 or under,
-- ▪ if the person is 65 or over,
-- ▪ if the person's salary is exactly 0.
-- ... WHERE age <= 18 OR age >= 65 OR salary = 0;

-- You can use both AND and OR in one query, although it can get a bit confusing:
-- ... WHERE age <= 18 OR age >= 65 AND salary > 0;
-- could be used to get those people who are not in normal working age, but are
-- currently working.
-- BUT,
-- when you're working with multiple chained operators, it's a good idea to use brackets
-- (a.k.a. parentheses) to tell the database the order of evaluation of the conditionals:
-- ... WHERE age <= 18 OR (age >= 65 AND salary > 0);
-- ... WHERE (age <= 18 OR age >= 65) AND salary > 0;

-- This is one of those situations where explaining how the logic is evaluated using
-- plain English becomes more difficult than with code!


-- Long queries

SELECT first_name, surname, age, salary FROM users WHERE (age <= 18 OR age >= 65) AND salary > 0;

-- To make it easier for a reader of the code (yourself or someone else), it can be
-- a good idea to split it into multiple lines.
-- You can do this without worrying, because SQL doesn't care about new lines in a query.
-- It only cares about the final semicolon that marks the end of the query:

SELECT first_name, surname, age, salary
FROM users
WHERE (age <= 18 OR age >= 65) AND salary > 0;

-- or maybe like this:

SELECT
    first_name,
    surname,
    age,
    salary
FROM user
WHERE (age <= 18 OR age >= 65) AND salary > 0;
