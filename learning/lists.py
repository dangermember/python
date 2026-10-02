x = list(range(10))
x[-2:5] = [14, 15, 16]
del x[-3]
y = [7 , 8, 9]
print('The list x is:', x)
print('The list y is:', y)
print('The list x * 2 is:', x * 2)
print('The list x + y is:', x + y)
print('19 is in x:', 19 in x)
print('19 is not in x:', 19 not in x)
print('15 is in x:', 15 in x)