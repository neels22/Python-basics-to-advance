

# special methods allow to use built operations in python such as length function or print function with our own user created objects

mylist= [1,2,3]
len(mylist)

# what if i want to check length of my own object??

class sample():
    pass 
mysample = sample()

# len(mysample) ### gives error

##########################

# 

class Book():

    def __init__(self,name,author,pages):

        self.name = name 
        self.author = author 
        self.pages = pages

    def __str__(self):
        return f" {self.name} and author is {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print('a book has been deleted')

mybook = Book('harry' ,'neel' , 200)

print(mybook)                   # this will use overide str method
res= len(mybook)                # this will use overidden len method
print(res)                      
del(mybook)                     # this will use overidden del method