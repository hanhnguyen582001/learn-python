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
z = 1/3.0
print('{0:4.2f}'.format(z))
print(2.0 == 2)
print(1.1+2.2 == 3.3)
print(2*3+1j)
print(arr[5])
print(decimal.Decimal(1)/decimal.Decimal(7))
decimal.getcontext().prec = 4
print(decimal.Decimal(100000)/decimal.Decimal(7))
print(fractions.Fraction(1.25))
# set
print(type((2.5).as_integer_ratio()))
a = {'1234', '1234', '1234'}
a.add('1234')
print(a)
L = [1, 2, 1, 3, 2, 4, 5]
print(list(set(L)))
L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print(L1 == L2)
print(set(L1) == set(L2))
# The Dynamic Typing
# Types Live with Objects, Not Variables and Objects Are Garbage-Collected
a = 3
print(type(a))
a = 'hanh'
print(type(a))
a = 2.1
print(type(a))
# Shared References and Equality
a = 3
b = 3
print(a == b)  # => true
print(a is b)  # => true
a = [3]
b = [3]
print(a == b)  # => true
print(a is b)  # => false
# string fudamental
s = ''  # empty string
s = "spam's"  # double quotes same the single
s = 's\np\ta\x00m'  # escape sequences
s = """a
b
c"""  # triple quoted block strings
b = b'sp\x61m'
u = u'sp\u00c4m'  # in python 3 every character in a string is one or more bytes
s1 = 'hanh'
s2 = ' nguyen'
print(s1+s2)  # concat string
s3 = s1*3
s1[0]
s1[1:2]
len(s1)
print('a %s parrot' % 'hello')
print('a {0} parrot'.format('hello'))
print("hanhhanh".find('z'))
print("hanhhanh".replace('a', 'x'))
print([c * 2 for c in 'hanh'])
print('h' in 'hanh')
print(list(map(ord, 'hanh')))
print(r'~\python\test')
print('hanh'[-1:None:-1])
print('hanh!'[:-1]+' nguyen' + 'hanh!'[-1])
S = 'HANH'
print(S.capitalize())
print(S.ljust(20, ' '))
print(S.casefold())
print(S.lower())
S.center(20)
print(S.lstrip('H'))
print(S.count('HA', 0, -2))
print(S.translate(str.maketrans('HA', 'AH')))
print(S.encode())
# Dictionary-Based Formatting Expressions
reply = """
Greetings...
Hello %(name)s!
Your age is %(age)s
"""
value = {'name': 'hanh', 'age': 23}
print(reply % value)
name = 'hanh'
age = '23'
print(reply % vars())
template = """Greetings...
Hello {name}!
Your age is {age}"""
print(template.format(**value))
template = f"""
Greetings...
Hello {value['name']}!
Your age is {value['age']}
"""
print(template)
# list
l = []
l = [123, 'abc', 1.23, {}]
L = l
L2 = l*2
l[0] = 1
print(L)
print(L2)
del L[0]
print(L)
l.remove('abc')
print(L)
l = [123, 'abc', 1.23, {}]
print(L)
l[1:3] = []
print(l)
l[1:] = [1, 2, 3, 4]  # => [123,1,2,3,4]
l[1] = [1, 2, 3, 4]  # => [123,[1,2,3,4],2,3,4]
print(l)
len(l)  # => get length of list l
print(list('123')+l)
l = [el*4 for el in l]
print(l)
l = [1, 4, 3, 1]


def doiso(a):
    return -a


l.sort(key=doiso)
print(l)
l.append(5)
print(sorted([doiso(x) for x in l], reverse=True))
l.extend([1, 2, 3, 4])
print(l)
l.insert(10, 5)
print(l)
# dic
D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(D['spam'])
print(D.get('hello'))  # => same dig()
print(list(D.keys()))
print(D.values())
print(D.setdefault('hanh', 5))
print(D)
print(D.items())
D = {x: x*2 for x in range(10)}
print(D)
D = dict(name='Bob', age=40)
D = dict([('name', 'Bob'), ('age', 40)])
D = dict.fromkeys(['a', 'b'])
print(D)
D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
D = {x: x ** 2 for x in [1, 2, 3, 4]}
D = {c: c * 4 for c in 'SPAM'}
print(D.items())
D = {'a': 1, 'b': 2, 'c': 3}
print(D.keys() & {'b': 1})
print(D)
D = {'a': 1, 'b': 2, 'c': 3, 'c': 4}
print(D)
D = dict(D.items() | {('c', 3), ('d', 4)})  # dict accepts iterable sets too
print(D)


def Key(a):
    print

items = list(D.items())
items.sort()
print(items)
D=dict(items)
print(D)
#tuple
T=('hello')
print(T) #=> 
l=['name', 'jobs']
T=('name', 'jobs')
l1=l[0:]
print(l1 is l)
t1=T[0:]
print(t1 is T)
t=40,
print(t)