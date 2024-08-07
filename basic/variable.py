# Python 변수 & 자료형

# int
number = 10
typeOfNumber= type(number)

# float
floatNumber = 10.1
typeOfFloat = type(floatNumber)

# string
string = 'Hello~ Python!'
typeOfString = type(string)

# boolean
boolean = True
typeOfBoolean = type(boolean)

# list
list = [1, 2, 3]
typeOfList = type(list)

# tuple
tuple = (1, 2, 3)
typeOfTuple = type(tuple)

# dictionary
dictionary = {'name': 'Kim', 'age': 30}
typeOfDictionary = type(dictionary)

# set
set = {1, 2, 3}
typeOfSet = type(set)

print('number:', number, typeOfNumber)
print('floatNumber:', floatNumber, typeOfFloat)
print('string:', string, typeOfString)
print('boolean:', boolean, typeOfBoolean)
# ------------------------------
print('list:', list, typeOfList)
print('tuple:', tuple, typeOfTuple)
print('dictionary:', dictionary, typeOfDictionary)
print('set:', set, typeOfSet)
# ------------------------------
print('list get 1:', list[1])
print('tuple get 1:', tuple[1])
print('dictionary get name:', dictionary['name'])
print('set get 1:', set.pop())
