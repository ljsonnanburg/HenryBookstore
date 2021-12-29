import tkinter as tk
from tkinter import ttk
from henryDAO import HenryDAO




class HenrySBA():
    def __init__(self):
       
        #################################
        # Kicks off the whole tab thing #
        #################################
        self.SBAtab = ttk.Frame(tabControl)
        tabControl.add(self.SBAtab, text = "Search by Author")    
        ###############################
        # Build list for author names #
        ###############################
        self.author_names = []
        for x in henryDB.authors:
            self.author_names.append("%s %s" % (x.author_first, x.author_last))
        ##############################
        # Build list for book titles #
        ##############################
        self.book_titles = []
        for x in henryDB.books:
            self.book_titles.append(x.title)
        
        ############################
        # Creates tree view object #
        ############################
        self.tree1 = ttk.Treeview(self.SBAtab, columns=('Branch Name', 'Copies Avialable'), show='headings')
        self.tree1.heading('Branch Name', text='Branch Name')
        self.tree1.heading('Copies Avialable', text='Copies Avialable')
        self.tree1.grid(column=1, row=1)

        ##########
        # Labels #
        ##########
        
        # Label for price
        self.price = ttk.Label(self.SBAtab)
        self.price.grid(column=3, row=1)
        self.price['text'] = "Select an author, then a book"
        
        # Label for Author Selection
        self.author_select = ttk.Label(self.SBAtab)
        self.author_select.grid(column=1, row=2)
        self.author_select['text'] = "Author Selection:"
        
        # Label for Author Selection
        self.book_select = ttk.Label(self.SBAtab)
        self.book_select.grid(column=2, row=2)
        self.book_select['text'] = "Book Selection:"
          
        ##############
        # Comboboxes #
        ##############
        
        # Combobox for Author
        self.authorbox = ttk.Combobox(self.SBAtab, width = 20, state="normal")
        self.authorbox.grid(column=1, row=3)
        self.authorbox['values'] = self.author_names
        #self.authorbox.current(0)
        self.authorbox.bind("<<ComboboxSelected>>", HenrySBA.chose_author)

        # Combobox for Book
        self.bookbox = ttk.Combobox(self.SBAtab, width = 20, state="disabled")
        self.bookbox.grid(column=2, row=3)
        self.bookbox['values'] = self.book_titles
        self.bookbox.current(0)
        self.bookbox.bind("<<ComboboxSelected>>", HenrySBA.chose_book)
    
    #############################################################################
    # chose_author(event): event handling for author selection combobox         #
    #                      updates book selection combo box with author's books #
    #############################################################################
    def chose_author(event):
        # get will get its value - note that this is always a string
        selIndex = event.widget.current()
        henryDB.authorSearch(selIndex+1) # Need to bump it up by one for SQL indexing
        
        #################################################################################
        # Build list for author's book titles; indexed for easy reference by chose_book #
        #################################################################################
        henrySBA.author_book_titles = [] 
        henrySBA.author_book_codes = []
        henrySBA.author_book_prices = []
        for x in henryDB.books_by_author:
            henrySBA.author_book_titles.append(x.title)
            henrySBA.author_book_codes.append(x.book_code)
            henrySBA.author_book_prices.append(x.price)
        henrySBA.bookbox['state'] = tk.NORMAL # Once author is selected, lets user interact with book combobox
        henrySBA.bookbox['values'] = henrySBA.author_book_titles # book combobox is updated with author's work
  
    def chose_book(event):
        selIndex = event.widget.current()
        henrySBA.price['text'] = ("Price: %s" %(henrySBA.author_book_prices[selIndex]))
        henryDB.getBookAvailability(str(henrySBA.author_book_codes[selIndex]))

            
        for i in henrySBA.tree1.get_children():  # Remove any old values in tree list
            henrySBA.tree1.delete(i)
        for row in henryDB.book_availability:
            henrySBA.tree1.insert("", "end", values=[row.branch_name, row.on_hand])    
        
