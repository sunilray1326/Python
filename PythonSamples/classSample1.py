"""
class sample code 
author @Sunil Ray
"""

class empl:

    department = "Development"

    ## the __init__ is constructor
    def __init__(self, **kwargs):
        ## two underscore __ makes a variable private and can only be read/write through class methods
        ## one underscore _ in variable name makes it protected, can be accessed directly within a module
        self.__name = kwargs['name'] if 'name' in kwargs else "John Doe"
        self.__age = kwargs['age']
        ## we can even assign default values to these variables
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

    def print_empl(self):
        print("Name: {} Age: {}  Department: {}".format(self.__name, self.__age, self.department))


obj1 = empl(name="Swamy", age=35)
obj2 = empl(age=30, name="Navdeep")
dict1 = {"name" : "Ashish", "age" : 45}
## if we have dict type with same parameters then we can pass it as parameter with dereferencing **
obj3 = empl(**dict1)

print("\n**********************************************")
obj1.print_empl()
obj2.print_empl()
obj3.print_empl()
print("**********************************************\n")

## we can access department directly withjout 
print("obj1 Department: ", obj1.department)
print("obj2 Department: ", obj2.department)
## but we cannot access __ private variable directly
## it will throw AttributeError during runt time
try:
    print("obj2 Department: ", obj2.__name)
except AttributeError:
    print("\n**** EXCEPTION - Caught AttributeError, object doesn't have such attribute ****\n")



