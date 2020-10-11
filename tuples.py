# Tuples: something like IMMUTABLE lists but with some differences,for more details:
# https://www.geeksforgeeks.org/python-difference-between-list-and-tuple/
x = "this", "is", "a", "tuple", 10  # or x = (2, 3, 4, 5)
print(x)

x = "single element tuple",
print(x)

x = x, (4, "another")  # Tuple inside a tuple
print(x)
print(x[1])