class HenrySBC():
    def __init__(self):
        #################################
        # Kicks off the whole tab thing #
        #################################
        self.SBCtab = ttk.Frame(tabControl)
        tabControl.add(self.SBCtab, text = "Search by Category")
        
        #################################
        # Build list for category names #
        #################################
        self.categories = []
        for x in henryDB.categories:
            self.categories.append(x)
            
        ##############################
        # Build list for book titles # 
        ##############################
        self.book_titles = []
        for x in henryDB.books:
            self.book_titles.append(x.title)
            
        ############################
        # Creates tree view object #
        ############################
        self.tree1 = ttk.Treeview(self.SBCtab, columns=('Branch Name', 'Copies Avialable'), show='headings')
        self.tree1.heading('Branch Name', text='Branch Name')
        self.tree1.heading('Copies Avialable', text='Copies Avialable')
        self.tree1.grid(column=1, row=1)
        
        # Label for price
        self.price = ttk.Label(self.SBCtab)
        self.price.grid(column=3, row=1)
        self.price['text'] = "Select a category, then a book"
        
        # Label for Author Selection
        self.author_select = ttk.Label(self.SBCtab)
        self.author_select.grid(column=1, row=2)
        self.author_select['text'] = "Category Selection:"
        
        # Label for Author Selection
        self.book_select = ttk.Label(self.SBCtab)
        self.book_select.grid(column=2, row=2)
        self.book_select['text'] = "Book Selection:"
        
        ##############
        # Comboboxes #
        ##############
        
        # Combobox for Category
        self.authorbox = ttk.Combobox(self.SBCtab, width = 20, state="normal")
        self.authorbox.grid(column=1, row=3)
        self.authorbox['values'] = self.categories
        self.authorbox.current(0)
        self.authorbox.bind("<<ComboboxSelected>>", HenrySBC.chose_category)

        # Combobox for Book
        self.bookbox = ttk.Combobox(self.SBCtab, width = 20, state="disabled")
        self.bookbox.grid(column=2, row=3)
        self.bookbox['values'] = self.book_titles
        self.bookbox.current(0)
        self.bookbox.bind("<<ComboboxSelected>>", HenrySBC.chose_book)
    
    #############################################################################
    # chose_category(event): event handling for author selection combobox         #
    #                      updates book selection combo box with author's books #
    #############################################################################
    def chose_category(event):
        selIndex = event.widget.current()
        henryDB.categorySearch(henrySBC.categories[selIndex])
        
        #################################################################################
        # Build list for author's book titles; indexed for easy reference by chose_book #
        #################################################################################
        henrySBC.category_book_titles = []
        henrySBC.category_book_codes = []
        henrySBC.category_book_prices = []
        for x in henryDB.books_in_category:
            henrySBC.category_book_titles.append(x.title)
            henrySBC.category_book_codes.append(x.book_code)
            henrySBC.category_book_prices.append(x.price)
        henrySBC.bookbox['state'] = tk.NORMAL
        henrySBC.bookbox['values'] = henrySBC.category_book_titles

    def chose_book(event):
        selIndex = event.widget.current()
        henrySBC.price['text'] = ("Price: %s" %(henrySBC.category_book_prices[selIndex]))
        henryDB.getBookAvailability(str(henrySBC.category_book_codes[selIndex]))
        
        for i in henrySBC.tree1.get_children():  # Remove any old values in tree list
            henrySBC.tree1.delete(i)
        for row in henryDB.book_availability:
            henrySBC.tree1.insert("", "end", values=[row.branch_name, row.on_hand])  
        
        
