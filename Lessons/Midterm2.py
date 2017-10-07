
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/fall2016/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# #  Midterm #2 Solutions

# In[3]:

vehicle = "rocket"
my_candy = "twix"

print("0...%d" %(len(my_candy) - 1))
print(len(vehicle))
print(my_candy[2])
print("Rocket" == vehicle)
print("apple" < my_candy)
print(my_candy[1:3])
new_string = vehicle[3:]
print(new_string)
print(my_candy.upper())
print(vehicle[1:4])
new_string = my_candy + " is the best"
print(new_string)


# String: sequence of characters
# 
# Valid indices of a string in terms of string length, n: 0...n-1
# 
# range
# 
# strip
# 
# immutable 
# 
# break

# In[ ]:

# Open file
infile = open("somefile.txt", "r")
# Process file
infile.readline()
# Close file
infile.close()


# In[ ]:

print("hello")
print("hello", end="")


# File modes covered in class:
# 1. "r"
# 1. "w"
# 1. "a"

# In[4]:

i = 0
while i < 3:
   print(i)
   i += 1 
print("Final value of i: ", i)


# In[ ]:

# infinite loop
# no progress towards BC being false
i = 10
while i > 5:
   print(i)
i -= 1


# In[14]:

# syntax error
i = 0
while i < 5:
print(i)
i += 1


# In[8]:

for i in range(-4, 4, 2):
   print(i)
print("Final value of i: ", i)


# In[ ]:

def open_input_file():
    fname = input("Please enter the name of a file to open: ")
    infile = open(fname, "r")
    return infile


# In[ ]:

import random
for i in range(500):
    print random.randrange(1, 9)


# In[11]:

choice = 1
while choice != 3:
    print("Welcome to my game!")
    print("1)View the rules")
    print("2)Play the game")
    print("3)Quit")
    choice = int(input(">"))
    if choice == 1:
        print("Here are the rules")
    elif choice == 2:
        print("Starting the game")
    elif choice == 3:
        pass
    else:
        print("Not a valid menu option")


# In[13]:

import math

# assume already defined
def is_prime(n):
    '''
    
    '''
    prime = True
    sqrt_n = math.sqrt(n)
    m = 2
    
    while m <= sqrt_n and prime:
        rem = n % m
        if rem == 0:
            prime = False
        m += 1
    return prime
    
def sum_primes(n):
    '''
    
    '''
    summ = 0
    for i in range(2, n + 1):
        if is_prime(i):
            summ += i
    return summ
    

n = int(input("Please enter an integer >= 2: "))
summ = sum_primes(n)
print("The sum of the prime numbers from 2 to %d is: %d" %(n, summ))


# String methods
# 1. `strip`
# 1. `upper`
# 1. `lower`
# 1. `find`
# 1. `replace`
# 1. Many others exist
# 
# Strings are compared for equality based on their unicode values. 
# 
# One solution:
# 
# Side1: 2, 8, 6, 1
# 
# Side2: 1, 4, 9, 3
# 
# Side3: 2, 5, 7, 3
