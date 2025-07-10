# models/book.py

from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional

@dataclass
class Book:
    title: str
    author: str
    category: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    rating: Optional[int] = None
    notes: str = ""
    quotes: List[str] = field(default_factory=list)

    def add_quote(self, quote: str):
        if quote:
            self.quotes.append(quote)

    def __str__(self):
        return f'"{self.title}" by {self.author} ({self.category})'