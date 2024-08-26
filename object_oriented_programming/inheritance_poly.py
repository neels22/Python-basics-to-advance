

class Animal():
    def __init__(self):
        print('animal created')

    def WhoamI(self):
        print('i am an animal')

    def eat(self):
        print('I am eating')


myanimal = Animal()
myanimal.eat()


# Inheritance 


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self) # creating instance of animal class as well
        print('dog created')

    def eat(self): # overwriting the eat function
        print('i am a dog who eats')
    def WhoamI(self):
        print('i am a dog')

mydog = Dog()
mydog.eat()
mydog.WhoamI()



##############################################

# Polymorphism 

print('\n'*2)
class Dog():
    def __init__(self,name):
        self.name = name 

    def speak(self):
        return self.name + ' woof'
    

class Cat():
    def __init__(self,name):
        self.name = name 

    def speak(self):
        return self.name + ' Meow'
    

mydog = Dog('nico')
mycat = Cat('felix')

print(mydog.speak())
print(mycat.speak())

# different objects but same method call 

for pet in [mydog,mycat]:
    print(type(pet))
    print(pet.speak())


# passing the object to the function
# leverage the capability 

def pet_speak(pet):
    print(pet.speak())

print('\n')
pet_speak(mydog)
pet_speak(mycat)




############################

# abstract classes designed to only serve as a base class and instanctiated
# only exist to create a blueprint 
# below its 
# expecting you to inherit the animal class and overwrite the speak method 

class Animal():
     
    def __init__(self,name):
        self.name = name 
    
    def speak(self):
        raise NotImplementedError('subclass must implement this abstract method')

# myanimal = Animal('fred') # gives error 
# myanimal.speak() # gives error

class dogged(Animal):
    def speak(self):
        return self.name + ' says woof'
    
mydogy = dogged('fido')
print(
mydogy.speak())

# abstract classes could be a base class for opening files 
# classes that inherit the same method name the .open name 
