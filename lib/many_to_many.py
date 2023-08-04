class Author:
    all_authors =[]

    def __init__(self, name):
        self.name = name
        self.contacts_list = []
        self.book.list = []
        Author.all_authors.append(self)
    
    def contacts(self):
        return self.contacts_list

    def books(self):
        return self.book_list
    
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book object.")
        if not isinstance(date, str):
            raise Exception("Invalid date format.")
        if not isinstance(royalties, int) or royalties < 0 or royalties > 100:
            raise Exception("Invalid  ryalties percentage")
        
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        self.book_list.append(book)
        return contract
class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)


class Contract:
    all_contacts = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]