# in the list and strings the index or coefficient always starts with 0 not 1
# lists are created using []


a = [1,2,3,5666,6,666,6,6,66,6,6,6,6,6,6,64,3,32,2,43,4,5,766]
a[4] = 768
print(a)

#we can create a list for items of different types
b = 456
d = [b, 'Bilal', True, 8.543, False]
print(d)

# List slicing

members = ['Bilal', 'Sheeraz', 'Jahangir', 140]
print(members[0:2])
print(members[-3:]) # means from element members(1) until the end
