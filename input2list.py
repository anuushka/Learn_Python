#If the inputs are given on one line separated by a character (the delimiter), use split() to get the separate values in the form of a list. 
#If the list values are all integer types, use the map() method to convert all the strings to integers.

a = input()
lis = a.split()
newlis = list(map(int, lis))
print (newlis)
