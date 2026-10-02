# This is a simple program to demonstrate the use of lists in Python.
# Create a list of numbers from 0 to 9
x = list(range(10))
print('The list x is:', x)
# replace elements from index 5 to 7 with new values
x[5:8] = [14, 15, 16]
print('The list x after replacing elements from index 5 to 8 is:', x)
# delete the element at index 7
del x[-3]
print('The list x after deleting the element at index 7 is:', x)
y = [7 , 8, 9]
print('The list y is:', y)
print('The list x * 2 is:', x * 2)
print('The list x + y is:', x + y)
print('19 is in x:', 19 in x)
print('19 is not in x:', 19 not in x)
print('15 is in x:', 15 in x)