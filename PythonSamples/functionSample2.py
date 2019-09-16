## How mutuable type data can be changed inside a function() and that will change value
## of passed paramter. How to avoid this side effect for mutuable data types

def main():
    intVal1 = 4
    intVal2 = 5
    print("The intVal1 id before calling add() is    {}".format(id(intVal1)))
    intVal3 = addNumber(intVal1, intVal2)
    print("The intVal1 id after calling addNumber() is     {}".format(id(intVal1)))
    print("the addNumber() result is {}".format(intVal3))
    ## so we can see that even if we change the value of parameter in called function
    ## the value of passed parameter is NOT changed in Python so it is call by value
    ## however, if we pass list data that is mutubale then changing the list items
    ## inside add() function will also change list that was passed from main() here
    ## this indictaes that if we pass mutuable type data to function, it will change 
    ## if it was operated inside function

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print("list1 before calling addList() function is {}".format(list1))
    list3 = addList(list1, list2)
    ## since list1 items are changed inside addList(), it will also reflact changes here in main
    print("list1 after calling addList() function is  {}".format(list1))
    print("The addList() result is {}".format(list3))

    l4 = ['a', 'b', 'c']
    l5 = ['d', 'e', 'f']
    print("l4 before calling addList() function is {}".format(l4))
    l6 = addList(list(l4), list(l5))
    ## we created a new list using l4 and passed that to addList fucntion
    ## so any change inside addList() will not impact l4 now
    print("l4 after calling addList() function is {}".format(l4))


def addNumber(data1, data2):
    result = data1 + data2
    print("the data1 id before changing its value is {}".format(id(data1)))
    data1 = 8
    data2 = 9
    print("the data1 id after changing its value is  {}".format(id(data1)))
    return result


def addList(data1, data2):
    result = data1 + data2
    print("the data1 before changing its value is {}".format(data1))
    data1[0] = 7; data1[1] = 8; data1[2] = 9
    print("the data1 after changing its value is  {}".format(data1))
    return result

if __name__ == "__main__": main()