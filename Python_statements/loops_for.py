
# many objects are iterable and we can use loops to iterate over them 
# such as lists or strings or dictionary, tuple etc
# avoid using list as a variable name
# use _ underscore when you dont want to use that variable 

# using variable on list 
my_iterable = [1,2,3,'adf',34]
for item in my_iterable:
    print(item)
    print('hello')

# printing only even numbers
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    if num % 2 ==0:
        print(num)
    else:
        print(f"its odd number: {num}")
    
# sum of the all elements in list
listsum = 0
for num in mylist:
    listsum += num
print(listsum)

# string iteration
for letter in 'hello world':
    print(letter)

# use _ underscore when you dont want to use that variable 
for _ in 'hiiiii':
    print('no variabble used')

###############

# iteration on tuple 
tup = (1,2,3)
for item in tup:
    print(item)

###############

# special quality --- tuple unpacking 
mylist2 = [(1,2), (3,4) , (5,6)]
len(mylist2)
for item in mylist2:
    print(item)

# below is tuple unpacking 
for a,b in mylist2:
    print(a)
    print(b)

###############

# dictionaries 

d = {'k1':1 , 'k2':2, 'k3':3}

# items 
for item in d.items():
    print(item)

# only keys
for key in d:
    print(key)

# only values
for value in d.values():
    print(value)

# key and value ---- using dict unpacking or similar to tuple unpacking
for key,value in d:
    print(value)

###############











