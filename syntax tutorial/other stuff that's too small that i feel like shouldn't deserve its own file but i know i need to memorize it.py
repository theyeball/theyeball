# f strings

weight = "2 kg"
height = "73 cm"

# instead of writing
print("im", height, "tall and i weigh", weight)

# you could simply write
print(f"im {height} tall and i weigh {weight}")

# f strings just makes it easier to see and also so that you don't have to worry about spacing



# iterating a dictionary
# if you use a for loop on a dictionary, the changing variable will be set to the keys of dictionary, NOT the values.

dict1 = {
    "ligma":"balls",
    90:17,
    "ministry":"of edu"
}

for i in dict1:
    print(i) # this will print ligma, 90, ministry



# dictionaries cannot have duplicate keys, which means that turning a list into a set of keys for a dictionaries will remove all of its duplicate elements.