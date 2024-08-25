
# self is just a convention for representing instance of object itself
#  Attributes are characteristics of objects


class Dog():
    
    def __init__(self,breed,name,spots): # special constructor method whenever instance is created 

        # Attributes are characteristics of objects
        # we take in the arguments
        # assign it using self.attribute_name
        # self keywords represents instance of the object itself
        # by convention parameter name and attribute name should be same
        self.breed = breed 
        self.name = name 
        self.spots = spots   





my_dog = Dog('pug','browny',True)

print(type(my_dog))

print(my_dog.breed) 
print(my_dog.name)
print(my_dog.spots)
