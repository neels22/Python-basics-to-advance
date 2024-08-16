
# use print statements inside functions for debugging

# with and without parenthesis 
def say():
    print('hello')
    print('neel')
say()
print(say)

# provide some default value 
def say_hello(name ='nelay' ):
    print(f"hello {name}")
say_hello("neel")
say_hello()

# returning a result 
def add_num(num1,num2):
    return num1 + num2
addition = add_num(10,20)
print(addition)





