# Functions

# my_sum works for both 2 or 3 parameters since c be default is equal to 0
def my_sum(a, b, c=0):
    return a + b + c


print(my_sum(1, 1))  # Call mySum with 2 parameters
mystery = my_sum
print(mystery(1, 1, 1))  # Call mySum with 3 parameters
