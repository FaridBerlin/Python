def hello ():
    print("Hello World!")

hello()

def sum(num1=0, num2=0):
    if (type(num1) != int or type(num2) != int):
        return 0 
    return num1 + num2

total = sum(7, 3)
print("The sum is:", total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items('apple', 'banana', 'cherry')

def multiple_items_with_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))
multiple_items_with_kwargs(name='John', age=30, city='New York')