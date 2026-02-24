CLASS_CODE = "CS111_W26_HBLL_CARD"

class LibraryCard:
    def __init__(self, name):
        self.name = name
        self.books = []
    def checkout_book(self, title):
        if len(self.books) > 2:
            return f"Limit Reached."
        else:
            self.books.append(title)
            return f"{title} has been checked out."
    def has_book(self, title):
        for book in self.books:
            if title == book:
                return True
        return False
    def return_book(self, title):
        for book in self.books:
            if title == book:
                self.books.remove(book)
                return f"{title} has been returned."
        return f"{title} hasn't been checked out."
    def __str__(self):
        if len(self.books) > 0:
            return f"{self.name} has checked out: {self.books}"
        else:
            return f"{self.name} has no books checked out."
    def __eq__(self, other):   
            return sorted(self.books) == sorted(other.books)

