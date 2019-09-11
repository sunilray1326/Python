
from os import path

# check if file exists then open in append mode
if path.exists("TestFile.txt"):
    print("\nFile exists so opening in append mode")
    file = open("TestFile.txt", "a+")
else:
    print("\nFile doesn't exist so creaitng it")
    file = open("TestFile.txt", "w+")

# write some lines in file
for i in range(10):
    # THe \n at end of file ensures that next write is to new line
    file.write("This is line number %d\n" % (i+1))

file.close()

#THIS READ ENTIRE FILE WITHOUT READING LINES
file = open("TestFile.txt", "r")
if file.mode == "r":
    print("\nNumber of lines in file %d\n" % len(file.readlines()))
    # RESET THE FILE TO START SINCE ABOVE readlines moved it to last
    file.seek(0)
    ## we can simply use file handler directly to read line by line
    for line in file:
        # TO FOCRE print NOT TO PRINT NEW LINE CHARACTER AT NEXT LINE 
        print(line, end = '')
        #RINT LENGTH OF LINE, REDUCE 1 since \n is also counted in length
        print("Number of character in line %d\n" % (len(line)-1))
file.close()

# THIS READ ONE CHARACTER AT A TIME FROM LINE
file = open("TestFile.txt", "r")
if file.mode == "r":
    line = file.readline()
    # FOR LOOP WILL ITERARE ONE LINE SO PRINT ONE CHARACTER AT A TIME
    for i in line:
        # Force print in one line using end = '' otherwise one char in one line
        print(i, end = '')
        # BELOW LINE IS TO EXECUTE LOOP AFTER USER PRESSES KEYBOARD
        #dummy = input()
file.close()