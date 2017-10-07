
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/fall2016/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L15-1 Final Exam Review

# ## What to Bring?
# * Two sharp pencils
# * Python Programming knowledge in your head :)
# * A "cheat sheet" (see below)  
# 
# ## What NOT to Bring?
# * Electronics (including calculators) may not be used during the exam!
# * Notes may not be used during the exam!
# 
# Note: If you are caught cheating, your exam will be confiscated and you will receive a 0.
# 
# Note: Use the restroom before class. **Once testing starts, the only reason for leaving the classroom is turning in your exam as done.**
# 
# ## The "Cheat Sheet"
# The exam will be closed-book, but you will be allowed a **handwritten** "cheat sheet": one side of a page whose dimensions may not exceed 8-1/2" by 5-1/2" (i.e. **one-half of a standard sheet of notebook paper**). You must present your cheat sheet to myself or a TA so it can be verified that it meets regulations. 
# 
# If you bring/use a cheat sheet that: 
# 1. Exceeds the allowable dimensions
# 1. Has writing on both sides of the page
# 1. Contains non-handwritten text (i.e. printed)
# 
# You run the risk of its being confiscated prior to the exam. This policy will be strictly enforced.
# 
# If you choose to use a cheat sheet, you will be required to turn in your cheat sheet with your exam.
# 
# ## Exam Timeframe
# You will have 2 hours (120 minutes) to take the exam. Time will be extremely tight for the exam so manage your time well. If you show up late to class, you will have less time to take the exam. 
# 
# Note: **NO EARLY EXAMINATIONS**, as per [university policy](https://registrar.wsu.edu/media/753372/Fall%202016%20Final%20Exam.pdf). Final Examinations will not be rescheduled for the purpose of leaving the institution before the close of the semester (per academic rule 79). This means you are to take your CptS 111 final exam during your scheduled time block:
# 
# * *Section 01 (2:10pm lecture)*: Friday, December 16th; 8:00 – 10:00am
# * *Section 02 (3:10pm lecture)*: Wednesday, December 14th; 3:10 – 5:10pm

# ## Exam Coverage
# The exam covers everything we have covered in the course. Here is an outline of the topics we have covered so far:
# 
# ### Exam #1 Topics
# [Exam #1 review topics](http://nbviewer.jupyter.org/github/gsprint23/cpts111/blob/master/lessons/L7-1.ipynb)
# 
# 
# ### Exam #2 Topics
# [Exam #2 review topics](http://nbviewer.jupyter.org/github/gsprint23/cpts111/blob/master/lessons/L11-2.ipynb)
# 
# 
# ### 1 Lists
# (Chapter 10 *Lists* in the Downey textbook.)
# * Describe what is a list
#     * A sequence of times with one variable name
#     * A list is considered a data structure
#         * A data structure is a way of storing and organizing information; a composite of related data items
#     * Lists can have items of different types
#     * Lists are mutable
# * Declare and apply single and 2-dimensional lists (nested lists)
#     * Use [ ] (hard brackets) to declare lists
#     * `list()`
# * Define what is an index
#     * Recall list indexing in C starts at 0
# * Lists and loops
#     * Use a loop to initialize each item in a list
#     * Use loops to traverse through lists
# * Write functions which accept lists (single and 2-dimensional) as parameters
# * What happens when a list is passed to a function?
#     * The list reference is copied and passed into the function
#     * Via the reference, the function can modify the list
# * Return lists from functions
# * How to get the number of items in a list?
# * Understand and apply list operators (e.g. concatenation, repetition, slice, etc.)
# * Understand and apply list methods (e.g. `append()`, `extend()`, etc.)
# * Understand and apply string methods that return lists (e.g. `join()`, `split()`, etc.)
# * Remove items in a list
# * Describe what is aliasing
#     * When two or more references refer to the same object
#     * Difference between how Python creates objects for mutable types (e.g. lists) and immutable types (e.g. strings)

# ### 2 Tuples
# (Chapter 12 *Tuples* in the Downey textbook.)
# * Describe what is a tuple
#     * An immutable list
# * Declare and apply single and 2-dimensional tuples (nested tuples)
#     * Use () and , (parentheses and/or commas) to declare tuples
#     * `tuple()`
# * How to get the number of items in a tuple?
# * Tuple indexing
# * Tuple slicing

# ### 3 Dictionaries
# (Chapter 11 *Dictionaries* and Chapter 13 *Case Study: Data Structure Selection* in the Downey textbook.)
# * Describe what are keys
# * Describe what are values
# * Describe what is a mapping
# * Describe what are key-value pairs
# * Describe what is a dictionary
#     * A list with keys as indices
#     * Dictionaries are mutable
#     * Valid data types for keys and values
# * Declare and apply single and 2-dimensional dictionaries (nested dictionaries)
#     * Use { } (curly brackets) to declare dictionaries
#     * `dict()`
# * Convert tuples to dictionaries and dictionaries to tuples
# * Dictionary indexing
# * Dictionaries and loops
# * Adding key-value pairs
# * Testing existence of a key
# * How to get the number of key-value pairs in a dictionary?
# * Understand and apply dictionary methods (e.g. `items()`, etc.)

