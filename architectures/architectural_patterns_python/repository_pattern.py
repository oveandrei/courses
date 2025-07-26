from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional

# --- Model ---
@dataclass
class Book:
    id: int
    title: str
    author: str

# --- Repository Interface ---
class BookRepository(ABC):
    @abstractmethod
    def get_by_id(self, book_id: int) -> Optional[Book]:
        """Retrieve a book by its ID."""
        pass

    @abstractmethod
    def get_all(self) -> List[Book]:
        """Retrieve all books."""
        pass

    @abstractmethod
    def add(self, book: Book) -> None:
        """Add a new book."""
        pass

    @abstractmethod
    def update(self, book: Book) -> None:
        """Update an existing book."""
        pass

    @abstractmethod
    def delete(self, book_id: int) -> None:
        """Delete a book by ID."""
        pass

# --- Concrete Repository Implementation ---
class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books = {}

    def get_by_id(self, book_id: int) -> Optional[Book]:
        return self.books.get(book_id)

    def get_all(self) -> List[Book]:
        return list(self.books.values())

    def add(self, book: Book) -> None:
        if book.id in self.books:
            raise ValueError(f"Book with id {book.id} already exists.")
        self.books[book.id] = book

    def update(self, book: Book) -> None:
        if book.id not in self.books:
            raise ValueError(f"Book with id {book.id} not found.")
        self.books[book.id] = book

    def delete(self, book_id: int) -> None:
        if book_id not in self.books:
            raise ValueError(f"Book with id {book_id} not found.")
        del self.books[book_id]

# --- Service Layer ---
class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def add_book(self, book: Book) -> None:
        self.repository.add(book)

    def get_book(self, book_id: int) -> Optional[Book]:
        return self.repository.get_by_id(book_id)

    def list_books(self) -> List[Book]:
        return self.repository.get_all()

    def update_book(self, book: Book) -> None:
        self.repository.update(book)

    def delete_book(self, book_id: int) -> None:
        self.repository.delete(book_id)

# --- Example Usage ---
if __name__ == "__main__":
    repo = InMemoryBookRepository()
    service = BookService(repo)

    # Add books with manually assigned IDs
    service.add_book(Book(1, "1984", "George Orwell"))
    service.add_book(Book(2, "Brave New World", "Aldous Huxley"))

    print("Books after adding:")
    for b in service.list_books():
        print(b)

    # Update a book
    service.update_book(Book(1, "Nineteen Eighty-Four", "George Orwell"))

    print("\nBook with ID 1 after update:")
    print(service.get_book(1))

    # Delete a book
    service.delete_book(2)

    print("\nBooks after deletion:")
    for b in service.list_books():
        print(b)
