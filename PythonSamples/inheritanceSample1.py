# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:05:27 2019

@author: Sunil_Ray
"""

class baseClass():
    def methodOne(self):
        print("\nInside baseClass methodOne")
    def methodTwo(self, string):
        print("\nInside baseClass methodTwo and string is" + string)

# ceating child class from base class
class childClass(baseClass):
    def methodOne(self):
        print("\nInside childClass methodOne")
        # how to call baseClass method from child class
        # Note that we are using Class Name to call its method
        baseClass.methodOne(self)
    def methodTwo(self, string):
        print("\nInside childClass methodTwo and string is" + string)

def main():
    obj1 = baseClass()
    obj1.methodOne()
    obj1.methodTwo("message string here")
    
    obj2 = childClass()
    obj2.methodOne()
    obj2.methodTwo("another message srting here")
    
if __name__ == "__main__":
    main()