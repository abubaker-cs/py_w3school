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

