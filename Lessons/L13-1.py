
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/fall2016/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L13-1 Advanced Lists and Tuples
# 
# Learner objectives for this lesson
# * Apply list methods
# * Delete items from a list
# * Learn about aliasing
# * Passing lists into functions as arguments
# * Returning lists from functions

# ## List Methods
# Just like with strings, lists are objects that have methods we can utilize. 
# 
# ### `append()`
# For example, since lists are mutable, there is an `append(<new item>)` method to add an item to the end of a list:

# In[1]:

cities = ["Pullman", "Spokane"]
print(cities)

# adds the string as an item
cities.append("Seattle")
print(cities)

# adds the list as an item
cities.append(["Moscow"])
print(cities)


# As review, how could we achieve the same functionality as `append()` without using `append()`?

# In[2]:

cities = ["Pullman", "Spokane"]
print(cities)

# adds the strings as an item
cities += ["Seattle"]
print(cities)


# ### `extend()`
# `extend()` is similar to `append()`; however, `extend()` takes a list as an argument and adds each item to the list:

# In[3]:

cities = ["Pullman", "Spokane"]
print(cities)

# adds each string in the list as an item
cities.extend(["Seattle", "Couer d'Alene"])
print(cities)


# What would happen if we used `append()` instead of `extend()` in the above code?

# In[4]:

cities = ["Pullman", "Spokane"]
print(cities)
cities.append(["Seattle", "Couer d'Alene"])
print(cities)


# `cities` becomes a nested list!

# ### `sort()`
# Many applications require lists of items to be sorted. In CptS121, you will learn how to write your own sorting algorithms. For now, we will use the `sort()` list method:

# In[6]:

cities = ["Pullman", "Spokane", "Seattle", "Couer d'Alene"]
print(cities)

# ascending order
cities.sort()
print(cities)


# How would you sort a list in descending order? Try using `help(cities.sort)` to find out:

# In[7]:

help(cities.sort)


# In[8]:

print(cities)
cities.sort(reverse=True)
print(cities)


# ## Deleting Items in a List
# Since lists are mutable, we can delete items in a list. 
# 
# ### Single Item Deletes
# We have two list methods to delete a *single* item in a list
# 1. When you know the *index* of the item to delete
#     * `pop(<index>)`
# 1. When you know the *value* of the item to delete
#     * `remove(<item>)`

# In[9]:

cities = ["Pullman", "Spokane", "Seattle", "Couer d'Alene"]

# pop returns the item removed
city = cities.pop(2)
print(city)
print(cities)

# remove does not return the item removed
cities.remove("Spokane")
print(cities)


# ### `del` Keyword and Multiple Item Deletes
# Alternatively, we can delete an object using the `del` reserved keyword:

# In[10]:

cities = ["Pullman", "Spokane", "Seattle", "Couer d'Alene"]
print(cities)

# del is not a function
del cities[1]
print(cities)


# We may want to delete multiple items at a time. We can do this with a slice and `del`:

# In[11]:

cities = ["Pullman", "Spokane", "Seattle", "Couer d'Alene"]
print(cities)

del cities[0:3]
print(cities)


# ### Relationship Between Strings and Lists
# A list of single character strings is not a string:

# In[12]:

my_list = ["c", "p", "t", "s", "1", "1", "1"]
print("%s" %(my_list))


# ### `join()` (string method)
# However, we can turn a list of strings into a string with the `join()` string method. We need to specify a "delimiter" string to use to concatenate the individual strings in a list into a single string:

# In[18]:

my_list = ["c", "p", "t", "s", "1", "1", "1"]
delimiter = '' # empty string
my_string = delimiter.join(my_list)
print("%s" %(my_string))

delimiter = ':)'
my_string = delimiter.join(my_list)
print("%s" %(my_string))


# ### `list()` (function)
# To convert the string back into a list, we can type cast the string into a list with `list()`:

# In[19]:

my_string = "cpts111"
my_list = list(my_string)
print(my_list)


# ### `split()` (string method)
# `split(<string delimiter>)` breaks a string into pieces at each `<string delimiter>`. The pieces are returned as a list: 

# In[20]:

sentence = "hello how are you"
pieces = sentence.split(" ")
print(pieces)


