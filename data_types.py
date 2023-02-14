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

# 01 Text Type:
# 1. str
x = "Hello World"
print("str: " + x)

# 02 Numeric Types:
# 2. int
# 3. float
# 4. complex
x = 20
print("int: " + str(x))

x = 36.98
print("float: " + str(x))

x = 1j
print("complex: " + str(x))

# 03 Sequence Types:
# 5. list
# 6. tuple
# 7. range

x = ["apple", "orange", "cherry"]
print("list: " + str(x))

x = ("apple", "banana", "orange")
print("tuple: " + str(x))

x = range(6)
print("range: " + str(x))

# 04 Mapping Type:
# 8. dict
x = {"name": "Abubaker", "age": 36}
print("dict: " + str(x))

# 05 Set Types:
# 9. set
# 10. forzenset
x = {"bmw", "mazda", "suzuki"}
print("set: " + str(x))

x = frozenset({"apple", "banana", "cherry"})
print("frozenset: " + str(x))

# 06 Boolean Type
# 11. bool
x = True
print("boolean: " + str(x))

# 07 Binary Types:
# 12. bytes
# 13. bytearray
# 14. memoryview
x = b"Hello"
print("bytes: " + str(x))

x = bytearray(5)
print("bytearray: " + str(x))

x = memoryview(bytes(5))
print("memoryview: " + str(x))

# None Type:
# 15. NoneType
x = None
print("NoneType: " + str(x))

"""
    Setting the Specific Data Type
    ==============================
    If you want to specify the data type, you can use the following constructor functions:
"""
x = str("Hello World")
print(type(x))

x = int(29)
print(type(x))

x = float(32.32)
print(type(x))

x = complex(1j)
print(type(x))

x = list(("apple", "banana", "cherry"))
print(type(x))

x = tuple(("apple", "banana", "cherry"))
print(type(x))

x = range(6)
print(type(x))

x = dict(name="John", age=36)
print(type(x))

x = set(("apple", "banana", "cherry"))
print(type(x))

x = frozenset(("apple", "banana", "cherry"))
print(type(x))

x = bool(5)
print(type(x))

x = bytes(5)
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))