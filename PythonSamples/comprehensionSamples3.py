
## we can initialize list while declaring it itself and faster way to do it
testList1 = list(range(1,20))
testList2 = [i for i in range(1,20)]
#[i for i in range(1,20) ]
print("List1 => ", testList1)
print("List2 => ", testList2)

## create a list of tuple 
testList3 = [(i, i**2) for i in range(1,10)]
print("List3 =>  ", testList3)
print("List3 3rd element => ", testList3[2])
print("List3 tuple first element => ", testList3[2][0])
print("List3 tuple second element", testList3[2][1])
try:
    testList3[2][1] = 12
except TypeError:
    print("\n**** WARNING : We cannnot modify tuple ****\n")

## we can even use some conditional statement while initializing it
testList1 = [i for i in range(1,20) if i % 2 == 0]
print("List1 =>  ", testList1)

testList1 = [i1 for i in range(1,20) if i % 2 == 0 for i1 in range(i, i+2)]
print("List1 => ", testList1)
print("---------------------------------------------------------------")

str1 = "I am test sentence"
## below string include one space before a and it is used to match with a space inside any other string
str2 = " aeiou"
list1 = [i for i in str1 if i not in str2]
set1 = {i for i in str1 if i not in str2}
print("List1 => ", list1)
print("Set1 => ", set1)
print("---------------------------------------------------------------")

list1 = {i for i in range(1,21)}
list2 = {i for i in range(11,31)}
print("List1 => ", list1)
print("List2 => ", list2)
list3 = [i for i in list1 if i not in list2]
list4 = [i for i in list1 if i in list2]
print("List3 => ", list3)
print("List4 => ", list4)
