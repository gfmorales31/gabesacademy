
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/fall2016/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L14-1 Classes and Objects
# 
# Learner objectives for this lesson
# * Define classes
# * Declare objects to instantiate classes
# * Implement basic object functionality
# * Implement class methods

# ## Objects We Have Used
# We have already been exposed to the notion of an *object*. For example, when we open a file for reading or writing, the `open()` function returns a *file object*. 

# In[1]:

# infile is a file object
infile = open("transactions.txt", "r")
print(infile.readlines())
infile.close()


# `infile` is a file object that has associated functions, called *methods*. We have already seen this notion of *methods* when we learned about string and list methods (think `my_string.upper()`, etc.). In the above example, `readlines()` and `close()` are methods belonging to file objects.
# 
# An *object* is a powerful programming concept that couples data storage (i.e. variables) with associated data operations and functionality (i.e. methods).

# ## Classes
# We know of several Python data types:
# * `int`
# * `float`
# * `string`
# * `file`
# * etc.
# 
# Today, we are going to learn how to define our own types! To do so, we will define *classes*. A class is a collection of *attributes* and *behaviors* that completely describes something. More on *attributes* and *behaviors* to come.
# 
# Programmatically, a class is a type definition, and an object is a variable of that type. We also say an object is an *instance* of a class.
# 
# Imagine we are writing a program to manage the status of books at a library or bookstore. For this program, it would be useful to have a class called `Book` where we could store information (think variables, called *attributes* when the variables belong to objects) and operations (think functions, called *methods* when the functions belong to objects) related to a book. Using the reserved keyword `class` to define a `Book` class, we can define this type:

# In[2]:

class Book:
    '''
    
    '''


# We have a definition for a `Book`! This class is not very powerful (yet). Let's see how we can make an instance of this class, called an object:

# In[3]:

# my_book is a Book object, i.e. it is an instance of the Book class
my_book = Book()


# Now that we have a book class, let's add variables to the class to represent information about books, such as `title` (string), `author` (string), `isbn` (string), and `checked_out` (Boolean). We call variables associated with an object *attributes* to specify they are variables belonging to a class. We can declare and access the attributes of an object with the *member selection* (dot) operator:

# In[4]:

my_book = Book()
my_book.title = "The Martian"
my_book.author = "Andy Weir"
my_book.isbn = "978-0-8041-3902-1"
my_book.checked_out = False # it's on the shelf


# We have actually seen and used the dot notation to access variables and functions before. Recall accessing pi in the math module (`math.pi`), calling a library function (`math.sqrt(4.0)`), and calling a method of a file object (`in_file.close()`) or a string object (`my_string.upper()`). 
# 
# We can display the attribute values just like other variables:

# In[5]:

if my_book.checked_out:
    print("The book \"%s\" is checked out" %(my_book.title))
else: # checked in
    print("The book \"%s\" is available on the shelf" %(my_book.title))


# Objects are mutable! We can change the status of a `Book` object should someone check in or check out a book from the library:

# In[8]:

my_book.checked_out = True


# Now, let's modify an attribute 2 different ways:
# 1. Via a function
# 1. Via a method
# 

# ## Objects and Functions

# Remember when we learned about aliasing? We can pass a reference to an object into a function to create an alias. For example, supposed we have a `Book` object called `hp1`. We can make an alias called `book` for `hp1` if we pass in `hp1` into a function with a parameter called `book`:

# In[6]:

def display_book(book):
    '''
    
    '''
    print("%s by %s" %(book.title, book.author))

def display_book_status(book):
    '''
    
    '''
    print("%s is checked out: %s" %(book.title, book.checked_out))
    
    
def return_book(book):
    '''
    
    '''
    book.checked_out = False
    
hp1 = Book()
hp1.title = "The Sorcerer's Stone"
hp1.author = "J.K. Rowling"
hp1.isbn = "978-0439708180"
hp1.checked_out = True

display_book(hp1)
display_book_status(hp1)
return_book(hp1)
display_book_status(hp1)


# ## Objects and Methods
# If we place a function *inside* a class definition, the function is a *method* associated with an instance of the class.

# In[6]:

