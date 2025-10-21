# can have 1, 2 or 3 parameters
# each has a different use case

# 1 parameter (0 to a number)
# range(x) = [0,1,2,...,x-1]
# note: range(x) has x elements
for i in range(3):
    print("goobiegoo")

# 2 parameters (start to end)
# range(x,y) = x,x+1,...,y-1
# note: this range of numbers includes x but does not include y
    # essentially this is just x to y-1
for i in range(34,36):
    print(i)

# 3 parameters (start to end with steps)
# range(x,y,z) = x,x+z,...y-something
# note: similar to using 2 parameters, y is not included
for i in range (0,7,2):
    print(i)

# p.s.
    # when you try to print a range with the list of numbers, then you have to include list(range(x,y)) to show it.
print(list(range(0,3)))