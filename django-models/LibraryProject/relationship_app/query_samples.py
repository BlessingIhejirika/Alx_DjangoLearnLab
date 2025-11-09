from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = author.books.all()
print("Books by", author.name)
for book in books_by_author:
    print("-", book.title)

# 2. List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("\nBooks in", library.name)
for book in books_in_library:
    print("-", book.title)

# 3. Retrieve the librarian for a library
librarian = library.librarian
print("\nLibrarian for", library.name, "is", librarian.name)
