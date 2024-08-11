


# mappings of key and value pairs 
# unordered 
# no need to know index location just use key and grab the value
# they cannot be sorted 
# 


#################

my_dictionary = {"key1":'hello',"key2":'hi'}
print(my_dictionary)

# using keys to get values
print(my_dictionary['key1'])
print(my_dictionary['key2'])

###
prices_lookup = {'apples':2.99,'oranges':1.99,'milk':5.80}
print(prices_lookup['apples'])

# nested dict
d= {'k1':123,'k2':[0,1,2],'k3':{'inside':100}}
print(d['k2'][2])
print(d['k3']['inside'])

##########################
d = {'k1':['a','b','c']}
mylist = d['k1']
print(mylist)
letter = mylist[2]
print(letter)
print(letter.upper())

print(d['k1'][2].upper()) ### everything the avobe few lines into one line 
##########################

# adding new value
d = {'k1':23}
d['k4'] = 23
print(d)

# update value of key 
d['k1']= 'new value'
print(d)

###################

print(d.values())
print(d.keys())
print(d.items())

###################
