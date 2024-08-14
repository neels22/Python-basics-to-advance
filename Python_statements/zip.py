


# zip together two or more lists and maps them 
# works till the length of shortest list  and ignores the extra 
# returns a list of tuples 
# we can unpack those tuples 

mylist = [1,2,3]
myl = [23,'adsf',234,'hello']

for item in zip(mylist,myl):
    print(item)

#below is the output we can also unpack it
# (1, 23)
# (2, 'adsf')
# (3, 234)

list(zip(myl,mylist)) # will return a list of tuples
