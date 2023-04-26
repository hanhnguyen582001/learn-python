#! /usr/bin/python3.11
# this is a single comment
import sys
import decimal
import fractions
name = 'hanh'
print(name)
print(2**32)
print(sys.platform)


def fullname():
    print('Nguyen The Hanh')


# 1/0
# Numeric
arr = [1, 2.1, 0o177, 3+4j, {1, 2, 3, 4},
       decimal.Decimal(1), fractions.Fraction(1, 3), True, False]
for i in arr:
    print(type(i))
print(arr[2]+arr[3])
a = complex(1, 2)
print(type(a))
print(abs(-1))
x, y = 1, 2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x % y)
print(-x)
print(+x)
print(abs(-x))
print(arr[3].conjugate())
print(divmod(x, y))
print(x**y)
z=1/3.0
print('{0:4.2f}'.format(z))
print(2.0==2)
print(1.1+2.2==3.3)
print(2*3+1j)
print(arr[5])
print(decimal.Decimal(1)/decimal.Decimal(7))
decimal.getcontext().prec = 4
print(decimal.Decimal(100000)/decimal.Decimal(7))
print(fractions.Fraction(1.25))
#set
print(type((2.5).as_integer_ratio() ))
a={'1234','1234','1234'}
a.add('1234')
print(a)
L = [1, 2, 1, 3, 2, 4, 5]
print(list(set(L)))
L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print(L1==L2)
print(set(L1) == set(L2))