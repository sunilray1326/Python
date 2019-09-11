## using multiple variables in single line and their assignments

print("-----------------------------------")
# simple fibonacii series
a, b = 0, 1
while (b<1000):
    print(b, end = ' ', flush = True)
    a, b = b, a+b
print("\n-----------------------------------")

## Python allows multiple variable and their expresion on same like
a, b, c = 1, 2, 3
while (c<20):
    print(a, b, c)
    a, b, c = b, c, c+1