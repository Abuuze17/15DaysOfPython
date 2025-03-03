# # Learning about the primitive data types in Python.

# # Strings
# # Integers
# # Floats
# # Booleans

# TypeError
# These errors occur when you are using the wrong data type. e.g. len(12345)

# Because you can only give the len() function Strings, it will refuse to work and give you a TypeError if you give it a number (Integer).

# e.g len(12345)

# solutions

len("Hello")

# Type Checking
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

# Type Conversion
str()
int()
float()
bool()

name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))  # str
print(type(length_of_name))  # int

print("Number of letters in your name: " + str(length_of_name))