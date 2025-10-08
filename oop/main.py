class Library:
    def __init__(self):
        self.books = []  # Initialize an empty list to store books

    def add_book(self, book):
        self.books.append(book)  # Add Book, EBook, or PrintBook instance to the list

    def list_books(self):
        for book in self.books:
            print(book)  # This will call the __str__ method of each book type
