from datetime import datetime

class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        self._books_list = []
        Author.all_authors.append(self)
    
    def contracts(self):
        return self._contracts

    def _get_books(self):
        return self._books_list

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        book.contracts().append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)

    books = property(_get_books)

class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        self._authors_list = []
        Book.all_books.append(self)
    
    def contracts(self):
        return self._contracts

    def _get_authors(self):
        return self._authors_list

    authors = property(_get_authors)

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Contract class should validate author of type Author")
        if not isinstance(book, Book):
            raise TypeError("Contract class should validate book of type Book")
        if not isinstance(date, str):
            raise TypeError("Contract class should validate date of type str")
        if not isinstance(royalties, int):
            raise TypeError("Contract class should validate royalties of type int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all_contracts, key=lambda contract: datetime.strptime(contract.date, '%m/%d/%Y'))
