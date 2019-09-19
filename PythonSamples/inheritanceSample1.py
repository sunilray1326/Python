"""
Created on Wed Aug 28 17:05:27 2019

@author: Sunil_Ray
"""

class baseClass1():
    
    def methodOne(self):
        print("Inside baseClass1 methodOne")
    
    def methodTwo(self, string):
        print("\nInside baseClass1 methodTwo and string is" + string)
    
    def methodThree(self):
        print("\n Inside baseClass1 methodThree")
    
    ## we need to pass "self" to all class methods since Python passes refernece to 
    ## to object while calling method. Otherwise you will get error like
    ## "method takes 0 positional arguments but 1 was given" - Python will pass "self" to method so 
    ## it will expect to have "self" parameter for all methods

class baseClass2():
    
    def methodOne(self):
        print("Inside baseClass2 methodOne")
    
    def methodThree(self):
        print("\n Inside baseClass2 methodThree")

    def methodFour(slef):
        print("\nInside baseClass2 methodFour")

# Ceating child class from base class
class childClass(baseClass2, baseClass1):
    
    def methodOne(self):
        print("\nInside childClass methodOne")
        # how to call baseClass1 method from child class
        # Note that we are using Class Name to call its method
        # we have call both parent class method explicity 
        baseClass1.methodOne(self)
        baseClass2.methodOne(self)
    
    def methodTwo(self, string):
        print("\nInside childClass methodTwo and string is" + string)


def main():
    obj1 = baseClass1()
    obj1.methodOne()
    obj1.methodTwo("message string here")
    
    obj2 = childClass()
    obj2.methodOne()
    obj2.methodTwo("another message srting here")
    ## will call baseClass2 methodThree even methodThree present in baseClass1 and baseClass2
    ## First search method in child class, if not then start searching in base classes in same
    ## order defined during class declarition - childClass(baseClass2, baseClass1)
    ## so first search in baseClass2 and if not found then search in baseClass1
    ## Please note that even though methodThree present in baseClass1, it will NOT be called
    obj2.methodThree()
    obj2.methodFour()
    
    print("ChildClass MRO => ", childClass.mro())

if __name__ == "__main__":
    main()