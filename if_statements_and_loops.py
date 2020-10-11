# If/else/elif statements
x = 3
y = 5
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

# While loop
i = 0
while i < 3:
    print(i, end=" ")
    i += 1  # The increment with the use of x++ doesn't not work in Python
print()

# For loop
for i in range(10):  # Loops from i = 0 until i = 9
    print(i, end=" ")
print()

for i in range(2, 10):  # Starting from 2
    print(i, end=" ")
print()

for i in range(2, 10, 3):  # Starting from 2, with step =3
    print(i, end=" ")
print()

# For each loop
list = [0, 1, 2, 3, 4]
for x in list:
    print(x, end=" ")
print()

# continue and break works exactly like Java, and you can also use it on a for loop
