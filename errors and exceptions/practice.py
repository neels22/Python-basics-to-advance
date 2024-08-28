


try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('you got a type error')

######
x = 5 
y = 0

try :

    z = x/y 
except ZeroDivisionError:
    print('cant divide by zero')


######
def ask():
    while True:
        try:
            n = int(input('enter a number'))
        except :
            print('thats not a number')
        else:
            print('yes that correct')
            break

ask()