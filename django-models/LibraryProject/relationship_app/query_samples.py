from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = author.books.all()
print("Books by", author.name)
for book in books_by_author:
    print("-", book.title)

# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("\nBooks in", library.name)
for book in books_in_library:
    print("-", book.title)

# Retrieve the librarian for a library
librarian = library.librarian
print("\nLibrarian for", library.name, "is", librarian.name)
