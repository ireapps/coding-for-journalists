# SQLite is a lightweight database manager that's part of Python's standard
# library, so it's a good example of how to hook a script up to a database.
# If you work in MySQL or Postgres, there are libraries you can use to make
# a connection and gain similar functionality.



# Connect to a test database; if one doesn't exist, it will be created on
# the fly. We also fire up a cursor to poke, prod and manipulate our
# database.



# Right now it's an empty database with no tables and no data. Let's create
# basic one that holds some CEO information.




# NOTE: with scripts, somestimes it's a good idea to preface a CREATE
# TABLE query with IF NOT EXISTS, that way you won't get an operational
# error.

# Let's insert three CEO names, companies and salaries into our ceos table.






# When we alter a table, we have to commit those changes.


# Let's run a quick query that gives us everything in the table.



# The database has run the query and gives it back to use as a list of tuples
# for each row. We have to fetch this information.



# Try fetchall() again; it should be empty and will be until we run another
# query.


# Let's try another basic query: a sum of the salaries.





# One more: companies that start with 'A,' sorted in descending order by
# salary






