users = ["Jon", "Bob", "Li"]

data = ['Jon', 33, True]

empty_list = []

print('Jon' in empty_list)

print(users[0])
print(users[-2])
print(users.index('Li'))

print(users[0:2])
print(users[1:])
print(users[:2])
print(users[1:3])

print (len(data))

users.append('Alice')
print(users)

users += ['Charlie', 'Diana']
print(users)

users.extend(['Eve', 'Frank'])
print(users)

users.insert(0, 'Zoe')
print(users)

users[2:2] = ['Grace', 'Hank']
print(users)

users[1:3] = ['Ivy', 'Jack']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users.pop(1))

del users[0]
print(users)

data.clear()
print(data)

users[1:2] = ['david']

users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]


print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)


# Tuple example
# tuples can not be changed after creation!!!

mytuple = tuple(("Neil", 22, True))

another_tuple = (1, 4, 2, 8)

print(mytuple)
print(type(mytuple))
print(type(another_tuple))

newlist = list(mytuple)
newlist.append("new item")
newtuple = tuple(newlist)
print(newtuple)

(one, *two, three) = another_tuple
print(one)
print(two)
print(three)

print(another_tuple.count(2))


