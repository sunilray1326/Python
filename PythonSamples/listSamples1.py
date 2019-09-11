import time

# calculate start time
start = time.time()
print("\n-----------------------------------")

# Deifne list by simplying giving [] at right hand side and no need to say list
num_list = []
## initialize list from 1 to 10000, so range should be 1,10001
for num in range(1,10001):
    num_list.append(num)
# USING BUILT IN SUM() to calculate sum of integer list
print("Sum: ", sum(num_list))

## we can initialize list while declaring it itself and faster way to do it
#testList = [i for i in range(1,21)]
testList = list(range(1,21))
print(testList)

## we can even use some conditional statement while initializing it
testList1 = [i for i in range(1,21) if i % 2 == 0]
print(testList1)

## we can even use some conditional statement while initializing it
testList2 = [i1 for i in range(1,21) if i % 2 == 0 for i1 in range(1,i)]
print(testList2)

## Initializing list of 20 items with value 0
testList3 = [0]*20
print(testList3)

## Initializing list of 20 items with value 0
testList4 = [0 for i in range(20)] 
print(testList4)

## Initializing list of 20 items with value 11
testList5 = [11]*20
print(testList5)
## we can later update specific range, say out of 20 items in above list that were
## initialized to value 11, update items 4-8 with value 20
testList5[3:7] = [20]*5
print(testList5)

## how to initialize 2D list
## arr = [[0]*no_of_cols]*no_of_rows
testList6 = [[11]*2]*4
print(testList6)

## how to initialize 2D list
##arr = [[0 for i in range(no_of_cols)] for j in range(no_of_rows)]
testList7 = [[11 for i in range(2)] for i1 in range(4)]
print(testList7)

print("\n-----------------------------------\n")

stop = time.time()
print("Time taken: {}".format(stop-start))
