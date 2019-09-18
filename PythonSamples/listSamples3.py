

list1 = [i for i in range(0,10)]
print(list1)

## access list using slice - start position, end of the slice non-exclusive, and step over
print("printing list1 from first to 4th element, 0 to 3 index", list1[0:4])
print("printing list from second to 4th element with 2 step over ", list1[1:5:2])

i = list1.index(4)
print("Found 4 at index", i)

## if use below statement without try block, it is givng Valueerror at runtime
try:
    i = list1.index(12)
    print("Found 12 at index", i)
except ValueError:
    print("12 is not in list")

## append add new element at end
list1.append(11)
## inset before index
list1.insert(1,10)
print(list1)

## remove items by value
list1.remove(10)
## remove item at end by just popping it
lastElement = list1.pop()
print("Popped last item: ", lastElement)
print("The current list is ", list1)
#list1.pop(1)
## we can also remove by using del
del list1[1]
print("Removed second item from list", list1)
## we can use slice to delete speific elements from list
del list1[1:9:3]
print("Removed 1:9:3 from list using slice", list1)

## we can join list items if it is string list
list2 = ['name1', 'name2', 'name3', 'nam4']
str1 = ':'.join(list2) 
print("List items joined by :", str1)

