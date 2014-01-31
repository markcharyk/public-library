#!/usr/local/bin/python2.7
#Author: Mark Charyk
#Version 1.0

class Book(object):
    """A class that makes books for Shelving in a Library"""
    def __init__(self, title, author, genre, lib):
        self.title = title
        self.author = author
        self.genre = genre
        self.lib = lib
        lib.unshelved_books.append(self)
    
    def print_out(self):
        print "%s by %s" % (self.title, self.author)
    
    def enshelf(self):
        """Put the Book on a Shelf"""
        for i in lib.shelves:
            """Find the appropriate shelf"""
            if self.genre == i.section:
                i.add_book(self)
                lib.unshelved_books.remove(self)
                return
        """If there is no shelf, create a new one"""
        self.lib.make_shelf(self.genre)
        self.enshelf()
    
    def unshelf(self):
        """Take the Book off a Shelf"""
        for i in lib.shelves:
            if self.genre == i.section:
                i.delete_book(self)
                lib.unshelved_books.append(self)
    
class Shelf(object):
    """A class that makes shelves for holding Books in a Library"""
  
    def __init__(self, section):
        self.section = section
        self.books = []
    
    def add_book(self, bk):
        self.books.append(bk)
		
    def delete_book(self, bk):
        self.books.remove(bk)
  
    def print_out(self):
        if not self.books:
            """Don't print anything if the shelf is empty"""
            return
        print "On the %s shelf: " % (self.section)
        for bk in self.books:
            bk.print_out()
      
class Library(object):
    """A class that makes a library for housing Shelves of Books"""
    
    def __init__(self):
        self.shelves = [Shelf("Fiction"), Shelf("Non-Fiction"), Shelf("Reference"), Shelf("YA")]
        self.unshelved_books = []
      
    def make_shelf(self, section):
        self.shelves.append(Shelf(section))
    
    def print_out(self):
        for sh in self.shelves:
            sh.print_out()
        if not self.unshelved_books:
            """Don't print anything if the list is empty"""
            print "--------"
            return
        print "Currently unshelved: "
        for bk in self.unshelved_books:
            bk.print_out()
        print "--------"
        
lib = Library()
bk = Book("Moby Dick", "Herman Melville", "Fiction", lib)
bk2 = Book("Divergent", "Veronica Roth", "YA", lib)
bk3 = Book("Fangirl", "Rainbow Rowell", "YA", lib)
bk4 = Book("Where The Wild Things Are", "Maurice Sendak", "Childrens", lib)
lib.print_out()
bk.enshelf()
bk2.enshelf()
bk3.enshelf()
bk4.enshelf()
lib.print_out()
bk5 = Book("The Very Hungry Caterpillar", "Eric Carle", "Childrens", lib)
bk2.unshelf()
bk5.enshelf()
lib.print_out()