class Book:
    '''
    
    '''
    # simply indent the method definition to associate it with the class
    # self is a reference to the calling object
    def display_book(self):
        '''

        '''
        print("%s by %s" %(self.title, self.author))
    
    def display_book_status(self):
        '''

        '''
        print("%s is checked out: %s" %(self.title, self.checked_out))
    
    def return_book(self):
        '''

        '''
        self.checked_out = False


# We do have to change one aspect of our function definitions to do this. When we call a method of a class, we do so in the form: `<object>.<method>()`. The method needs a reference to the object in order to access that particular instance's attributes. In Python, the `self` reference provides access to the *current* object. `self` is the first parameter of every method of every class, and it is *implicitly* passed into the method. This means, Python passes it in for us, we do not explicitly pass the object reference in as an argument of the method.
# 
# Now, if we have a `Book` object (instance of the `Book` class), we can use the member selection operator to call the `display_book_status()` and `return_book()` methods associated with `Book`s:

# In[7]:

hp1 = Book()
hp1.title = "The Sorcerer's Stone"
hp1.author = "J.K. Rowling"
hp1.isbn = "978-0439708180"
hp1.checked_out = True

hp1.display_book()
hp1.display_book_status()
hp1.return_book()
hp1.display_book_status()


# ## Special Methods

# ### The `__str__()` Method
# The `__str__()` special method is called implicitly when a string representation of the object is required, such as `print(hp1)`. We have already written a method with similar functionality, `display_book()`. We just need to change the method identifier to `__str__()` and return the string instead of print the string, and we can achieve the `print(hp1)` functionality!

# In[5]:

class Book:
    '''
    
    '''       
    def __str__(self):
        '''
        
        '''
        return "%s by %s" %(self.title, self.author)
        
hp1 = Book()
hp1.title = "The Sorcerer's Stone"
hp1.author = "J.K. Rowling"
hp1.isbn = "978-0439708180"
hp1.checked_out = True
print(hp1)


# Note: We can also explicitly call special methods: `hp1.__str__()`

# ### The `__init__()` Method
# There is a special method identifier, `__init__()` (short for initialize) that is implicitly called by Python everytime you instantiate a new object. The double underscores denote that this method *special* in Python. We can write our own version of the `__init__()` method to specify attribute values at time of instantiation. Here is an example of the `__init__()` method for our `Book` class.

# In[11]:

class Book:
    '''
    
    '''
    def __init__(self, book_title, book_author, book_isbn, book_checked_out):
        self.title = book_title
        self.author = book_author
        self.isbn = book_isbn
        self.checked_out = book_checked_out
        


# And now we will instantiate a Harry Potter `Book` object:

# In[12]:

hp1 = Book("The Sorcerer's Stone", "J.K. Rowling", "978-0439708180", False)


# On this instantiation, the `__init__()` method we wrote is implicitly called and the attributes `title`, `author`, `isbn`, and `checked_out` are declared and initialized to the values we passed in as arguments.

# ## Lists of Objects
# Let's put together some of the topics we have learned so far to declare a bookshelf of `Books`. This will be a list of `Book` objects. We can declare this list just like any other list, and populate it with `Book` objects:`

# In[4]:

book_shelf = []

hp1 = Book("The Sorcerer's Stone", "J.K. Rowling", "978-0439708180", True)
book_shelf.append(hp1)

hp2 = Book("The Chamber of Secrets", "J.K. Rowling", "978-0439708180", False)
book_shelf.append(hp2)

hp3 = Book("The Prisoner of Azkaban", "J.K. Rowling", "978-0439708180", True)
book_shelf.append(hp3)

hp4 = Book("The Goblet of Fire", "J.K. Rowling", "978-0439708180", True)
book_shelf.append(hp4)

hp5 = Book("The Order of the Phoenix", "J.K. Rowling", "978-0439708180", False)
book_shelf.append(hp5)

hp6 = Book("The Half Blood Prince", "J.K. Rowling", "978-0439708180", False)
book_shelf.append(hp6)

hp7 = Book("The Deathly Hallows", "J.K. Rowling", "978-0439708180", True)
book_shelf.append(hp7)

for book in book_shelf:
    print(book)


# ## TODO
# 1. Read chapters 15, 16, and 17.
# 1. PA7 is due tonight.
# 1. Take a look at PA8.
# 
# ## Next Lesson
# 1. More on classes.
