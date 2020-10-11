# Lists: In Python You can have any type of object (even different types) in a list.
# Lists are mutable

# Basic List operations.
list = []

list.append("hey")
list.append("building")

# list = ["hey", "building"]  # You can also initialise a list like this

print("Length:", len(list))
print("Index 1:", list[1])

# Insert at a specific index of a list
list.insert(1, "xd")
print(list)

# Deleting an element at a specific index of a list
del (list[1])
print(list)

# Deleting elements in a specific range in a list
del (list[1:2])
print(list)

# Other List operations

# List extension 1 (works similar to concat)
list1 = ["hey", "I"]
list2 = ["am", "Nick"]
list1.extend(list2)
print(list1)

# List extension 2 - Easier version (works similar to concat)
list1 = ["hey", "I"]
list2 = ["am", "Nick"]
list1 = list1 + list2

# List within another list
list1 = ["hey", "I"]
list2 = ["am", "Nick"]
list3 = []
list3.append(list1)
list3.append(list2)

# list3 = [list1, list2] # You can also initialise the list like this instead with the append

print(list3)

# In order to print an element of the second inner list
print(list3[1][1])  # Prints only my name
