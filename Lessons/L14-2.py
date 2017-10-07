
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/fall2016/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L14-2 Object Oriented Programming
# 
# Learner objectives for this lesson
# * Practice defining classes and implementing object oriented programming (OOP) concepts
# * Learn about operator overloading
# * Learn about composition

# ## Practice Problem
# ### Part 1
# Define a class called `Point`. A `Point` represents a position in 2 dimensional space, defined by an x and a y coordinate (no need to define any methods *yet*). 
# 
# Instantiate a `Point` object representing the origin (0,0):

# In[ ]:

class Point:
    '''
    
    '''

origin = Point()
origin.x = 0
origin.y = 0


# ### Part 2
# Re-write your `Point` definition and instantiation of `Point` to make use of an `__init__()` method:

# In[ ]:

class Point:
    '''
    
    '''
    def __init__(self, x, y):
        '''
        
        '''
        self.x = x
        self.y = y
    
point = Point(1, 4)


# ### Part 3
# Add a method to `Point` called `display_point()` that displays `Point` information in the form: `(x, y)`. Then call `display_point()` to print a `Point` object.

# In[ ]:

class Point:
    '''
    
    '''
    def __init__(self, x, y):
        '''
        
        '''
        self.x = x
        self.y = y
        
    def display_point(self):
        '''
        
        '''
        print("(%d,%d)" %(self.x, self.y), end="")
    
point = Point(1, 4)
point.display_point()


# ### Part 4
# Modify `display_point()` to implement the special function `__str__()`. Then print a `Point` object.

# In[2]:

class Point:
    '''
    
    '''
    def __init__(self, x, y):
        '''
        
        '''
        self.x = x
        self.y = y
        
    def __str__(self):
        '''
        
        '''
        return "(%d, %d)" %(self.x, self.y)
    
point = Point(1, 4)
print(point)


# ### Part 5
# Add a predicate method to `Point` called `equals()` that accepts another `Point` object and determines if it has the same `x` and `y` values as the calling object (think `self`). Then call `equals()` to determine if 2 `Point` objects store equivalent data.

# In[2]:

class Point:
    '''
    
    '''
    def __init__(self, x, y):
        '''
        
        '''
        self.x = x
        self.y = y
        
    def display_point(self):
        '''
        
        '''
        print("(%d,%d)" %(self.x, self.y), end="")
        
    def equals(self, other_point):
        '''
        
        '''
        if self.x == other_point.x and self.y == other_point.y:
            return True
        return False
    
origin = Point(0, 0)

some_other_point = Point(0, 0)

origin.display_point()
print(" is equal to ", end="")
some_other_point.display_point()
print(": %s" %(origin.equals(some_other_point)))


# ## Object Oriented Programming
# Object oriented programming (OOP) involves designing programs where most of the computation involves operations on objects. Classes are implemented to represent things in the real world and how they interact. While OOP is a vast subject (and sometimes more of an art than a science), we are going to just scratch the surface on how powerful OOP iswith the following concepts:
# * Operator overloading
# * Composition
# 
# Other OOP concepts include:
# 
# * Abstraction
# * Encapsulation
# * Inheritance
# * Polymorphism
# * Among others!
# 
# You can read more about OOP concepts in Chapter 18 of the Downey textbook, as well as online and in other textbooks.

# ### Operator Overloading
# What about changing the syntax to compare two `Point` objects for equality from `point1.equals(point2)` to `point1 == point2`? We can achieve such behavior with special methods for defining operator functionality. This is called *operator overloading*. In the equality example, we are going to define the behavior for comparing two `Point` objects with the `==` operator.

# #### The `__eq__()` Method
# All we have to do is modify our `equals()` method to implement the special method `__eq__()`:

# In[1]:

class Point:
    '''
    
    '''
    def __init__(self, x, y):
        '''
        
        '''
        self.x = x
        self.y = y
        
    def __str__(self):
        '''
        
        '''
        return "(%d,%d)" %(self.x, self.y)
        
    def __eq__(self, other_point):
        '''
        
        '''
        if self.x == other_point.x and self.y == other_point.y:
            return True
        return False
    
point1 = Point(1, 4)
point2 = Point(3, -2)
point3 = Point(3, -2)

# different x,y values
print(point1 == point2)
# same x,y values
print(point2 == point3)
# confirm they are different objects 
print(point2 is point3)


# #### Other Operators to Overload
# Try implementing the functionality for other operators:
# * `+`: `__add__()`
# * `-`: `__sub__()`
# * `<`: `__lt__()`
# * `>`: `__gt__()`
# * Read about more in the [Python documentation](https://docs.python.org/3/reference/datamodel.html#specialnames)

# ### Composition
# Objects can have attributes that are other objects. Let's define a `Circle` class that has 2 attributes:
# 1. `center`: a `Point` object representing the location of the center of a circle
# 1. `radius`: a numeric value representing the radius of the circle

# In[4]:

class Circle:
    '''
    
    '''
    def __init__(self, x, y, radius):
        '''
        
        '''
        center = Point(x, y)
        self.center = center
        self.radius = radius
        
    def __str__(self):
        '''
        
        '''
        return "Circle with center: %s and radius %.2f" %(self.center, self.radius)
    
circle = Circle(0, 5, 100.0)
print(circle)


# Note: We can think of the relationship between a `Circle` and a `Point` as: "a `Circle` **has a** `Point`". The "has a" relationship is important to distinguish from the "is a" relationship of inheritance... You will learn about inheritance when you take CptS 122! :)

# ## TODO
# 1. Work on PA8
# 1. Start studying for the final!
# 
# ## Next Lesson
# 1. Converting to/from binary and decimal
# 1. Review for the final
