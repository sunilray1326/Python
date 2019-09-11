

# creating and initializing list
x = [1, 2, 3, 4]
print(x)
print("-----------------------------------\n")

## Can change any element through index, index starts from 0 and not 1
x[1] = 5
print(x)
print('x type is', type(x))
print("-----------------------------------\n")

# if we assign value with (), then it is typle and cannot be changed
x = (1,2,3,4)
print(x)
print('x type is', type(x))
## we CANNOT modify tuple, get error -> TypeError: 'tuple' object does not support item assignment
#x[1] = 5
print("-----------------------------------\n")

## using () will initialize variable to TUPLE that is not mutuable
x = (1,2,3,4,1,2)
print(x)
print('x type is', type(x))
print("-----------------------------------\n")

## using {} will initilize variable to SET so all duplicates will be removed automatically
x = {1,2,3,4,1,2}
print(x)
print('x type is', type(x))
print("-----------------------------------\n")

listObj = list()
listObj.append("Name 1")
listObj.append("Name 2")
listObj.append("Name 3")
listObj.append("Name 4")
print("listObj is type {}".format(type(listObj)))
print("-----------------------------------\n")
print(listObj)

## When wnt to initiliaze list with values then NO NEED TO USE list keyword
## Just use [] and provide value as shown below
#listObj = list['Name 1', 'Name 2', 'Name 3', 'Name 4']
listObj2 = ['Name 1', 'Name 2', 'Name 3', 'Name 4']
print(listObj2)

listObj3 = list(['Name 1', 'Name 2', 'Name 3', 'Name 4'])
print(listObj3)
## we can access any element directly using index of position in list
print("Third elemnt is: ", listObj3[2])
print("-----------------------------------\n")

## use list() and range() to initialiaze list
list1 = list(range(4))
print("list1 is - ", list1)

## below creates dictionary
dict1 = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3', 'key4' : 'value4'}
print("list2 type is ", type(dict1))
for i,j in dict1.items():
    print("Key: ", i, "Value: ", j)
## we can modify dict type as it is mutabl
dict1["key2"] = "value10"
print(dict1)