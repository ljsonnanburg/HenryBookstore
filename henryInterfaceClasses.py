class Author():
    def __init__(self, author_num, author_last, author_first):
        self.author_num = author_num
        self.author_last = author_last
        self.author_first = author_first
        
    def __str__(self):
        return("Author number %d is named %s %s" %(self.author_num, self.author_first, self.author_last))
    
class Book():
    def __init__(self, book_code, title, publisher_code, book_type, price, paperback):
        self.book_code = book_code
        self.title = title
        self.publisher_code = publisher_code
        self.book_type = book_type
        self.price = price
        self.paperback = paperback
    
    def __str__(self):
        return("The book with code %s is titled %s. Published by %s. Genre is %s. Price is %f. Is it paperback? %s" %(self.book_code, self.title, self.publisher_code, self.book_type, self.price, self.paperback))
    
class Publisher():
    def __init__(self, publisher_code, publisher_name):
        self.publisher_code = publisher_code
        self.publisher_name = publisher_name

class Availability():
    def __init__(self, branch_name, on_hand):
        self.branch_name = branch_name
        self.on_hand = on_hand
    
    def __str__(self):
        return("%s has %d copies of this book" % (self.branch_name, self.on_hand))