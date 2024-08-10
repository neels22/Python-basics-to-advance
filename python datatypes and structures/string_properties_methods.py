

# immutability of strings

name = 'sam'
# name[0] = 'p'   ## --> gives an error

### how to do it then? ----> using concatenation 

last_letters = name[1:]
print('P' + last_letters)

#################
# more use cases - concatenation

x= "helo"
x = x+ " this is hello"
print(x)
 
##

print("zz"*10)

#################

# errors 
# '2' + 3  

##

'2' + '3' # --> '23'

#################

# attributs and methods available on string

x = "hello world"

print(x.upper()) # doesnt affect origianl string for that youll need to re-assign

print(x.lower())

print(x.split()) # this creates a list of the string based on the para you pass in default is white space

print(x.split('l'))

#################

