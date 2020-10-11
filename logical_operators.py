# Comparison between variables and objects

# Logical operators in Java: !, &&, ||
# Logical operators in Python: not, and, or
print(4 == 5 and True)  # False
print(4 != 5 or False)  # True
print(not (4 >= 5))  # True

# Java: "==" checks if the two objects are the exact instances (or basically points to the same memory location)
# Java: ".equals" checks if the value of two objects is the same

# In Python it kinda works the other way around

# In Python "==" checks if the value of the two objects is the same
# In Python "is" checks if the two objects are the exact instances
s1 = "nick"
s2 = "nick"

print(s1 == s2)  # True
print(s1 is s2)  # WARNING: prints true (Python sets the same instance for both objects)
print("id of s1:", id(s1), "id of s2:",
      id(s2))  # We can check it with id() function in python which returns the “identity” of an object.

s1 = "nick"
s2 = input("Give a string to compare with the string 'nick':")

print(s1 == s2)  # True
print(s1 is s2)  # The outcome is False with any input
print("id of s1:", id(s1), "id of s2:", id(s2))  # We can check it with id() function in python which returns the “identity” of an object.