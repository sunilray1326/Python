
"""
Multiple inheritance example and MRO

@Author Sunil Ray
"""

class B1:

    def process(self):
        print("B1 process")

class C1(B1):
    pass

class C2(B1):
    def process(self):
        print("C2 Process")

class C3(C1,C2):
    pass

objC1 = C3()
objC1.process()
print("C3 MRO ==> ", C1.mro())

## As per original MRO it should be
## C3 => C1 => B1 => C2 => B1 However, 