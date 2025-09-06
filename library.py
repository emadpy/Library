class Library:

    def __init__(self):
        self.books = []


    def add_book(self, title, author):
        if title and author and title.strip() and author.strip():
            self.books.append({"title": title, "author": author})

    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)

    def search_book(self, title):
        for book in self.books:
            if book["title"] == title:
                print(book)

    def show_books(self):
        for book in self.books:
            print(f"Title: {book['title']} | Author: {book['author']}")