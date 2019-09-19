"""
Multiple inheritance example and MRO

@Author Sunil Ray
"""

class B1:

    def process(self):
        print("B1 process")

class B2:
    def process(self):
        print("B2 process")

class C1(B1, B2):
    pass

class C2(C1, B2):
    def process(self):
        print("C2 Process")

## below class hirarchy will give run time error as Python is not able to
## determine MRO since 
class C3(C2,C1):
    pass

class C4(C1,B1):
    pass

objC1 = C1()
objC1.process()
print("C1 MRO ==> ", C1.mro())

objC2 = C2()
objC2.process()
print("C2 MRO ==> ", C2.mro())

objC3 = C3()
objC3.process()
print("C3 MRO ==> ", C3.mro())

objC4 = C4()
objC4.process()
print("C4 MRO ==> ", C4.mro())