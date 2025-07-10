from models.book import Book
from models.library import Library
from datetime import date

lib = Library()
lib.load_from_file("data/library.json")  

existing_titles = [b.title.lower() for b in lib.list_books()]

if "sapiens" not in existing_titles:
    book = Book(
        title="Sapiens",
        author="Yuval Noah Harari",
        category="History",
        start_date=date(2024, 3, 1),
        end_date=date(2024, 3, 15),
        rating=9,
        notes="Very thought-provoking.",
        quotes=["Cognitive revolution is key."]
    )
    lib.add_book(book)

if "lord of the rings" not in existing_titles:
    book2 = Book(
        title="Lord of the Rings",
        author="J.R.R. Tolkien",
        category="Fantasy",
        start_date=date(2005, 5, 14),
        end_date=date(2005, 7, 27),
        rating=10,
        notes="A masterpiece of fantasy literature.",
        quotes=["You shall not pass!"]
    )
    lib.add_book(book2)

# Save once after all additions
lib.save_to_file("data/library.json")


print("\n Search by title: 'Sapiens'")
for book in lib.find_books_by_title("Sapiens"):
    print("-", book)

print("\n Search by author: 'Tolkien'")
for book in lib.find_books_by_author("Tolkien"):
    print("-", book)

print("\n Search by category: 'Fantasy'")
for book in lib.find_books_by_category("Fantasy"):
    print("-", book)

print("\n Search by notes/quotes: 'pass'")
for book in lib.search_books_by_notes_or_quotes("pass"):
    print("-", book)

