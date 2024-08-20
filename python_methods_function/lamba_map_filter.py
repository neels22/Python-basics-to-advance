
# map takes a function and a iterable 
# map will execute the function on every element of the list

def square(num):
    return num**2
my_list = [1,2,3,4,5]
for item in map(square,my_list):
    print(item)
res= list(map(square,my_list))
print(res)

def splicer(mystring):
    if len(mystring) %2 ==0:
        return 'Even'
    else:
        return mystring[0]
names = ['neel','neelay','evenl']
res=list(map(splicer,names))
print(res)

############

# filter function 
# filter will return only elements that satisfy the condition
# has to return true or false

def check_even(num):
    return num%2 ==0
li = [1,2,3,4,5,6]
res=list(filter(check_even,li))
print(res)
for n in filter(check_even,li):
    print(n)

############

# lambda expression is anonymous function 
# you can use them in conjunction with map and filter 
# 

def square(num):
    return num ** 2
res = square(9)
print(res)

res = lambda num:num**2
print(res(9))

res=list(map(lambda num:num**2,li))
print(res)

res=list(filter(lambda num: num%2 == 0,li))
print(res)

res= list(map(lambda x:x[0],names))
print(res)