class HenrySBP():
    def __init__(self):
        #################################
        # Kicks off the whole tab thing #
        #################################
        self.SBPtab = ttk.Frame(tabControl)
        tabControl.add(self.SBPtab, text = "Search by Publisher")


        self.publisher_names = []
        for x in henryDB.publishers:
            self.publisher_names.append(x.publisher_name)
        
        ##############################
        # Build list for book titles #
        ##############################
        self.book_titles = []
        for x in henryDB.books:
            self.book_titles.append(x.title)
    
        ############################
        # Creates tree view object #
        ############################
        self.tree1 = ttk.Treeview(self.SBPtab, columns=('Branch Name', 'Copies Avialable'), show='headings')
        self.tree1.heading('Branch Name', text='Branch Name')
        self.tree1.heading('Copies Avialable', text='Copies Avialable')
        self.tree1.grid(column=1, row=1)
        
        
        ##########
        # Labels #
        ##########
        
        # Label for price
        self.price = ttk.Label(self.SBPtab)
        self.price.grid(column=3, row=1)
        self.price['text'] = "Select a publisher, then a book"
        
        # Label for Author Selection
        self.author_select = ttk.Label(self.SBPtab)
        self.author_select.grid(column=1, row=2)
        self.author_select['text'] = "Publisher Selection:"
        
        # Label for Author Selection
        self.book_select = ttk.Label(self.SBPtab)
        self.book_select.grid(column=2, row=2)
        self.book_select['text'] = "Book Selection:"
        
        ##############
        # Comboboxes #
        ##############
        
        # Combobox for Author
        self.authorbox = ttk.Combobox(self.SBPtab, width = 20, state="normal")
        self.authorbox.grid(column=1, row=3)
        self.authorbox['values'] = self.publisher_names
        #self.authorbox.current(0)
        self.authorbox.bind("<<ComboboxSelected>>", HenrySBP.chose_publisher)

        # Combobox for Book
        self.bookbox = ttk.Combobox(self.SBPtab, width = 20, state="disabled")
        self.bookbox.grid(column=2, row=3)
        self.bookbox['values'] = self.book_titles
        self.bookbox.current(0)
        self.bookbox.bind("<<ComboboxSelected>>", HenrySBP.chose_book)
        
        
        
        
        
    def chose_publisher(event):
        selIndex = event.widget.current()
        henryDB.publisherSearch(henryDB.publishers[selIndex].publisher_code)
        #################################################################################
        # Build list for author's book titles; indexed for easy reference by chose_book #
        #################################################################################
        henrySBP.publisher_book_titles = [] 
        henrySBP.publisher_book_codes = []
        henrySBP.publisher_book_prices = []
        for x in henryDB.publisher_books:
            henrySBP.publisher_book_titles.append(x.title)
            henrySBP.publisher_book_codes.append(x.book_code)
            henrySBP.publisher_book_prices.append(x.price)
        henrySBP.bookbox['state'] = tk.NORMAL
        henrySBP.bookbox['values'] = henrySBP.publisher_book_titles
        
        
        
    def chose_book(event):
        selIndex = event.widget.current()
        henrySBP.price['text'] = ("Price: %s" %(henrySBP.publisher_book_prices[selIndex]))
        henryDB.getBookAvailability(str(henrySBP.publisher_book_codes[selIndex]))
    
        for i in henrySBP.tree1.get_children():  # Remove any old values in tree list
            henrySBP.tree1.delete(i)
        for row in henryDB.book_availability:
            henrySBP.tree1.insert("", "end", values=[row.branch_name, row.on_hand])
            
# Main window
root = tk.Tk()
root.title("Henry Bookstore") 
root.geometry('800x400')

# Tab control
tabControl = ttk.Notebook(root)
tabControl.pack(expand = 1, fill ="both")
henryDB = HenryDAO() # Initializes DAO for the data harvest
henryDB.getAuthorData() # Gets all that good, good author data
henryDB.getCategoryData() # Tells henryDAO to check out some categories
henryDB.getPublisherData() # Snoops around the publishers
henryDB.getBookData() # Reads some books

# Breathes life into these GUI tabs
henrySBA = HenrySBA()
henrySBC = HenrySBC()
henrySBP = HenrySBP()



