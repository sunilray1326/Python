#
# Function and loop examples
#

# just to print message
def fun1():
    print("I am fun1")

# calculate power of given number, if no power given then default to 1
# the dafault value parameters must come after all non-default parameters
def power(num, pw=1):
    print("\nInside power() function")
    result = 1
    
    # If only one range is given then range starts from 0
    # For example range(4) means 0 to 4 and loop will iterate through 0 to 3
    print("Given power is", range(pw))
    
    for i in range(pw):
        #print(i)
        result = result * num
    return result

# Add multiple numbers passed and return result
def add(*num):
    print("\nInside add function")
    print(num)
    result = 0
    
    # the for loop works as iterator and iterate through each value in list
    for i in num:
        #print(i)
        result = result + i
    return result

# we can pass variable argumemts to function but it shuold be last parameter
# we can either pass one value or none to this parameter and it works
def add_multi(num1, num2, *args):
    print("\ninside add_multi() function")
    # while printing string and number, we need to convert number to string
    print("num1:", str(num1), "num2:", str(num2), "*args:", str(args))
    
    result = num1 + num2
    
    # If there is no value in list, the loop will not execute
    # Even if value is 0 in case it is number, loop will execute
    # for (0,0,0,0) as values, loop will execute 4 times
    for i in args:
        print(i)
        result = result + i
    return result

def whileTest(num, pw):
    print("\ninside whileTest function")
    result = 1;
    while (pw >= 1):
        #print(pw)
        result = result * num
        pw = pw - 1
    return result

# will print mesasge inside fun1()
fun1()

# fun1() will print message and print() will print "none" since function doesnt
# return any value
print(fun1())
print(fun1)

print(power(2))
print(power(2,4))

print("Result of add() => {}".format(add()))
print("Result of add(2,3) => {}".format(add(2,3)))
print("Result of add(4,5,6) => {}".format(add(4,5,6)))
print("Result of add(7,8,9,10) => {}".format(add(7,8,9,10)))

print(add_multi(9,8,7))
print(add_multi(9,8,7,6))
# even if we don't pass any value to *args parameter, it still works
print(add_multi(9,8))
print(add_multi(9,8,0))
print(add_multi(9,8,0,0,0,0))

print(whileTest(4,3))

# see how range() works
print("\nrunnig range() function with for loop")
for i in range(4,8):
    print(i)

#using the enumerate() function to get index
print("\nlist to iterate for \"for loop\"")
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

# enumerate function returns object stored in memory and not any readable value
#print(enumerate(days))
for index, day in enumerate(days):
    print (index, day)
# We can also access list using index as show below
# so if we have any number available, we can use that as idex to get value from list
print("\naccessing days[] using index")
print(days[2])