
# generator functions allow us to write a function that can send back a value and then later resume to pick up where it left of 

# allows us to generate a sequence of values over time 
# main difference is use of -- yield keyword

# when generator function is compiled they become a object that supports an iteration protocol 
# meaning when they are called in your code they dont actually return a value and then exit 

# instead they will suspend and resume their execution state around the last of point of value generation

# advantage is that instead of having to compute and entire series of value up front generator computes one value waits until next value is called for 

# for example range() function does produce a list in memeory instead it just keeps track of last number and the step size to provide a flow of numbers 

# next 

# iter 


def create_cubes(n):
    for x in range(n):
        yield x**3

print(list(create_cubes(10)))


#####################

def simple_gen():
    for x in range(3):
        yield x 

# for number in simple_gen():
#     print(number)

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))

############################

s = 'hello'

# for letter in s:
#     print(letter)

# you cant use next(s) --- error is string is not iterator 
# turn the string into a generator 

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))