# ### 4 Objects
# (Chapter 15 *Classes and Objects*, Chapter 16 *Classes and functions*, and Chapter 17 *Classes and methods* in the Downey textbook.)
# * Describe what is a class?
#     * A collection of attributes and behaviors that completely describes something
# * Describe what is an object?
#     * An instance of a class
#     * Objects are mutable
# * Describe what is object oriented programming
# * Pre-defined Python classes we have been using
# * Programmer-defined Python classes we write ourselves
# * Defining/instantiating classes
# * Setting/getting attributes
# * Defining/calling methods
# * Describe what is the `self` parameter?
# * Special methods
#     * `__init__()`
#     * `__str__()`
#     * `__eq__()`
#     * others?
# * Objects and functions
# * Lists of objects
# * Describe what is operator overloading
#     * Special methods that define operator functionality
#     * For example, `__eq__()` defines functionality for the equals operator `==`
# * Describe what is composition
#     * Attributes that are other objects

# ### Other Topics
# * 8x8 light board hardware/software
#     * RGB values
# * `time` module
# * Converting decimal to binary
# * Converting binary to decimal

# ## Recommended Strategy for Preparing for the Exam
# The exam questions will require you to solve problems in a variety of formats: defining key terms, evaluating expressions, writing code, determining the output of code, etc.
# 
# I recommend that you use the following activities and materials to prepare for the exam:
# * Review quizzes, lab exercises, programming assignments, and problems solved in class
#     * These may well be your best resource. An excellent learning activity would be to retake the quizzes and re-solve the lab exercises, in class exercises, and programming assignments. 
# * Lesson notes and example code
# * Read the textbook
#     * Read or re-read chapters 1-3, 5 (no recursion), 6-17, and Appendix A and in the Downey textbook. 

# ## Extra Practice Problems

# ### 1
# Define a `Student` class to store information about a student. `Student` information includes an ID number (string), first name (string), last name (string), and number of credits (integer). In your definition, include `__init__()`, `__str__()`, and `__eq__()` special methods. Two `Student`s are compared for equality based on their ID Number.
# 
# Write code to instantiate two `Student` objects, display the `Student`s, and compare the two `Student`s for equality.

# ### 2
# The following problem is motivated by PA5. Write a function called `compute_mins_seconds(ms)` that accepts a duration in milliseconds and returns a tuple of minutes and seconds. For example, `compute_min_seconds(125000)` would return the tuple `(2, 5)` corresponding to 2 minutes and 5 seconds in 125000 milliseconds.

# ### 3
# For the following problems, we will need to download a file: [words.txt](http://thinkpython2.com/code/words.txt). This file contains 113,809 official crossword words, one per line. Using words.txt, write a program with the following functionality:
# 1. `count_words()`: accepts the file object as an argument and returns the number of words in the file.
# 1. `avg_word_length()`: accepts the file object as an argument and returns the average number of characters per word.
# 1. `write_word_lengths()`: accepts the file object as an argument and for each word in words.txt, writes the number of characters in the word to a file (lengths.txt), one number per line.
# 
# You may choose to define/call additional functions if you wish.

# ### 4
# Write a function that accepts a string representing a binary number and returns an integer representing the string in decimal. 
# 
# Test your function with "11001", which is 25 in decimal (check this by hand too, it's good practice!).

# In[34]:

def binary_to_decimal(binary):
    '''
    
    '''
    decimal = 0
    highest_power_two = len(binary) - 1
    
    for i in range(len(binary)):
        digit = int(binary[i])
        decimal += digit * 2 ** (highest_power_two - i)
        
    return decimal

print(binary_to_decimal("11001"))
    


# ### 5
# Write a function that accepts an integer and returns a string representing the integer in binary.
# 
# Test your function with 132, which is "10000100" in binary (check this by hand too, it's good practice!).

# In[35]:

def decimal_to_binary(decimal):
    '''
    
    '''
    binary = ""
    highest_power_two = 7 # hardcoding this to only handle decimals in [0, 2^8 - 1]
    # could compute highest_power_two with log base 2(decimal)
    for i in range(highest_power_two, -1, -1):
        power_two = 2 ** i
        if decimal // power_two > 0:
            binary += "1"
            decimal -= power_two
        else:
            binary += "0"
    
    return binary

print(decimal_to_binary(132))


