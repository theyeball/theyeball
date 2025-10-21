# before getting into the math module, it's important to note that python already has some functions involving it

# min() and max()
# these can find the maximum and minimum value in an iterable
# of course, all elements of the list must be numbers for it work

list1 = [1,2,3,4.2]
print(min(list1),max(list1))

# abs()
# absolute value of a number
print(abs(3))
print(abs(-1))

# pow(a,b)
# power function, essentially (a^b)
print(pow(3,4))
print(pow(1,100))


import math
# the math module can do some other math stuff

# math.sqrt()
# square root of a number, where it can't be negative of course
# output will be in float
print(math.sqrt(121))
print(int(math.sqrt(64)))

# math.ceil() and math.floor()
# ceiling and floor function
print(math.ceil(1.4))
print(math.floor(1.4))

# constants
constants = (
    math.e,
    math.pi,
    math.tau, # essentially pi*2
    math.inf, # number close to infinity
    math.nan # not a number
)

