

# decorators allow you to decorate a function

# want to add some new funcionality but keep the old also
# want to add or delete functionality anytime 

# @some_decorator --- you can just delete this line to remove that functionality
# def funct()return 

# calling function within another function

# you can return a function from inside a function
def cool():
    def super_cool():
        print( 'hey')
    return super_cool
new_f = cool()
new_f()


# you can pass a function as an argument to a function

def hello():
    return 'hi hello'

def other(some_func):
    print('other function')
    print(some_func())

other(hello)

###############################

# decorator ---

def new_decorator(original_function):
    
    def wrap_func():
        
        print('some extra code before original function')
        original_function()

        print('some extra code after original function')

    return wrap_func

def func_needs_decorator():
    print('i want to be decorated')


# this is one way to decorate a function 
wrapped = new_decorator(func_needs_decorator)
wrapped()

print('\n'*2)

# this is recommended way and easy way 

@new_decorator     # --------- you can comment to turn off 
def func_needs_decorator():    # basically what we did above like passing the function same this @ does 
    print('i want to be decorated')

func_needs_decorator()

