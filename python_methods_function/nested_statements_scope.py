



x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

#####################
# how does python know which variable assignement i am refereing to 

# scope 
# legb rule format --- local function , enclosing function locals (funciton) inner to outer, global (module) , built in 

# local
lambda num:num**2 # here num is local to this lambda function

# enclosing
name = 'this is outside ' # global
def greet():
    name = 'samay' # enclosing

    def hello():
        name = "i am a local " # local 
        print('heelo' + name)

    hello()
print(greet())
# hello will look at local 
# here hello will  look at the enclosing function containing the name 
# then if it doent have the name then it looks globally 

###########################

x = 25

def printer(x):
    print(f'x is {x}')
    # local reassignment 
    x= 200
    print(f'i just locally changed x to {x}')

print(printer(x))
print(x)

#############################

# global keyword -- not to use at beginner level 
# accidentally might overwrite this global assignment 

x = 25

def printer():
    global x
    print(f'x is {x}')
    # local reassignment on a glocal variable
    x= 'new value'
    print(f'i just locally changed global x to {x}')

print(printer())
print(x)












