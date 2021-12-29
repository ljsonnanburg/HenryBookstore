# first need to make sure connector is installed:
#  pip install mysql-connector-python

import mysql.connector
import copy
from henryInterfaceClasses import Author
from henryInterfaceClasses import Book
from henryInterfaceClasses import Publisher
from henryInterfaceClasses import Availability
class HenryDAO():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            user='root',
            passwd='ilovesql',
            database='comp3421',
            host='127.0.0.1')

        self.mycur = self.mydb.cursor()
        
        
        
    def close(self):
        self.mydb.commit()
        self.mydb.close()
        
    def getAuthorData(self):
        self.authors = [] # empty list to populate with actor objects
        sql = "SELECT * FROM henry_author"; # sql query to fetch author data
        self.mycur.execute(sql); 
        for row in self.mycur: # make this create author objects4
            newAuthor = Author(row[0], row[1], row[2])
            self.authors.append(newAuthor)
    
    def getCategoryData(self):
        self.categories =[]
        sql = "SELECT DISTINCT TYPE FROM HENRY_BOOK";
        self.mycur.execute(sql);
        for row in self.mycur:
            self.categories.append(row)
    
    def getPublisherData(self):
        self.publishers = []
        sql = "SELECT PUBLISHER_CODE, PUBLISHER_NAME FROM HENRY_PUBLISHER";
        self.mycur.execute(sql);
        for row in self.mycur:
            newPublisher = Publisher(row[0], row[1])
            self.publishers.append(newPublisher)
        
    def getBookData(self):
        self.books = []
        sql = "SELECT * FROM henry_book";
        self.mycur.execute(sql);
        for row in self.mycur:
            newBook = Book(row[0], row[1], row[2], row[3], row[4], row[5])
            self.books.append(newBook)
    
    def authorSearch(self, author_id):
        # SQL query to find books by author
        
        self.books_by_author = []
        sql = ("SELECT * FROM henry_book WHERE BOOK_CODE IN (SELECT BOOK_CODE FROM HENRY_WROTE WHERE AUTHOR_NUM = %d)" %(author_id));
        
        self.mycur.execute(sql);
        for row in self.mycur:
            authorBook = Book(row[0], row[1], row[2], row[3], row[4], row[5])
            self.books_by_author.append(authorBook)

    def categorySearch(self, category):
        self.books_in_category = []
        sql = ("SELECT * FROM henry_book WHERE TYPE = '%s'" %(category))
        self.mycur.execute(sql);
        for row in self.mycur:
            categoryBook = Book(row[0], row[1], row[2], row[3], row[4], row[5])
            self.books_in_category.append(categoryBook)
    
    def publisherSearch(self, publisher_code):
        self.publisher_books = []
        sql = ("SELECT * FROM henry_book WHERE PUBLISHER_CODE = '%s'" %(publisher_code))
        self.mycur.execute(sql);
        for row in self.mycur:
            publisherBook = Book(row[0], row[1], row[2], row[3], row[4], row[5])
            self.publisher_books.append(publisherBook)
            
    def getBookAvailability(self, book_code):
        self.book_availability = []
        sql = ("SELECT BRANCH_NAME, ON_HAND FROM HENRY_INVENTORY JOIN HENRY_BRANCH ON HENRY_INVENTORY.BRANCH_NUM = henry_branch.BRANCH_NUM WHERE BOOK_CODE = '%s'" %(book_code));
        self.mycur.execute(sql);
        for row in self.mycur:
            inStock = Availability(row[0], row[1])
            self.book_availability.append(inStock)






if __name__ == '__main__':
# Testing stuff
    test = HenryDAO()
    test.getAuthorData()
    test.getBookData()
    #test.getBookAvailability("138X")
    #test.categorySearch("ART")
    test.publisherSearch("AP")
    test.close()
