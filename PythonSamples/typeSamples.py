## working with type and id

tup1 = (1,2,3,4,5)

print("tup1 is {}".format(tup1))
print("type of tup1 is:", type(tup1))
print("----------------------------------------------------")
tup1 = (1,'two', 3, [4, 5, 'six'], 7.12)
tup2 = (1,'two', 3, [4, 5, 'six'], 7.12)
print("----------------------------------------------------")

print("tup1 is {}".format(tup1))
print("type of tup1 is:", type(tup1))
print("type of tup2 is:", type(tup2))
print("----------------------------------------------------")

print("type of tup1[1] is {} and tup1[3] is {}".format(type(tup1[1]), type(tup1[3])))
print("type of tup1[0] is {} and tup2[4] is {}".format(type(tup1[0]), type(tup1[4])))
print("----------------------------------------------------")

## id() function returns unique object identifier so id of tup1 and tup2 should be different
print("id of tup1 is", id(tup1))
print("id of tup2 is", id(tup2))
print("----------------------------------------------------")

## notice that id of all elements of tup1 and tup2 are same since Python creates 
## only one object of that value but list id is NOT same
print("id of tup1 elements are: ", id(tup1[0]), id(tup1[1]), id(tup1[2]), id(tup1[3]), id(tup1[4]))
print("id of tup2 elements are: ", id(tup2[0]), id(tup2[1]), id(tup2[2]), id(tup2[3]), id(tup2[4]))
print("----------------------------------------------------")

## use "is" to check if 2 objects are same object - same id() value
if tup1[0] is tup2[0]:
    print("both tup first element is same object")
if tup1[1] is tup2[1]:
    print("both tup second element is same object")
if tup1[3] is tup2[3]:
    print("both tup foorth element is same object")
print("----------------------------------------------------")

## to check what kind of class it is, we can use isinstance() function
if isinstance(tup1, tuple):
    print("tup1 is tuple")
if isinstance(tup1[3], list):
    print("tup1 fourth element is list")

tup1[3].append(7)
print(tup1)