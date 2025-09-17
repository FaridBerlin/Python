def squared(num):
    return num * num
# lambda version
# squared = lambda num : num * num

print(squared(2))

def addTwo(num):
    return num + 2
# lambda version
# addTwo = lambda num : num + 2

print(addTwo(12))

def sum_total(a, b):
    return a + b

# lambda version
# sum = lambda a, b : a + b

print(sum_total(2, 2))


###################################

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

#############################################



numbers = [3, 7, 12, 18, 20, 21]
squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))

###########################

odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))

###############################################

from functools import reduce


numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))  # built-in sum function

lambda acc, curr: acc + len(curr)

names = ['Alice', 'Bob', 'Charlie', 'David']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
