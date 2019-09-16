

def fun():
    print("I am fun()")

## since everything is an object in Python, we can assign function name itself to a variable
## and then call function using that variable as shown below we are calling fun1() using funVar variable
funVar = fun ## adress of fun() is passed to funVar here so we can call function using this variable
funVar()

def outerFunction():
    print("I am outer function")
    def innerFunction():
        print("I am inner function")
    return innerFunction

print("---------------")
## this will only execute outerFunction() and will not get into innterFunction()
## howwverm outerFuntion() returns innerFunction() address so we can call innerFunction()
## using returned value stored in var2
var1 = outerFunction()  ## the return value of function is passed to variable so we can call inner using it
print("---------------")
var1()
print("---------------")

## we can use decorator for function as well
def fun1(f):
    print("Inside fun1()")
    def fun2():
        print("Inside inner fun2()")
        #print("Before calling external function")
        f()
        #print("After calling external function")
    print("fun2 adress is: ", fun2)
    return fun2
    
print("---------------")

def fun3():
    print("****Inside external fun3()")

def fun4():
    print("####Inside external fun4()")

var2 = fun1(fun3)
print("fun1 adress is: ", fun1)
print("Var2 adress is: ", var2)
var2()

var3 = fun1(fun4)
print("fun1 adress is: ", fun1)
print("Var2 adress is: ", var3)
var3()
var2()


## we can simply over write fun3 adress with fun2() adress that is returned by fun1()
# fun3 = fun1(fun3)
# fun3()


