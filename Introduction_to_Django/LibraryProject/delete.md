
---

## ❌ **delete.md**

```markdown
### Delete Operation

```python
from bookshelf.models import Book

# Delete the created book and confirm deletion
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()
# Expected Output:
# <QuerySet []>
# Successfully deleted the book; no books remain in the database
