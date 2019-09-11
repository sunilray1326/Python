

from decimal import Decimal

x = 0.1 + 0.1 + 0.1
print(x)

x = 0.1 + 0.1 + 0.1 - 0.3
print(x)

## So floating point maths is different and we CANNOT use it for MONEY related calculations
## Need to use Decimal class for Money related calculations
a = Decimal('0.1')
b = Decimal('0.3')

x = a + a + a - b
print(x)

x = True
print('x is {}'.format(type(x)))

x = 5 > 7
print(x)

x = None 
print(type(x))
