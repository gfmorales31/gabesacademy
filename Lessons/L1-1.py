
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](# [CptS 111](http://piazza.com/wsu/fall2016/cpts111/home)
# [Washington State University](https://wsu.edu/)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L1-1 Introduction
# 
# Learner objectives for this lesson
# * Gain an overview of the course and its expectations
# * Understand the details of the syllabus
# * Learn a high level view of computer science
# * Introduce yourself and meet others

# ## Course Overview
# Welcome to CptS 111! Please see the [course website](piazza.com/wsu/fall2016/cpts111/home) for the syllabus and information about the course. Now let's get started!
# 
# ## What is Computer Science?
# Computer science is the study of computers and computational systems, with a particular focus on *algorithms* and *problem solving*
# * An algorithm is a sequence of instructions that solves a problem
# * Problem solving is formulating problems and designing, creative, clear, and accurate solutions

# You try it: What are areas of study in Computer Science?
# * Artificial intelligence
# * Graphics
# * Networks
# * Software engineering
# * Programming languages
# * Computer systems
# * Security
# * Bioinformatics
# * Database systems
# * Many others

# ### What Can Computers Do?
# Computers can perform 6 fundamental operations:
# #### 1. Accept input (i.e. from the user)

# In[1]:

input("Please enter a number: ")


# #### 2. Produce output

# In[2]:

print("CptS 111 is awesome!")


# #### 3. Assign a value to a variable

# In[3]:

x = 5


# #### 4. Arithmetic (math)

# In[4]:

12 * 60


# #### 5. Compare and branch (conditionals)

# In[6]:

if x > 10:
    print("x is greater than 10")


# #### 6. Repeat a set of instructions (loops)

# In[7]:

x = 0
while x < 5:
    print(x)
    x = x + 1


# All of the programs you have used are composed of combinations of these 6 types of computer instructions, that is amazing! Writing programs, or *programming*, is really breaking problems into smaller and smaller subtasks until the subtasks are simple enough to be solved using the basic instructions above. These subtasks are *algorithms*.

# ### Algorithms
# What is an algorithm? **A sequence of instructions that solves a problem**. A sequence of instructions is an algorithm if it meets the following criteria:
# * Well-ordered instructions
# * Unambiguous instructions
# * Computable instructions
# * Produces a result
# * Doesn't run forever
# 
# Why are algorithms so important to computer science? If we can specify an algorithm...
# * We can automate the solution
# * We can also repeat a solution to a problem
# 
# Impossible to do these algorithms on this scale without computers: [Google Inside Search](http://www.google.com/insidesearch/howsearchworks/thestory/)
# In 60 seconds, 2,314,800 google searches!!
# 
# ### Examples of Algorithms
# Algorithms are a sequence of instructions that solves a problem. Algorithms are everywhere!
# 
# Is this an algorithm?
# * In a Dutch oven, cook sausage, ground beef, onion, and garlic over medium heat until well browned. 
# * Stir in crushed tomatoes, tomato paste, tomato sauce, and water. Season with sugar, basil, fennel seeds, Italian seasoning, 1 tablespoon salt, pepper, and 2 tablespoons parsley. Simmer, covered, for about 1 1/2 hours, stirring occasionally.
# * Bring a large pot of lightly salted water to a boil. Cook lasagna noodles in boiling water for 8 to 10 minutes. 
# * Drain noodles, and rinse with cold water. 
# 
# Yes
# 
# Is this an algorithm?
# * Top with a third of mozzarella cheese slices. 
# * Spoon 1 1/2 cups meat sauce over mozzarella, and sprinkle with 1/4 cup Parmesan cheese. 
# * Repeat layers, and top with remaining mozzarella and Parmesan cheese. Cover with foil: to prevent sticking, either spray foil with cooking spray, or make sure the foil does not touch the cheese. [http://allrecipes.com/recipe/worlds-best-lasagna/](http://allrecipes.com/recipe/worlds-best-lasagna/).
# 
# No! Why not? Hint: Are any operations missing? Are all operations unambiguous?
# 
# Is this an algorithm?
# * Apply small amount of shampoo to hair
# * Work into scalp for about 1 minute
# * Rinse thoroughly
# * Repeat
# 
# No! Why not? Hint: Is it well ordered? Does it halt?
# 
# You try it: Write an algorithm for filling your gas tank.
# * Pay
# * Remove gas cap
# * Place gas nozzle in tank (could be ambiguous if diesel is an option)
# * Pull lever to fill
# * Stop filling when full (could run forever if this line wasn't here)
# * Remove nozzle
# * Replace gas cap (have to remove nozzle first, wouldn't be well ordered if these were flipped)
# 
# 
# ## High-level Programming Languages
# Just like how we have many different *natural* languages for humans to talk to each other (e.g. English, Spanish, German, etc.), there are many different *programming* languages for humans to talk with computers (e.g. **Python**, C, C++, Java, etc.).
# 
# You may have heard of binary? It's a bunch of 0's and 1's. Watch this Big Bang Theory [clip](https://www.youtube.com/watch?v=8emAAkjLoBw) on binary! Programming languages are a medium between natural languages and binary. 
# 
# Note: natural languages are often ambiguous and contain redundant information. For example, consider this text: 
# 
# >It deosn't mttaer in waht oredr the ltteers in a
# word are, the iprmoatnt tihng is taht the frist
# and lsat ltteer are in the rghit pcale.
# 
# We humans can read this, despite the fact that 13 of the 27 words are misspelled. Another example:
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/betty.png)
# 
# Clearly Alice and Betty don't have on the same dress. These two examples are important to keep in mind because writing code in a programming language is much more precise than natural language. Your computer is very literal and you need to pay attention to detail.
# 
# Example: [Domain name system](https://en.wikipedia.org/wiki/Domain_Name_System)
# 
# ### The Continuum of Languages
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/language_continuum.jpg)
# * Low-level languages were created from the perspective of the machine; working with 1's and 0's, also known as logic levels **"machine readable"**
# * High-level languages, have natural language like elements **"human readable"**
# 
# Problem: Computers can't execute high-level programming languages
# Solution: They must be translated
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/interpreter.jpg)
# * Programmer uses a text editor to write a text-based source file in a programming language
# * A Compiler program translates source file
#  * Checks to make sure that program is syntactically correct
#  * If so, the compiler translates the program into a file with lower level instructions (byte code)
# * An Interpreter program translates the byte code into architecture-specific machine readable instructions and runs the program.
# 
# ### Library Modules
# High-level programs often make use of software libraries containing predefined pieces of code (code you don't have to write, but get to use!), including
# * Math functions
# * Input/output functions
# * Graphics libraries
# 
# ### Executing Programs
# In this class, programs will execute in a text-based window called a console
# * Input data can be entered at command-line prompts
# * Output results will be displayed in the console window
# In the real world, many programs have a graphical user interface (GUI). We will touch on GUI programming, but it is beyond the scope of this course. Major in computer science and take upper-division CS classes, you will learn GUI programming then :)
# 
# ### Integrated Development Environments (IDE)
# Combines editing of source code with running your program.
# * Generally a single button will start the translation process
# Provide a variety of tools to assist programmers, for example, 
# * Source code syntax highlighting
# * Autocompletion lists ("Intellisense")
# * A debugger, which allows a programmer to step through programs, one instruction at a time
# * A testing framework for developing unit tests

# ## TODO
# When learning to program (or really any new skill), practice is essential. In this class, I will always make sure you have material to learn and practice programming. At the end of each lesson, I will have a section called TODO (slang for an action item you need "to do"). Since we haven't learned programming just yet, your first to do list will be a little different than future lists:
# 1. Introduce yourself to me! Come by my office hours with a cool picture or story from an adventure you had this summer. If you *really* can't make it to my office hours, you can send me an email instead.
# 1. Visit [Blackboard](https://learn.wsu.edu/) and open the Piazza link. Enroll in the CptS 111 Piazza course and add yourself to your lab section group.
# 1. Visit the [course schedule](http://www.eecs.wsu.edu/~gsprint/cpts111/schedule.html) and get a jump start on the reading. Read chapters 1 and 2 tonight.
# 1. Take a look at [Lab 0](http://nbviewer.jupyter.org/github/gsprint23/cpts111/blob/master/labs/Lab0.ipynb) (downloading and installing Python Anaconda3). *There are no official lab meetings this week.* We will discuss Lab 0 in detail during Wednesday's lesson.
# 
# ## Next Lesson
# We dive into Python :D
