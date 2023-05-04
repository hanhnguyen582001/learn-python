#! /usr/bin/python3.11
# this is a single comment
import sys
import decimal
import fractions
from collections import namedtuple
import pickle
import json
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
D = dict(items)
print(D)
# tuple
T = ('hello')
print(T)  # =>
l = ['name', 'jobs']
T = ('name', 'jobs')
l1 = l[0:]
print(l1 is l)
t1 = T[0:]
print(t1 is T)
t = 40,
print(t)
REC = namedtuple('rec', ['name', 'age', 'jobs'])
hanh = REC(age=22, name='hanh', jobs=['coder', 'intern'])
print(hanh)
print(hanh[0])
print(hanh.name)
ordict = hanh._asdict()
print(type(ordict))
name, age, jobs = hanh
print(f'{name} {age} {jobs}')
for x in ordict:
    print(ordict[x])
rubyFile = open(r'ruby.rb', 'a+')
rubyFile.seek(0)
print(repr(rubyFile.read()))
# rubyFile.write('puts("hế hế hế hế lô")\n')
# rubyFile.seek(0)
# print(repr(rubyFile.readline()))
rubyFile.close()
rubyFile = open(r'ruby.rb', 'rb')
data = rubyFile.read()
print(data[0:4])
print(data[0])
print(data.decode('utf-8'))
X, Y, Z = 43, 44, 45
s = 'Spam'
D = {'name': 'Hanh', 'age': 22}
L = [1, 2, 3]
f = open('datafile.txt', 'w')
f.write(s + '\n')
f.write(f'{X},{Y},{Z}\n')
f.write(str(L)+'&'+str(D)+'\n')
f.close
f = open('datafile.txt', 'r')
datalists = f.readlines()
s = datalists[0].strip()
print(s)
X, Y, Z = tuple([int(p) for p in (datalists[1].lstrip().split(','))])
print(repr(X))
D = {'a': 1, 'b': 2}
f = open('datafile.pkl', 'wb')
pickle.dump(D, f)
f.close
f = open('datafile.pkl', 'rb')
E = pickle.load(f)
print(E)
print(hanh)
json_obj = json.dumps(hanh._asdict(), indent=4)
with open('person.json', 'w') as outfile:
    outfile.write(json_obj)
print(open('person.json').read())
with open('person.json', 'r') as infile:
    json_object = json.load(infile)
print(json_object)
x = 'spam'
a, *b = x
print(b)
x = spam, ham = ['yum', 'YUM']
print(x)
s = 'hello helooo abcsdwe'
S = 'hello helooo abcsdwe'
print(s is S)
x = 1 + 2 + 3 \
    + 4
print(x)
print(2 or 3)  # => 2
print(3 or 2)  # => 3
print([] or 3)  # => 3
print([] or {})  # => {}
print(2 and 3)  # => 2
print(3 and 2)  # => 2
print([] and 3)  # => []
print([] and {})  # => []
if (hanh.age > 20):
    print('hanh da gia')
else:
    print('hanh con tre')
print('hanh da gia') if hanh.age > 20 else print('hanh con tre')
s = 'spam'
while s:
    if (s[0] == 'm'):
        break
    if (s[0] != 'p'):
        print(s[0])
    s = s[1:]
else:
    print('da in xong')
T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)
for x in T:
    print(x[0], x[1])
D = {1: 2, 2: 3, 3: 4}
for key in D:
    print(key, D[key], sep='=>')
lot = [(1, 2, 3), (4, 5, 6)]
for both in lot:
    a, b, c = both
    print(a, b, c)
for line in open('ruby.rb'):  # Use iterators: best for text input
    print(line.rstrip())
print(tuple(range(5, -5, -2)))
print(tuple(range(5, 10)))
print(tuple(range(5)))
s = 'Nguyen The Hanh'
for c in s[::2]:
    print(c)
for i in range(0, len(s), 2):
    print(s[i])
l = [1, 2, 3, 4, 5]
for i in range(len(l)):
    l[i] += 1
print(l)
# albeit without changing the original list in place
# (we could assign the expression’s new list object result back to L, but this would not update any other references to the original list)
[x+1 for x in l]
print(l)
l = [1, 2, 3, 4, 5]
zipped = zip(l, range(5))
print(tuple(zipped))
zipped = zip(l, range(5))
print(dict(zipped))
print(type(range(5)))
print(list(map(lambda x: x+1, l)))
for (offset, item) in enumerate(l):
    print(item, 'appears at offset', offset)
for (i, l) in enumerate(open('ruby.rb')):
    print('%s) %s' %(i,l.strip()))