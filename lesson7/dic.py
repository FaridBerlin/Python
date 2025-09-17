# Dictionary
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Acces items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())
# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify if key exists
print("vocals" in band)
print("drums" in band)

# changing values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# removing items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

# delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# copying dictionaries

# just a Bad copy....create a reference
# band3 = band 
# print("Bad copy")
# print(band3)
# print(band)

# band3["durms"] = "Bob"
# print(band)

# Good copy
band2 = band.copy()
band2["drums"] = "Bob"
print("Good copy")
print(band)
print(band2)

# or use the dict constructor
band3 = dict(band)
band3["drums"] = "Bonham"
print("Good copy")
print(band3)
print(band)

# Nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals",
}

member2 = {
    "name": "Page",
    "instrument": "guitar",
}

band = {
    "member1": member1,
    "member2": member2,
}
print(band)
print(band["member1"]["name"])

# Sts

nums = { 1, 2, 3, 4 }

nums2 = set([1, 2, 3, 4])

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums)  # Output will be {1, 2, 3}

nums = {1,True, 2, False, 3, 4,0}
print(nums)  # Output will be {0, 1, 2, 3, 4} since True is treated as 1 and False as 0

print(2 in nums)  # True


# Adding elements
nums.add(8)
print(nums)  # Output will be {0, 1, 2, 3, 4, 8}

morenums = {5, 6, 7, 8}
nums.update(morenums)
print(nums)  

# Merging sets
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)  # Output will be {1, 2, 3,

one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)  # Output will be {2, 3}

one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)  # Output will be {1, 4}