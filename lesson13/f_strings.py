person = "David"
coins = 3

print ("\n" + person + " has " + str(coins) + " coins.\n")

message = "\n%s has %d coins.\n" % (person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = f"\n{person} has {coins} coins left."
print(message)


# pass formatting options

num = 10
print(f"\n2.5 times {num} is {2.25 * num:.2f}.\n")

for num in range(1, 11):
    print(f"\n2.5 times {num} is {2.25 * num:.2f}.")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}.")




