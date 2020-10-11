# User-input
# print("Enter a number: ") # This would cause a change of line
print("Enter a number: ", end="")  # This keeps the cursor on the same line
x = input()

print("You entered:", x)


# Simpler(better) User-input

# Remember to cast the input to the preferable type in order to avoid future problems
x = float(input("Enter a number: "))
print("You entered:", x)