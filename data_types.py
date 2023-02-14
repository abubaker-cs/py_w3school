# Python Data Types
print("Python Data Types")

# Built-in Data Types

"""
    1. Text Type:	str
    2. Numeric Types:	int, float, complex
    3. Sequence Types:	list, tuple, range
    4. Mapping Type:	dict
    5. Set Types:	set, frozenset
    6. Boolean Type:	bool
    7. Binary Types:	bytes, bytearray, memoryview
    8. None Type:	NoneType
"""

# Getting the Data Type - You can get the data type of any object by using the type() function:
x = 5
print(type(x))

"""
    Setting the Specific Data Type
    ==============================
    In Python, the data type is set when you assign a value to a variable:
"""
x = "Hello World"
print("str: " + x)

x = 20
print("int: " + str(x))

x = 36.98
print("float: " + str(x))

x = 1j
print("complex: " + str(x))

x = ["apple", "orange", "cherry"]
print("list: " + str(x))

x = ("apple", "banana", "orange")
print("tuple: " + str(x))

x = range(6)
print("range: " + str(x))

x = {"name": "Abubaker", "age": 36}
print("dict: " + str(x))

x = {"bmw", "mazda", "suzuki"}
print("set: " + str(x))

x = frozenset({"apple", "banana", "cherry"})
print("frozenset: " + str(x))

x = True
print("boolean: " + str(x))

x = b"Hello"
print("bytes: " + str(x))

x = bytearray(5)
print("bytearray: " + str(x))

x = memoryview(bytes(5))
print("memoryview: " + str(x))

x = None
print("NoneType: " + str(x))

"""
    Setting the Specific Data Type
    ==============================
    If you want to specify the data type, you can use the following constructor functions:
"""