# ### 6
# Write a program to roll a 6-sided die 1,000 times. Use a dictionary to store the count of each die face to determine the percentage of each outcome. Are the percentages what you would expect them to be?
# 
# Repeat the above problem for rolling two 6-sided dice (i.e. the sum of both dice). Are the percentages what you would expect them to be?

# In[42]:

def roll_dice_1000_times():
    '''
    
    '''
    # for counting single 6 sided die throws
    d = {}
    # for counting the sum of two 6 sided die throws
    d2 = {}
    for i in range(1000):
        roll = random.randrange(1, 7)
        roll2 = random.randrange(1, 7)
        if roll in d:
            d[roll] += 1
        else:
            d[roll] = 1
            
        summ = roll + roll2
        if summ in d2:
            d2[summ] += 1
        else:
            d2[summ] = 1
    for roll in d:
        d[roll] /= 1000
        d[roll] *= 100.0
    for summ in d2:
        d2[summ] /= 1000
        d2[summ] *= 100.0
    return d, d2
    
one_die, two_dice = roll_dice_1000_times()
for face_value in one_die:
    print("%d: %.2f%%" %(face_value, one_die[face_value]))
    
print()
for face_value in two_dice:
    print("%d: %.2f%%" %(face_value, two_dice[face_value]))


# ### 7
# Given the following table of data:
# 
# |ID Number|Last name|First name|
# |-|-|-|
# |28905|Smith|Jane|
# |19485|Smith|John|
# |28450|Smith|John|
# |17834|Smith|Justin|
# 
# Write code to perform the following:
# 1. Populate a dictionary called `students` with the student information in the table. Keys in the dictionary should be ID Numbers and values in the dictionary should be two-item tuples containing first and last names.
# 1. Write a loop to display each key-value pair in `students` in the following form: `28905: Smith, Jane`
# 1. Add another student, 19654 Janet Smithy, to `students`
# 1. Remove ID number 28450 from `students`
# 1. Convert `students` to a list of tuples and print the list

# ### 8
# Define and test the following two functions which operate on 2D lists of integers:
# 1. `reverse_rows(list_ints)`: reverses the items in `list_ints` by rows
# 1. `reverse_cols(list_ints)`: reverse the items in `list_ints` by columns
# 
# For example, if `list_ints =[[1, 2, 3], [4, 5, 6]]`, `reverse_rows(list_ints)` would modify `list_ints` to be `[[3, 2, 1], [6, 5, 4]]` and `reverse_cols(list_ints)` would modify `list_ints` to be `[[4, 5, 6], [1, 2, 3]]`

# ### 9
# For this problem, we are going to define basic classes to represent objects related to `turtle` graphics. For each of the following classes, include `__init__()` and `__str__()` methods:
# 1. Define a `Pen` class to represent a writing/drawing pen. Include attributes to represent pen color and ink width.
# 2. Define a `Coordinate` class to represent a 2D coordinate pair. Include attributes to represent the x and y coordinates.
# 3. Define a `SimpleTurtle` class to represent a simplified version of a turtle in `turtle` graphics. `SimpleTurtle` should include attributes representing the pen (a `Pen`), location (`Coordinate`), the direction of travel (a number), and whether or not the pen is touching the canvas (a Boolean). Add a method to move a `SimpleTurtle` object a certain number of steps. If the pen is down, inform the user of the line drawn.
# 
# Test your `SimpleTurtle` class by instantiating an object and moving it to simulate drawing a square.

# ### 10
# Write a function called `build_jagged2d()` that accepts an integer value greater than 1 as an argument. The function creates a nested list of integers where the first row has one zero, the second row has two zeroes, and so on. The function returns the two dimensional list.
# 
# Example: `build_jagged2d(3)` returns a two dimensional list of three rows, the first row having one zero, the second having two zeros, and the third having three zeroes. Logically, this looks like the following:
# ```
# 0
# 0 0
# 0 0 0
# ```
# Programmatically, this looks like: `[[0], [0, 0], [0, 0, 0]]`

# ### 11
# Write a function called `geometric_sum()` that accepts one positive integer argument, `n`. The function returns the sum of the numbers:
# 
# $$1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + ... + \frac{1}{2^{n - 1}}$$
# 
# For example, `geometric_sum(4)` returns 1.875000

# ## TODO
# 1. Please study for the exam! At a *minimum*:
#     * Work or re-work through:
#         * The above practice problems
#         * Tasks from the review lab: [Lab 14](http://nbviewer.jupyter.org/github/gsprint23/cpts111/blob/master/labs/Lab14.ipynb)
#         * PA6 - PA8
#     * Review key concepts and definitions
# 1. Work on PA8.
# 1. Start thinking about a fun side project in Python to work on over break!
# 
# ## Next Lesson
# 1. More review.
# 1. Demos of fun stuff in CS.
# 1. In case I forget, congrats on finishing CptS 111, have a great winter break, and enjoy CptS 121!
