# global scope

name = "dave"
count = 1

def another():
    color = "blue"
    # count += 1  # This will raise an error since count is not defined in this scope
    global count
    count += 1  # This will work since we declared count as global
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"  # This will modify the color variable in the enclosing scope
        print(color)
        print(name)
        
    greeting("dave")

another()
