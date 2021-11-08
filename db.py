from sqlobject import *

con = connectionForURI("postgres://postgres:postgres@localhost/bookclub_flask")
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
