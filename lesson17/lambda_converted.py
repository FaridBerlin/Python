# Original lambda functions converted to def functions
# This is what VS Code might suggest when you use "Convert to function" refactoring

def squared(num):
    return num * num

print(squared(2))

def addTwo(num):
    return num + 2

print(addTwo(12))

def sum_func(a, b):  # Note: renamed from 'sum' to avoid conflict with built-in sum()
    return a + b

print(sum_func(2, 2))

# Original lambda versions (commented out for comparison):
# squared = lambda num : num * num
# addTwo = lambda num : num + 2
# sum = lambda a, b : a + b
