

def fun():
    print("I am fun()")

## since everything is an object in Python, we can assign function name itself to a variable
## and then call function using that variable as shown below we are calling fun1() using funVar variable
funVar = fun ## adress of fun() is passed to funVar here so we can call function using this variable
funVar()
print("---------------")

def outerFunction():
    print("I am outer function")
    def innerFunction():
        print("I am inner function")
    return innerFunction

## this will only execute outerFunction() and will not get into innterFunction()
## howwverm outerFuntion() returns innerFunction() address so we can call innerFunction()
## using returned value stored in var2
var1 = outerFunction()  ## the return value of function is passed to variable so we can call inner using it
var1()
print("---------------")

## we can pass function itself as paremeter to another function and use that to call back
def fun1(f):
    print("Inside fun1()")
    def fun2():
        print("Inside inner fun2()")
        #print("Before calling external function")
        f()
        #print("After calling external function")
    print("fun2 adress is: ", fun2)
    return fun2
    
def fun3():
    print("****Inside external fun3()")

def fun4():
    print("####Inside external fun4()")

## when we call fun1(f) and pass a function as parameter, Python genertaes new adress for fun2() and keep f value avaiable
## when we call fun(f) with another function parameter, it genertaes new address for fun2() with f value available to it
## so we can call fun1(f) with many functions and for every call, Python will keep fun2() with passed f function adress
## so it can call back those functions
var2 = fun1(fun3)
var3 = fun1(fun4)
print("fun1 adress is: ", fun1)
print("Var2 adress is: ", var2)
print("Var3 adress is: ", var3)
print("---------------")
print("Calling fun2() using var2")
var2()
print("calling fun2() using var3")
var3()
print("---------------")

## we can simply over write fun3() itself with fun2() adress that is returned by fun1(f) call
print("calling fun2() usinf fun3()")
fun3 = fun1(fun3)
fun3()
print("---------------")
print("calling fun2() usinf fun4()")
fun4 = fun1(fun4)
fun4()
print("---------------")


## we can use decorator for function as well to simply avoid saying fun3 = fun1(fun3) kind of assignment
## this makes decorator handy for this purpose, please note that whenever @f1 is declared and
## followed by another funcion declarion, the f1(f) will be called automatically so we do not need to
## call it explictly
def f1(f):
    print("Inside f1()")
    def f2():
        print("Inside inner f2()")
        #print("Before calling external function")
        f()
        #print("After calling external function")
    print("f2 adress is: ", f2)
    return f2

@f1    
def f3():
    print("****Inside external f3()")

@f1
def f4():
    print("####Inside external f4()")

print("calling f2() usinf f3()")
f3()
print("calling f2() usinf f4()")
f4()