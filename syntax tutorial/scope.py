# a scope of a variable just means its availability to be used in different regions

# global scope
# a global variable can be used anywhere, outside functions and objects and also inside it

x = 300

print(x)

def func1():
    print(x)

func1()

# the keyword global needs to be used if the variable is defined in a function

b = 100

def func2():
    global b
    b = 50

func2()

print(b)


# local scope
# a local variable can be only be used in the function that created it

y = 17

def func3():
    y = "not 17"
    print(y)

func3()

# a local variable can also be used by functions within the function that defined the same variable

def func4():
    t = 400
    def innerfunc4():
        return t+100
    return innerfunc4()

print(func4())


# nonlocal scope
# this only works for nested functions
# a nonlocal variable is a variable which was defined in a function within a function, whose usage was expanded to the rest of the function
# the keyword nonlocal is required

def func5():
    g = 9.8 # the value of g is assigned in the first function

    def innerfunc5():
        nonlocal g # the g used in this function is the one used throughout the whole func5()
        g = 10 
    
    innerfunc5()
    return g # the value of g returned will be fromm innerfunc5()

print(func5())
    