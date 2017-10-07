
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/fall2016/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L5-1 Debugging and Function Practice
# 
# Learner objectives for this lesson
# * Understand how Python keeps track of program flow of execution with the call stack
# * Utilize basic features of a debugger

# ## Call Stack
# Recall that functions can call other functions. For example:

# In[2]:

def inner_function(param_two):
    '''
    
    '''
    print("Hello from inner_function(). param_two: %d" %(param_two))
    # 2 (1 + 1) will be copied into return_value in outer_function()
    return param_two + 1

def outer_function(param_one):
    '''
    
    '''
    print("Hello from outer_function(). param_one: %d" %(param_one))
    # 1 (0 + 1) will be copied into param_two in inner_function()
    return_value = inner_function(param_one + 1)
    print("inner_function() return value: %d" %(return_value))
    # 3 (2 + 1) will be copied into return_value in main()
    return return_value + 1
    
def main():
    '''
    
    '''
    print("Hello from main()")
    # note this return_value variable is different than the return_value variable declared in outer_function
    # 0 will be copied into param_one in outer_function()
    return_value = outer_function(0) 
    print("outer_function() return value: %d" %(return_value))

main()


# When a statement in one function (e.g. `main()`) makes a call to another function (e.g. `outer_function()`), the execution of the calling function (e.g. `main()`) resumes once the execution of the called function (e.g. `outer_function()`) completes. As functions are called, Python keeps track of the order of function calls with the *call stack*. Here is an example for the above code:
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/call_stack_example.png)
# 
# The top most function on the call stack is the currently executing function. Once the top most function on the call stack finishes executing, execution returns to the calling function, and so on.
# 
# ## Program Crashes
# If an error occurs in your program, Python prints a *traceback* message to the console, which contains information about the state of the call stack when the program crashes:

# In[5]:

def function_with_error(x):
    '''
    
    '''
    print(y)
    
def main():
    '''
    
    '''
    function_with_error(5)

main()


# ## Debugging Your Program
# A *bug* is an error in your program. *Debugging* is the process of removing bugs from your program.
# 
# How to debug your program:
# 1. Use the debugger (demo to come)
# 1. Insert print statements in your code (aka diagnostic calls)
#     * Display intermediate results at critical points
#     * Make sure everything actually is what you think it is (aka echo, aka sanity check)
# 1. Use Google
#     * Compile and runtime errors: often others have had these before you
#     * Logic errors: make sure you truly understand the algorithm
# Note: if you use *anything* from Google, cite the source in a comment in your code.
# 
# ### Setting Debugger Breakpoints
# We can halt program execution at a specific line number in our code, this is called a *breakpoint.* In Spyder, double click in the gray side bar by the line you wish to place a breakpoint. A red dot representing the breakpoint will appear:
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/setting_breakpoint.png)
# 
# ### Stepping Through Your Program
# Now, instead of running the program with the green play button (or F5), run the *Python debugger* (`pdb`) with the blue play/pause button (Ctrl + F5). The program will run until the breakpoint is reached, then it will pause. Now, you can step through the code line by line, stepping over functions (Ctrl + F10) or into functions (Ctrl + F11). There are also toolbar buttons to do this to the right of the debug play/pause button.
# 
# As you step through your program, you can watch your variable values change in the Variable Explorer panel:
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/variable_explorer.png)
# 
# If you would like to learn more about debugging in Python, read about [`pdb`](https://docs.python.org/3/library/pdb.html) and check out this [`pdb` command cheatsheet](http://web.stanford.edu/class/physics91si/2013/handouts/Pdb_Commands.pdf).

# ## Practice Problems
# Note: Some problem descriptions have been taken from Chapter 2 of Hanly & Koffman's Problem Solving and Program Design in C (7th Edition). For each problem define a `main()` function and use functions where appropriate!

# ### Problem #1 Tax
# Write a program to compute the total price for a purchase after sales tax. Prompt the user to enter the purchase amount and the sales tax percent. Display the total price (to the nearest 2 decimal places) after adding the sales tax to the purchase amount.
# 
# Use functions where appropriate!
# 
# Example output:
# 
# ```
# Please enter the purchase price: 9.00
# Please enter the sales tax as a percent (%): 7.8
# Total purchase price after tax: $9.70
# ```

