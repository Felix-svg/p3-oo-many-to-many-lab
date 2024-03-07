from datetime import datetime


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        if (
            not isinstance(book, Book)
            or not isinstance(date, str)
            or not isinstance(royalties, int)
        ):
            raise Exception
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
        self._authors = []

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [author for author in Author.all]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if (
            isinstance(author, Author)
            and isinstance(book, Book)
            and isinstance(date, str)
            and isinstance(royalties, int)
        ):
            self.author = author
            self.book = book
            self.date = date
            self.royalties = royalties
            Contract.all.append(self)
        else:
            raise Exception

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
