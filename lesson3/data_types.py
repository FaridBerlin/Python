import math

# Strung data types 

# literal assignments

first = "Boby"
last = "Fisher"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function

# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
full_name = first + " " + last

print(full_name)

full_name += "!"

print(full_name)

# casting a number to a string

decade = str(1970)
print(type(decade))
print(decade)

statement = "The decade was " + decade + "s."
print(statement)

# multiple lines
multi_line = """
This is a string that spans
       multiple lines.
            All the way to the end."""
print(multi_line)


# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere \'s this at\\located?'
print(sentence)

# String methods

# print(first)
# print(first.lower())
# print(first.upper())
# print(first)


print(multi_line.title())
print(multi_line.replace("end", "start"))
print(multi_line)

print(len(multi_line))
multi_line += '                                  '
multi_line = '                    ' + multi_line
print(len(multi_line))

print(len(multi_line.strip()))
print(len(multi_line.lstrip()))
print(len(multi_line.rstrip()))

print ("")


# Build a menu
title = "Menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$2".rjust(4))
print("Muffin".ljust(16, ".") + "$1.50".rjust(4))
print("Cheesecake".ljust(16, ".") + "$3".rjust(4))


print("")

# String index values
print(first[1])
print(first[-1])
print(first[1:-1])

# some methods return boolean data

print(first.startswith("B"))
print(first.endswith("Z"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(myvalue))
print(type(x))
print(isinstance(myvalue, bool))
print(isinstance(x, bool))

# Numeric data types
price = 100 
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float data type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex data type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numeric types
print(abs(gpa))  
print(abs(gpa * -1))  

print(round(gpa))  # Round to nearest integer

print(round(gpa, 1))  # Round to one decimal place

# Math module functions
print("\n--- Math Module Examples ---")
print(f"Pi value: {math.pi}")
print(f"Square root of 64: {math.sqrt(64)}")
print(f"Ceiling of {gpa}: {math.ceil(gpa)}")
print(f"Floor of {gpa}: {math.floor(gpa)}")
print("End of file reached")



