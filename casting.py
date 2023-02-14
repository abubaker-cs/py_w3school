# Python Casting

"""
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an
object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

    1. int()
    2. float()
    3. str()
"""

# Integer
# Constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal
# (providing the string represents a whole number)
x = int(1)          # x will be 1
y = int(2.8)        # y will be 2
z = int("3")        # z will be 3

print("Integers:")

print("x: " + str(x))
print("y: " + str(y))
print("z: " + str(z))

print("")
print("-------------------------------------------")
print("")

# Float
# Constructs a float number from an integer literal, a float literal or a string literal (providing the string
# represents a float or an integer)
a = float(1)        # a will be 1.0
b = float(2.8)      # b will be 2.8
c = float("3")      # c will be 3.0
d = float("4.2")    # d will be 4.2

print("Floats:")

print("a: " + str(a))
print("b: " + str(b))
print("c: " + str(c))
print("d: " + str(d))

print("")
print("-------------------------------------------")
print("")

# Strings
# Constructs a string from a wide variety of data types, including strings, integer literals and float literals
e = str("s1")       # e will be 's1'
f = str(2)          # f will be '2'
g = str(3.0)        # g will be '3.0'

print("Strings:")

print("e: " + e)
print("f: " + f)
print("g: " + g)