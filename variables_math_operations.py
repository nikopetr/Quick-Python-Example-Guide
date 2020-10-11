# Strings in python (works with both single or double quotes)
s1 = "words"
s2 = 'words'


# Printing different var types
x = 4
print("x =", x)  # Python automatically puts a space for the separation
print("x = ", x, sep="")  # Custom separation


# Math Operations
# Addition
x = 4 + 4
print("x =", x)

# Division
x = 3 / 4
print("x =", x)

# Int Division (in order to work like Java)
x = 3 // 4
print("x =", x)

# Pow
x = 2 ** 3  # 2^3
print("x =", x)

# Mod
x = 4 % 2
print("x =", x)


# Casting
x = 3.5
x = int(x)
print("x =", x)
# x = int(3.5) works as well


# Max-Min function
x = max(3, 4, 5)
print("x =", x)
x = min(3, 4)
print("x =", x)