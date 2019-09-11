

## we can initialize list while declaring it itself and faster way to do it
testList1 = [i for i in range(1,20) ]
print(testList1)

## we can even use some conditional statement while initializing it
testList2 = [i for i in range(1,20) if i % 2 == 0]
print(testList2)

## we can even use some conditional statement while initializing it
testList3 = [i1 for i in range(1,21) if i % 2 == 0 for i1 in range(1,i)]
print(testList3)
print("---------------------------------------------------------------")

print(testList1[::-1])
print(testList1[-1::])
print(testList1[::-2])
print(testList1[::])
print(testList1[1::])
## start:end:step over value
## if you want to work with reverse list, that is reading list from end and perform operation
## to read specific values, you need to use negative index for start and end position 
print(testList1[3:8:])

print("---------------------------------------------------------------")
## read list from end, starting index -12 means 12th position from end in reverse direction
## end position -16 means stop reading after 16th position from end in reverse direction
## -1 step over means move in reverse direction while reading list 
print(testList1[-3:-8:-1])
## below 2 lines output will be same due to step over direction is reverse 
## so in first case, list will count start position from end in reverse direction as -12
## in second case, list will count start position 
print(testList1[-12:-16:-1])
print(testList1[7:3:-1])
print("---------------------------------------------------------------")
print(testList1[-1::-1]) ## == print(testList[::-1])
print(testList1[-1::1])
print(testList1[::])
print(testList1[:-1:])
print(testList1[-4:-6:-1])
## when step over direction is negative means, list will ONLY work in REVERSE direction 
print("---------------------------------------------------------------")

## Operations on list
list1 = [i for i in range(1,13)]
list2 = [i for i in range(11,21)]
print("List1 - ", list1)
print("List2 - ", list2)
list3 = list1 + list2
print("List3 - ", list3)
## only + is supported for list and no other operations like - or *
#list4 = list1 - list2
#print(list4)
print("11 is present in list1 - ", 11 in list1)
print("13 is present in list1 - ", 13 in list1)
print("list1 4th to 8th elements - ", list1[3:8])
print("length ofs list1 is - ", len(list1))
print("Max of list1 is -", max(list1))
print("Min of list1 is -", min(list1))
print("Occurence of 11 in list3 is -", list3.count(11))
print("Occurence of 13 in list3 is -", list3.count(13))

## finding max value in list
key, maxVal = 0, 0
for i in list3:
    #print(i, "occuence is -", list3.count(i), "key, Max - ", key, maxVal)
    if list3.count(i) > maxVal:
        maxVal = list3.count(i)
        key = i

print(key, "occured max time", maxVal)

## use comprehension to find max occurence in list
print("---------------------------------------------------------------")
print(list3)
val = max(list3,key=list3.count)
print("The max occured element in list is: ", val, "and it occured", list3.count(val), "times")
print("---------------------------------------------------------------")

## read a string from keyboard and concery it into list
## using split(), we can convert one sentence into list of strings
## if we dont use split(), then for will iterate sentence one character at a time
## and we will get list of individual characters
msgStr = input("Enter a sentence to convert to list: ")
list4 = msgStr.split(' ')
## if we use for i in msgStr then i will be one character at a time
print(list4)
print("The max occured character in string is: ", max(list4,key=list4.count))
findStr = input("Enter search string: ")
print(findStr, "is in list?", findStr in list4)