# ## Aliasing
# When we declare a list variable, as in `list1 = [0, 1, 2, 3]`, a list *object* is created. We say the variable `list1` is a *reference* to the list object `[0, 1, 2, 3]`. In memory, this looks like the following:
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/reference_example.png)
# 
# If we declare another list variable, `list2 = [0, 1, 2, 3]`, `list2` refers to a *different* list object, even though both objects that `list1` and `list2` refer to contain the same items:
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/references_multiple_example.png)
# 
# We can test if `list1` and `list2` refer to lists that contain the same elements:

# In[21]:

list1 = [0, 1, 2, 3]
list2 = [0, 1, 2, 3]
print(list1 == list2)


# To test if `list1` and `list2` *refer* to the same list object, we can use the Python reserved keyword, `is`. `is` tests whether two variables refer to the same object: 

# In[22]:

list1 = [0, 1, 2, 3]
list2 = [0, 1, 2, 3]
print(list1 is list2)


# Note: Python is intelligent! Since strings are immutable, only one object is created in the following code:

# In[23]:

string1 = "cpts111"
string2 = "cpts111"
print(string1 == string2)
print(string1 is string2)


# In the above code, both `string1` and `string2` refer to the same string object. This phenomenon is called *aliasing*. 
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/alias_string_example.png)
# 
# Let's return to our list example and see aliasing at work. 
# 
# If instead of assigning `list2` to a new list object, we assign `list2` to `list1`: `list2 = list1`, `list2` refers to the same object as `list1`.
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/alias_example.png)
# 
# We now say the object is *aliased*, because it has more than one reference, or alias.
# 
# If the aliased object is mutable, either reference can modify the object:

# In[24]:

# same object aliased by list1 and list2
list1 = [0, 1, 2, 3]
list2 = list1
print(list1)
print(list2)
list2[2] = 100
print(list1)
print(list2)
print("\n")

# compared to creating two separate objects list1 and list2
list1 = [0, 1, 2, 3]
list2 = [0, 1, 2, 3]
print(list1)
print(list2)
list2[2] = 100
print(list1)
print(list2)


# Aliasing is important to keep in mind, especially when passing lists as arguments.

# ## Lists Arguments
# We can pass lists into functions as arguments:

# In[25]:

def pretty_print_list(list_to_print):
    '''
    
    '''
    for value in list_to_print:
        print(value, end=" ")

numbers = [0.0, 0.2, 0.4]
pretty_print_list(numbers)


# When a list is passed as an argument to a function, the function parameter variable is a *reference* to the list, making the list *aliased*. This means that if we modify a list in our function, the change to the object persists and the calling code will see the change.
# 
# In the example above, `numbers` and `list_to_print` are aliases to the list object `[0.0, 0.2, 0.4]`. If `pretty_print_list()` can use `list_to_print` to modify the object. 
# 
# Let's write a new function, `add_one()`, that adds one to each value in a list:

# In[26]:

def add_one(list_arg):
    '''
    
    '''
    for i in range(len(list_arg)):
        list_arg[i] += 1

numbers = [0.0, 0.2, 0.4]
print(numbers)
add_one(numbers)
print(numbers)


# ## Returning Lists
# We can write functions that return lists. Consider a function that returns a list of numbers from arguments `start_index` to `end_index + 1`:

# In[27]:

def create_sequence(start_index, end_index):
    '''
    
    '''
    sequence = []
    
    for i in range(start_index, end_index):
        sequence.append(i)
    return sequence

first_ten_nums = create_sequence(0, 10)
print(first_ten_nums)


# ## Tuples
# Tuples are immutable lists. They are declared as a comma separated list, with or without parentheses:

# In[28]:

my_tuple = "x", "y", "z"
print(my_tuple)
print(type(my_tuple))

# need a comma after a single element initialization
my_tuple2 = (1, )
print(my_tuple2)

# need a comma after a single element initialization
not_a_tuple = ("a")
print(not_a_tuple)
print(type(not_a_tuple))

# creating an empty tuple
empty_tuple = tuple()
print(empty_tuple)
print(type(empty_tuple))


# Tuple indexing and slicing works the same as for lists:

# In[29]:

my_tuple = ("x", "y", "z")
print(my_tuple[1])
print(my_tuple[0:2])


# HOWEVER, tuples are immutable, so you cannot modify them. The follow code demonstrates the immutability of tuples:

# In[30]:

my_tuple = ("x", "y", "z")
# crashes! tuples are immutable, you cannot change them
my_tuple[2] = "a"


# ## TODO
# 1. Work on PA6.
# 1. Read Chapters 10, 11, and 12.
# 
# ## Next Lesson
# We cover dictionaries, a quite powerful data structure!
