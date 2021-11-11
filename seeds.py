from db import Book

print("Seeding Books ...")
Book.clearTable()
Book(title="2001: A Space Odyssey", publisher="Hutchinson", yearPublished=1968)
Book(title="The Fellowship of the Ring", publisher="Allen & Unwin", yearPublished=1954)
Book(title="Harry Potter and the Philosopher's Stone", publisher="Bloomsbury", yearPublished=1997)
print("Done.")
