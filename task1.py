class Book:
    def __init__(self, title, author, price, stock, isbn=None):
        """Initializes a Book object.

        Args:
            title: The title of the book.
            author: The author of the book.
            price: The price of the book.
            stock: The number of copies in stock.
            isbn: (Optional) The ISBN of the book.
        """
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
        self.isbn = isbn

    def __str__(self):
        """Returns a string representation of the book."""
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}, Stock: {self.stock}"

    def update_stock(self, new_stock):
        """Updates the stock level of the book.

        Args:
            new_stock: The new stock level.
        """
        if new_stock >= 0:
            self.stock = new_stock
        else:
            print("Error: Stock cannot be negative.")

    def is_available(self):
        """Checks if the book is in stock."""
        return self.stock > 0
    
    def get_book_details(self):
        """Returns a dictionary of book details."""
        return {
            'title': self.title,
            'author': self.author,
            'price': self.price,
            'stock': self.stock,
            'isbn': self.isbn
        }