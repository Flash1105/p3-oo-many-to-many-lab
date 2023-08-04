from datetime import datetime

class Author:
    all_authors =[]

    def __init__(self, name):
        self.name = name
        self.contracts = []
        self.book = []
        Author.all_authors.append(self)
    
    def contracts(self):
        return self.contracts

    def books(self):
        return self.book
    
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book object.")
        if not isinstance(date, str):
            raise Exception("Invalid date format.")
        if not isinstance(royalties, int) or royalties < 0 or royalties > 100:
            raise Exception("Invalid  ryalties percentage")
        
        contract = Contract(self, book, date, royalties)
        self.contracts.append(contract)
        self.book.append(book)
        book.authors_list.append(self)
        return contract
    
    @staticmethod
    def is_valid_date_format(date):
        try:
            datetime.strptime(date, '%d/%m/%Y')
            return True
        except ValueError:
            return False
                              
class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.contracts = []
        self.authors = []
        Book.all_books.append(self)


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author object.")
        if not isinstance(book, Book):
            raise Exception("Invalid book object.")
        if not isinstance(date, str) or not Contract.is_valid_date_format(date):
            raise Exception("Invalid date format. date must be in the format 'dd/mm/yyyy'")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @staticmethod
    def is_valid_date_format(date):
        try:
            datetime.strptime(date, '%d/%m/%Y')
            return True
        except ValueError:
            return False
