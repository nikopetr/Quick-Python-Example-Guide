# Strings
# In Python, a string is immutable (Just like Java). You cannot overwrite the values of immutable objects.
# However, you can assign the variable again

# Length of a String
s = "input"
print("Length =", len(s))

# Substring 1
s = "01234"
print("Substring 1:", s[2:])  # From index 2 to the end

# Substring 2 (In between letters)
s = "01234"
print("Substring 2:", s[1:3])  # Starts from index 1 to 3

# Substring 3 (Last letters)
s = "01234"
print("Substring 3:", s[-3:])  # Last 3 characters from the end

# Contains substring (Works with all four cases)
s = "input"
print("Contains :", "pu" in s)
print("Contains :", "p" in s)
print("Contains :", 'p' in s)
print("Contains :", 'pu' in s)