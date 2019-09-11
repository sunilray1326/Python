
# import a module from Python library
import platform

print("-----------------------------------\n")
print("Python Compiler: ", platform.python_compiler())
print("Python Version: ", platform.python_version())
print("Platform OS details: ", platform.os)
print("-----------------------------------\n")

# IN PYTHON, EVERYTHING IS OBJECT SO WE CAN CALL FUNCTION ON THAT
# we are calling upper() and lower() directly on string
# Print is not a function and string is not object in Python 2
print("hello world".upper())
print("HELLO WORLD".lower())
print("HELLO WORLD".capitalize())

# all functions in Python return value, if no return statement then it return None
def testFunction():
    valueThree = 0
    print("Inside testFunction with {} return statement".format(valueThree))

## can test None return type for function 
if (None == testFunction()):
    print("testFunction returned None")

# {} is used as placeholder for string object and we are calling
version = "3.7.3"
lang = "Python"
# we can use as may placeholder {} as we want to print variable values
print('I am {} {}'.format(lang,version))

msg = 'I am Python 3.7.3'
# in Python f is used to call format function so we can use it with placeholder {} 
print(f'hello world, {msg}')

# Function, objects, and module define scope of variable but not block like If block
# valueOne variable scope is same as outside If block below so we can access it outside If block
# But if valueOne was defined inside function, object or module, then cannot access it outside function/module/object
x = 10
y = 20
if(x <y):
    valueOne = 30
else:
    valueTwo = 40

# Even though valueOne defined inside If block, it can be accessed outside If block
print('variable valueOne defined inside If block above but can read outside {}'.format(valueOne))

# Below line will execution error - NameError: name 'valueThree' is not defined
#print('cannot read variable defined inside testFunction'.format(valueThree))

if(x<y):
    print('X {} is less than Y {}'.format(x,y))
elif(x>y):
    print('X {} is greater than Y {}'.format(x,y))
else:
    print('X {} is equal to Y {}'.format(x,y))

print("X is type {}".format(type(x)))

## we can use place holder {} while creating string as shown below
x = 8
y = 9
msg = 'Seven {} {}'.format(x,y)
print(msg)

## we can use f formatter from 3.6 onwards and no need for format() call
msg1 = f'Seven {x} {y}'
print(msg1)