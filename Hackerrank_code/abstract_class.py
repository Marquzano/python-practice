from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    """Provides a template class for book classes."""

    def __init__(self, title, author):
        """Initializes the basic attributes of a book."""
        self.title=title
        self.author=author

    @abstractmethod
    def display(): 
        """An abstract method to display the books."""
        pass

# write MyBook class
class MyBook(Book):
    """A model of my books."""

    def __init__(self, title, author, price):
        """Initializes the attributes for my books."""
        super().__init__(title, author)
        self.price = price
    
    def display(self):
        """Displays the attributes of my books."""
        print("Title: " + self.title.title())
        print("Author: " + self.author.title())
        print("Price: " + str(self.price))


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()