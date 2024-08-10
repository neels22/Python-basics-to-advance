


# string interpolation 
# injecting a variable into a string 

#ways to do it
# 1. .format method
# 2. f-string()


###############  .format method

print('this is a string {}'.format("INSERTED")) 

print('the {} {} {}'.format("Fox","Brown" , "quick")) 
# order is maintained

# you can change it using indexing 
print('the {2} {1} {0}'.format("Fox","Brown" , "quick"))

# you can also assign keywords 
print('the {q} {b} {f}'.format(f="fox",b="brown",q="quick"))



############### 

# float formatting using .format

result = 100/777
print("the result was {r:1.3f}".format(r=result))
print("the result was {r:10.3f}".format(r=result)) # 10 just adds white space



############### f-strings method
# directly inject into strings 

name = 'jose'
print( f'hello his name is {name}' )

age = 3 

print(f"name is {name} and age is: {age}")








