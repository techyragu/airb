# Getting input from user
# name = input("What is your name? ")
# color = input("Which is your fav color? ") #built in function
# print(name + ' likes ' + color )

# multiply string by number using *
# print('*' * 10) # **********
# print(type(10))

# print(type(range(5)))

# List
#zeroes = [0] * 10   # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#print(zeroes) 
#print([id(i) for i in zeroes]) # all pointing to same object
# [4320503200, 4320503200, 4320503200, 4320503200, 4320503200, 4320503200, 4320503200, 4320503200, 4320503200, 4320503200]

# print(id(zeroes[1]))
# zeroes[1] = 2
# print(id(zeroes[1])) # changed

# nested_zeroes = [[0]] * 10
# print(nested_zeroes) # [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
# print([id(i) for i in nested_zeroes]) # All point to same object
# nested_zeroes[0].append(1)  # CAREFUL 
# print(nested_zeroes) # [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]

# create 2d matrix

# matrix = [ [j for j in range(5)] for i in range(5)]
# print(matrix)
# #print([id(i) for i in matrix])
# for row in matrix:
#     print(id(row))
#     for col in row:
#         print(id(col), end= ",")
#     print()


# matrix0 = [ [0] * 5 for i in range(5)]
# print(matrix0)
# print([id(i) for i in matrix0])

# numbers = list(range(5))
# print(numbers)
# print(numbers[1:3])
# numbers[1:3][0] = 5 # slice create new list reference
# print(numbers)

# numbers.insert(8, 99)
# del numbers
# print(numbers)


items = [
    ("product1", 20),
    ("product2", 10),
    ("product3", 30)
]

# sort on price
# items.sort()
# items.sort(key=lambda x: x[1])

# print(map(lambda item:item[1], items))
# print(list(map(lambda item:item[1], items)))

# print(filter(lambda item: item[1] >=20, items))
# print(list(filter(lambda item: item[1] >=20, items)))

# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
# print(zip(list1, list2))
# print(list(zip(list1, list2)))

# s1 = {1,3,7}
# print(s1)
# s1.add(4)
# print(s1)
# s1.add(9)
# print(s1)

# first = {1,2,3}
# second = {2,3,4}
# print(first|second) # union {1, 2, 3, 4}
# print(first&second) # intersection {2, 3}
# print(first-second) # only in a {1}
# print(first^second) # only in first or second, not in both {1, 4}

# d = dict()
# print(d)
# d = {}
# print(d)

# s = set()
# print(s)

# with open("/Users/rahulgupta/learnspace/codewithmosh/app.py") as file:
#     print(file.name)


# from timeit import timeit
# code1="""
# for i in range(5):
#     pass
# """
# print("code1", timeit(code1, number=10000))

# class Point():

#     default_color = "red" # class attribute (share across all objects)

#     @classmethod    # class method , decorator classmethod, first param is cls
#     def zero(cls):
#         return cls(0,0) # returns point object 


#     def __init__(self, x, y):
#         self.x = x # instance attribute
#         self.y = y

#     def draw(self): # instance method
#         print("draw point")

# point = Point(1, 2)
# print(isinstance(point, Point))


import random
import string

print(random.random())