# In[1]:

def get_purchase_price():
    '''
    
    '''
    price = float(input("Please enter the purchase price: "))
    return price

def get_sales_tax():
    '''
    
    '''
    tax = float(input("Please enter the sales tax as a percent: "))
    return tax

def compute_total_price(price, tax):
    '''
    
    '''
    price += price * (tax / 100)
    return price

def display_total_price(total):
    '''
    
    '''
    print("Total purchase price after tax: $%.2f" %(total))
    
def main():
    '''
    
    '''
    price = get_purchase_price()
    tax = get_sales_tax()
    total = compute_total_price(price, tax)
    display_total_price(total)
main()


# ### Problem #2 Mileage Reimbursement
# Write a program that calculates mileage reimbursement for a salesperson at the rate of \$.35 per mile. 
# 
# Use functions where appropriate!
# 
# Example output:
# 
# ```
# MILEAGE REIMBURSEMENT CALCULATOR
# Please enter the beginning odometer reading: 13505.2
# Please enter the ending odometer reading: 13810.6
# You traveled 305.4 miles. At $0.35 per mile, your reimbursement is $106.89
# ```

# In[6]:

def get_reading(label):
    '''
    
    '''
    odo = float(input("Please enter the %s odometer reading: " %(label)))
    return odo

def compute_difference(reading1, reading2):
    '''
    
    '''
    diff = reading2 - reading1
    return diff
    
def compute_reimbursement(diff):
    '''
    
    '''
    reimb = diff * 0.35
    return reimb

def display_reimbursement(diff, r):
    '''
    
    '''
    print("You traveled %.1f miles. At $0.35 per mile, your reimbursement is $%.2f" %(diff, r))
    
def main():
    '''
    
    '''
    r1 = get_reading("beginning")
    r2 = get_reading("ending")
    diff = compute_difference(r1, r2)
    reimb = compute_reimbursement(diff)
    display_reimbursement(diff, reimb)

main()


# ### Problem #3 Pythagoras
# The Pythagorean theorem states that the sum of the squares of the sides of a right triangle is equal to the square of the hypotenuse.
# 
# $$side1^{2} + side2^{2} = hypotenuse^{2}$$
# 
# For example, if two sides of a right triangle have lengths 3 and 4, then the hypotenuse must have a length of 5. Together the integers 3, 4, and 5 form a Pythagorean triple. There are an infinite number of such triples. Given two positive integers `m` and `n`, **where `m`> `n`**, a Pythagorean triple can be generated by the following formulas:
# 1. side1 = $m^2 – n^2$
# 1. side2 = $2mn$
# 1. hypotenuse = $m^2 + n^2$
# 
# Write a program that takes the values for `m` and `n` as input and displays the values of the Pythagorean triple generated by the formulas above.
# 
# Use functions where appropriate!
# 
# Example output:
# 
# ```
# Please enter an m value: 4
# Please enter an n value: 2
# Pythagorean triple: 12^2 + 16^2 = 20^2
# ```

# In[5]:

def get_value(m_or_n):
    '''
    
    '''
    val = int(input("Please enter an %s value: " %(m_or_n)))
    return val

def compute_side1(m, n):
    '''
    
    '''
    side1 = m ** 2 - n ** 2
    return side1

def compute_side2(m, n):
    '''
    
    '''
    side2 = 2 * m * n
    return side2

def compute_hypotenuse(m, n):
    '''
    
    '''
    hypo = m ** 2 + n ** 2
    return hypo

def display_triple(s1, s2, hypo):
    '''
    
    '''
    print("Pytahgorean triple: %d^2 + %d^2 = %d^2" %(s1, s2, hypo))
    
def main():
    '''
    
    '''
    m = get_value("m")
    n = get_value("n")
    s1 = compute_side1(m, n)
    s2 = compute_side2(m, n)
    hypotenuse = compute_hypotenuse(m, n)
    display_triple(s1, s2, hypotenuse)
main()


# ## TODO
# 1. Work on PA2.
# 2. Read Appendix A (Chapter 20) and Chapter 5.
# 
# ## Next Lesson
# We start conditionals!
