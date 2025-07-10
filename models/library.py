# models/library.py

from models.book import Book
from typing import List
import json
from datetime import date
import os


class Library:
    # Library class to manage a collection of books
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)
    
    # List all books in the library
    def list_books(self):
        return self.books
    
    # Save the library to a JSON file
    def save_to_file(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            data = [self._book_to_dict(book) for book in self.books]
            json.dump(data, f, indent=4, ensure_ascii=False, default=str)

    # Load the library from a JSON file
    def load_from_file(self, path: str):
        if not os.path.exists(path):
            return  # File does not exist — no books to load
        with open(path, "r", encoding="utf-8") as f:
            raw_books = json.load(f)
            self.books = [self._book_from_dict(b) for b in raw_books]

    # Helper methods to convert Book to/from dict
    def _book_to_dict(self, book: Book) -> dict:
        return {
            "title": book.title,
            "author": book.author,
            "category": book.category,
            "start_date": book.start_date.isoformat() if book.start_date else None,
            "end_date": book.end_date.isoformat() if book.end_date else None,
            "rating": book.rating,
            "notes": book.notes,
            "quotes": book.quotes
        }

    def _book_from_dict(self, data: dict) -> Book:
        return Book(
            title=data["title"],
            author=data["author"],
            category=data["category"],
            start_date=date.fromisoformat(data["start_date"]) if data.get("start_date") else None,
            end_date=date.fromisoformat(data["end_date"]) if data.get("end_date") else None,
            rating=data.get("rating"),
            notes=data.get("notes", ""),
            quotes=data.get("quotes", [])
        )
    
    # Search methods
    def find_books_by_title(self, keyword: str) -> List[Book]:
        keyword = keyword.lower()
        return [book for book in self.books if keyword in book.title.lower()]

    def find_books_by_author(self, name: str) -> List[Book]:
        name = name.lower()
        return [book for book in self.books if name in book.author.lower()]

    def find_books_by_category(self, category: str) -> List[Book]:
        category = category.lower()
        return [book for book in self.books if category in book.category.lower()]

    def search_books_by_notes_or_quotes(self, keyword: str) -> List[Book]:
        keyword = keyword.lower()
        return [
            book for book in self.books
            if keyword in book.notes.lower() or
               any(keyword in quote.lower() for quote in book.quotes)
        ]