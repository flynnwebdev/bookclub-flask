from sqlobject import *
from dotenv import dotenv_values

uri = "postgres://%(PG_USER)s:%(PG_PASS)s@%(PG_HOST)s:%(PG_PORT)s/bookclub_flask" % dotenv_values()

con = connectionForURI(uri)
sqlhub.processConnection = con

class Book(SQLObject):
    title = StringCol()
    publisher = StringCol()
    yearPublished = IntCol()


# Run this file directly to reset/create the db and ORM tables
if __name__ == "__main__":
    con.dropDatabase()
    con.createEmptyDatabase()
    Book.createTable()
