

# collections module
# built in modules 
# built in containers
# specialized dictionaries or tuples etc

## counter class ###############################

from collections import Counter

mylist = [1,2,1,3,2,2,3,2,'a','a','hello']
print(Counter(mylist))


st = 'aaabbbccadfadba'
print(Counter(st))

st = 'how many times a word show up in this word'

res= Counter(st.split())
print(res)

print(res.most_common())
print('\n')
print(list(res)) # list unique values
print('\n')

## default dictionary #########################

from collections import defaultdict

d = {'a':10}
print(d['a'])

# d['wrong'] # in normal dictionary when accessing wrong key it gives key error

# in default dictionary if you access a key that is not present it will assign a default value

d = defaultdict(lambda: 0) # default values will be zero
d['correct'] = 100
print(d['correct'])

print(d['wrong']) # wont give an error


#########  nametuple #####################

mytupl = (10,20,30)

mytupl[0] # returns 10 

# in certain situations you can create keys and values 

from collections import namedtuple 

dog = namedtuple('Dog',['age','breed','name'])

sammy = dog(age=5,breed='husky',name='sam')

print(type(sammy)) 

print(sammy)
print(sammy.age)
print(sammy.breed)