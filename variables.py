# Python has no command for declaring a variable, it is created once you first assign a value to it
x = 5
y = "John"
print(x)
print(y)

# Once assigned, the type of variable can be changed:
x = 4
x = "Abubaker"
print(x)

# Casting: Manually assigning the type of data
##############################################

x = str(3)
y = int(4)
z = float(34.33)
print(x)
print(y)
print(z)

# type(?)
#########
print(type(x))
print(type(y))
print(type(z))

# Single or Double Quotes?
##########################
x = "Abubaker Farooq"
# is the same as
x = 'John'

# Case-Sensitive
################
a = "Abubaker"
A = "Farooq"  # A will not overwrite a
print(a)
print(A)

# Naming Convention:
# ##################
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Multi Words Variable Names
camelCase = "Abubaker"
PascalCase = "Abubaker"
snake_case = "Abubaker"

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Apple"

print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

"""
    Multiline
    Comment
"""

# Unpack a Collection If you have a collection of values in a list, tuple etc. Python allows you to extract the
# values into variables. This is called unpacking.
cars = [
    "BMW",
    "Mazda",
    "Toyota"
]

x, y, z = cars

print(x)
print(y)
print(z)

# Python - Output Variables

# The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# For numbers, the + character works as a mathematical operator:
x = 24
y = 12
print(x + y)

# The best way to output multiple variables in the print() function is to separate them with commas, which even
# support different data types:
x = 31
y = "Abubaker"
print(x, y)

# Global Variables
# ///////////////
# Variables that are created outside a function (as in all the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

# Create a variable outside a function, and use it inside the function
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

"""
    If you create a variable with the same name inside a function, this variable will be local, and can only be used 
    inside the function. The global variable with the same name will remain as it was, global and with the original 
    value.
"""

# Create a variable inside a function, with the same name as the global variable

x = "great_outside"


def mygreat():
    x = "great_inside"
    print("Python is " + x)


mygreat()

print("Python is " + x)

# The global Keyword
"""
    Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
    To create a global variable inside a function, you can use the global keyword.
"""


def myDef():
    global x
    x = "fantastic"


myDef()

print("Python is " + x)

# Also, use the global keyword if you want to change a global variable inside a function.
y = "awesome_outside"


def myfunc():
    global y
    y = "fantastic_inside"


myfunc()

print("Python is " + y)
