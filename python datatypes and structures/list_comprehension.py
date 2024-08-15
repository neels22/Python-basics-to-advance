

mystring = "hello"
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

# using list comprehension we can reduce the above code like this
mylist = [letter for letter in mylist]
print(mylist)

mylist = [x for x in 'word']
print(mylist)

mylist = [num for num in range(0,11)]
print(mylist)

mylist = [num**2 for num in range(0,11)]
print(mylist)

# using if else 
mylist = [x for x in range(0,11) if x%2==0]
print(mylist)

# order changes when else is involved 
mylist = [ x if x%2==0 else 'odd' for x in range(0,11)]
print(mylist)

celcius = [10,20,30,40]
farenhiet = [ ((9/5)*temp +32) for temp in celcius ]
print(farenhiet)

# nested loops
mylist = []
for x in [1,2,3]:
    for y in [10,20,30]:
        mylist.append(x*y)
print(mylist)

mylist = [x*y for x in [1,2,3] for y in [10,20,30]]
print(mylist)
