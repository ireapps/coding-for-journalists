# SQLite is a lightweight database manager that's part of Python's standard
# library, so it's a good example of how to hook a script up to a database.
# If you work in MySQL or Postgres, there are libraries you can use to make
# a connection and gain similar functionality.

import sqlite3

# Connect to a test database; if one doesn't exist, it will be created on
# the fly. We also fire up a cursor to poke, prod and manipulate our
# database.
conn = sqlite3.connect('my_test.sqlite')
c = conn.cursor()

# Right now it's an empty database with no tables and no data. Let's create
# basic one that holds some CEO information.
c.execute(
         'CREATE TABLE ceos' \
         '(ceo_name text, company text, salary int)' )

# NOTE: with scripts, somestimes it's a good idea to preface a CREATE
# TABLE query with IF NOT EXISTS, that way you won't get an operational
# error.

# Let's insert three CEO names, companies and salaries into our ceos table.
c.execute(
         "INSERT INTO ceos " \
         "VALUES ('John Smith', 'Acme, Inc.', '275000'), " \
         "('Libby Rogers', 'AstroTech', '1200000'), " \
         "('Darla Jones', 'Ballard Partners', '942000')" )

# When we alter a table, we have to commit those changes.
conn.commit()

# Let's run a quick query that gives us everything in the table.
c.execute(
         "SELECT * FROM ceos" )

# The database has run the query and gives it back to use as a list of tuples
# for each row. We have to fetch this information.
result = c.fetchall()
print result

# Try fetchall() again; it should be empty and will be until we run another
# query.
c.fetchall()

# Let's try another basic query: a sum of the salaries.
c.execute(
         "SELECT SUM(salary) FROM ceos" )
result2 = c.fetchall()
print result2

# One more: companies that start with 'A,' sorted in descending order by
# salary
c.execute(
         "SELECT * FROM ceos " \
         "WHERE company LIKE 'A%' " \
         "ORDER BY salary DESC" )
result3 = c.fetchall()
print result3
