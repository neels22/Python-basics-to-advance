

# arguments and keyword arguments 
# arbitraty number of arguments and keyword arguments

# positional arguments 
def myfunc(a,b):
    return sum((a,b))*0.05
print(myfunc(40,60))

# when we need to take arbritrary number of arguments 
def myfunc(*args):
    return sum((args))*0.05
print(myfunc(40,60,34,34,54,24,4,4,45,34))
# we can give as many numbers as we want

# args is basically a tuple 
def myfunc(*args):
    print(args)
print(myfunc('adf',234,'asdf'))

# techinically args can be replaces with any keyword 
def myfunc(*spam):
    print(spam)
# but by convention always use args

# loop through args
def myfucn(*args):
    for item in args:
        print(item)
print(myfucn(234,345,234,234,2))

# **kwargs
def myf(**kwargs):
    if 'fruit' in kwargs:
        print('my  fav fruit is {}'.format(kwargs['fruit']))
    else:
        print("couldnt find any fruit")
print(myf(fruit="veggie",veg='apple'))
# kwargs will return a dictionary 

# you have to give arguments first and keywords after than you cant change order and you can add args after kwargs
def myf(*args, **kwargs):
    print(args)
    print(kwargs)
    print('i would like {} {}'.format(args[0],kwargs['food']))
print(myf( 10,11,12, fruit='apple', food='eggs'  ))
