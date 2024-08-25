
# self is just a convention for representing instance of object itself
#  Attributes are characteristics of objects


class Dog():

    species = 'mammal' # class object attribute
    # same for any instance of a class
    # 
    
    def __init__(self,breed,name,spots): # special constructor method whenever instance is created 

        # Attributes are characteristics of objects
        # we take in the arguments
        # assign it using self.attribute_name
        # self keywords represents instance of the object itself
        # by convention parameter name and attribute name should be same
        self.breed = breed 
        self.name = name 
        self.spots = spots   

    # methods are actions that can utilize class attributes 
    # methods needs to be executed
    # 
    def bark(self, age):
        print(f'woof my name is {self.name} and age is {age} ')





my_dog = Dog('pug','browny',True)

print(type(my_dog))

print(my_dog.breed) 
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)

my_dog.bark(12)



##########################################
class Circle():
    PI = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area= radius*radius*self.PI

    #methods

    def get_circumference(self):
        return self.radius* self.PI*2
    

my_circle = Circle(5)

print(my_circle.radius)
print(my_circle.area)
res = my_circle.get_circumference()
print('circumference is '+str(res))
