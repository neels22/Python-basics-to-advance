import math

# help(math)

value = 4.35

print(math.floor(value))
print(math.ceil(value))
print(round(value))

print(round(5.5)) # why is this going up -- reason overtime rounding down or up affect your final result they will be lesser or higher 
print(round(4.5)) # why is this going down -- EVEN or ODD is used 


from math import pi  

print(pi)

print(math.e) # 
print(math.inf) # infinity
print(math.nan) # not a number  


# logarithmic values 

print(math.log(100,10)) # number and base 10**2 - 100

print(math.sin(10))
print(math.degrees(pi/2))
print(math.radians(180)) 


################################################

# psuedo random number generators 

import random

res = random.randint(0,100) # return some random integer between 0 to 100
print(res)

# seed - setting a seed for a sequence random integers


############################ 
mylist  = list(range(0,20))
print(mylist)


print(random.choice(mylist))
# sample with replacement
# print(random.choice(population = mylist,k=10))
# sample without replacement 
# print(random.sample(population=mylist,k=10))

random.shuffle(mylist)
print(mylist)


# random distrubutions

print(random.uniform(a=0,b = 100))

print(random.gauss(mu=0,sigma=1))