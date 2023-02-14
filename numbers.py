import random

"""
    Python Numbers
    1. Integer
    2. Float
    3. Complex
"""

x = 1  # int
y = 2.8  # float
z = 1j  # complex

# type() = to verify the type of existing variable
print("1: " + str(type(x)))
print("2.8: " + str(type(y)))
print("1j: " + str(type(z)))

print("")
print("-------------------------------------------")
print("")

# int = Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 2342349082398493284
z = -234234
print("1: " + str(type(x)))
print("2342349082398493284: " + str(type(y)))
print("-234234: " + str(type(z)))

print("")
print("-------------------------------------------")
print("")

# float = Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 123.3434
y = 1.0
z = -3434.343
print("123.3434: " + str(type(x)))
print("1.0: " + str(type(y)))
print("-3434.343: " + str(type(z)))

print("")
print("-------------------------------------------")
print("")

# Note: Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 34e4
y = 12E3
z = -94.3e100
print("34e4: " + str(type(x)))
print("12E3: " + str(type(y)))
print("-94.3e100: " + str(type(z)))

print("")
print("-------------------------------------------")
print("")

# Complex = Complex numbers are written with a "j" as the imaginary part:
x = 3 + 5j
y = 5j
z = -5j

print("3+5j: " + str(type(x)))
print("5j: " + str(type(y)))
print("-5j: " + str(type(z)))

print("")
print("-------------------------------------------")
print("")

# Type Conversion - You can convert from one type to another with the int(), float(), and complex() methods:

x = 1  # int
y = 2.8  # float
z = 1j  # complex

# int > float
a = float(x)

# float > int
b = int(y)

# int > complex
c = complex(x)

print(str(a) + ": " + str(type(x)))
print(str(b) + ": " + str(type(y)))
print(str(c) + ": " + str(type(z)))

print("***")
print("Note: You cannot convert complex numbers into another number type.")

print("")
print("-------------------------------------------")
print("")

# Random Number: Import the random module, and display a random number between 1 and 9:
print(random.randrange(1, 10))
