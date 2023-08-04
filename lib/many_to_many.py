from datetime import datetime

class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.contracts = []
        self.books_list = []
        Author.all_authors.append(self)
    
    def get_contracts(self):
        return self.contracts

    def books(self):
        return self.books_list
    
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book object.")
        if not isinstance(date, str) or not self.is_valid_date_format(date):
            raise Exception("Invalid date format. Date must be in the format 'dd/mm/yyyy'.")
        if not isinstance(royalties, int) or royalties < 0 or royalties > 100:
            raise Exception("Invalid royalties percentage.  Royalties must be an integer between 0 and 100.")
        
        contract = Contract(self, book, date, royalties)
        self.contracts.append(contract)  
        self.books_list.append(book)
        book.authors_list.append(self)
        return contract
    
    def is_valid_date_format(self, date):
        try:
            datetime.strptime(date, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def total_royalties(self):
        return sum(contract.royalties / 100 for contract in self.contracts) 


class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.contracts_list = []
        self.authors_list = []
        Book.all_books.append(self)

    def contracts(self):
        return self.contracts_list

    def authors(self):
        return self.authors_list


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author object.")
        if not isinstance(book, Book):
            raise Exception("Invalid book object.")
        if not isinstance(date, str) or not self.is_valid_date_format(date):
            raise Exception("Invalid date format. Date must be in the format 'dd/mm/yyyy'.")
        if not isinstance(royalties, int) or royalties < 0 or royalties > 100:
            raise Exception("Invalid royalties percentage")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all_contracts, key=lambda contract: contract.date)
    
    def is_valid_date_format(self,date):
        try:
            datetime.strptime(date, '%d/%m/%Y')
            return True
        except ValueError:
            return False
