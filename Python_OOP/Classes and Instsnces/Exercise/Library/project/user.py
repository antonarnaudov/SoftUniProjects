class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            if self.username not in library.rented_books.keys():
                library.rented_books[self.username] = {}
            library.rented_books[self.username].update({book_name: days_to_return})
            library.books_available[author].remove(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for rented in library.rented_books.values():
            for book, time in rented.items():
                if book == book_name:
                    return f'The book "{book}" is already rented' \
                           f' and will be available in {time} days!'

    def return_book(self, author: str, book_name: str, library):
        if book_name not in library.rented_books[self.username]:
            return f"{self.username} doesn't have this book in his/her records!"

        self.books.remove(book_name)
        library.books_available[author].append(book_name)
        library.rented_books[self.username].pop(book_name)

    def info(self):
        return ', '.join(sorted(self.books))

    def __str__(self):
        return f'{self.user_id}, {self.username}, {self.books}'
