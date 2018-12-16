# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:51:39 2018

@author: Administrator
"""
from typing import List

class UnableToFindAuthorError(RuntimeError):
    pass

class UnableToFindBookError(RuntimeError):
    pass

class UnableToFindPatronError(RuntimeError):
    pass

class AlreadyCheckedOutError(RuntimeError):
    pass

class HaveNotCheckedToError(RuntimeError):
    pass

class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author
        self.checkedTo = None #type: str

class Author:
    def __init__(self, name: str):
        self.name = name
        self.book_list = list() #type: List[Book]
        
    def includeBook(self, book_name: str):
        book = self.searchBook(book_name)
        if book is None:
            self.book_list.append(Book(book_name, self.name))
            
    def searchBook(self, book:str)->Book:
        for b in self.book_list:
            if b.name == book:
                return b
        return None

class Patron:
    def __init__(self, name: str):
        self.name = name #type: str
        self.book_list = list()
        
    def hasNoBook(self):
        return len(self.book_list) == 0
        
    def checkOutBook(self, book: Book):
        book.checkedTo = self.name
        self.book_list.append(book)
        
    def returnBook(self, book: Book):
        book.checkedTo = None
        self.book_list.remove(book)
        
    def searchBook(self, book:str)->Book:
        for b in self.book_list:
            if b.name == book:
                return b
        return None


class Library:
    def __init__(self):
        self.author_list = list() #type: List[Author]
        self.patron_list = list() #type: List[patron]
        
    def searchAuthor(self, author)->Author:
        for a in self.author_list:
            if a.name == author:
                return a
        return None
    
    def searchPatron(self, patron)->Patron:
        for p in self.patron_list:
            if p.name == patron:
                return p
        return None
        
    def includeBook(self, author_name:str, book_name:str):
        author = self.searchAuthor(author_name) #type: Author
        if author is not None:
            author.includeBook(book_name)
        else:
            author = Author(author_name)
            author.includeBook(book_name)
            self.author_list.append(author)
        print('Included book %s from %s' % (book_name, author_name))
            
    def checkOutBook(self, patron_name:str, author_name:str, book_name:str):
        author = self.searchAuthor(author_name)
        if author is None:
            raise UnableToFindAuthorError()
            
        book = author.searchBook(book_name)
        if book is None:
            raise UnableToFindBookError()
        if book.checkedTo is not None:
            raise AlreadyCheckedOutError()
            
        patron = self.searchPatron(patron_name) #type: Patron
        if patron is not None:
            patron.checkOutBook(book)
        else:
            patron = Patron(patron_name)
            patron.checkOutBook(book)
            self.patron_list.append(patron)
            
        print('Checked out book %s to %s' % (book_name, patron_name))
            
    def returnBook(self, patron_name:str, author_name:str, book_name:str):
        author = self.searchAuthor(author_name) #type:Author
        if author is None:
            raise UnableToFindAuthorError()
            
        book = author.searchBook(book_name)
        if book is None:
            raise UnableToFindBookError()
            
        patron = self.searchPatron(patron_name) #type: Patron
        if patron is None:
            raise UnableToFindPatronError()
            
        book = patron.searchBook(book_name)
        if book is None:
            raise HaveNotCheckedToError()
            
        patron.returnBook(book)
        if patron.hasNoBook():
            self.patron_list.remove(patron)
            
        print('Returned book %s from %s' % (book_name, patron_name))
            
    def print_books(self):
        print('*'*10 + 'books in library' + '*'*10)
        for author in self.author_list:
            print(author.name)
            for book in author.book_list:
                print('  * '+book.name)
                if book.checkedTo is not None:
                    print('   - checked to '+book.checkedTo)
        print('-'*40)
    
    def print_patrons(self):
        print('*'*10 + 'books checked out' + '*'*10)
        for patron in self.patron_list:
            print(patron.name)
            for book in patron.book_list:
                print('  * '+book.name + '\n')
        print('-'*40)
        
            
if __name__ == '__main__':
    lib = Library()
    lib.includeBook('Scott Meyers', 'Effective C++')
    lib.includeBook('Scott Meyers', 'More Effective C++')
    lib.includeBook('Stanley B. Lippman', 'Essential C++')
    lib.includeBook('David Vandevoorde', 'C++ Templates')
    
    lib.checkOutBook('Jiangtao', 'Scott Meyers', 'Effective C++')
    lib.print_books()
    lib.print_patrons()
    
    lib.returnBook('Jiangtao', 'Scott Meyers', 'Effective C++')
    lib.print_books()
    lib.print_patrons()
            
        
            
        
        
        

