#! /usr/bin/python3.11
# this is a single comment
import dir1.main
import first
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
    print('%s) %s' % (i, l.strip()))

# function


def f1():
    X = 88  # Enclosing def local

    def f2():
        print(X)  # Reference made in nested def
    f2()


f1()

# functions retain state


def f1(X):
    def f2():
        print(X)  # Remembers X in enclosing def scope
    return f2  # Return f2 but don't call it


action = f1(10)  # Make, return function
action2 = f1(11)
action()
action2()

# lambda functions retain state too


def f1(X):
    return lambda: print(X)


action = f1(10)  # Make, return function
action2 = f1(11)
action()
action2()

# nolocal variable


def tester(start):
    def nested(label):
        nonlocal start
        print(label, start)
        start += 1
    return nested


F = tester(0)
F('spam')
F('spam')


def tester(start):
    def nested(label):
        print(label, nested.state)  # nested is in enclosing scope
        nested.state += 1  # Change attr, not nested itself

    nested.state = start  # Initial state after func defined
    return nested


F = tester(0)
F('spam')
F('spam')


def tester(start):
    global state  # Move it out to the module to change it
    state = start  # global allows changes in module scope

    def nested(label):
        global state
        print(label, state)
        state += 1
    return nested


F = tester(0)
F('spam')
F('spam')


class tester:  # Class-based alternative (see Part VI)
    def __init__(self, start):  # On object construction,
        self.state = start  # save state explicitly in new object

    def nested(self, label):
        print(label, self.state)  # Reference state explicitly
        self.state += 1


F = tester(0)
F.nested('spam')
F.nested('spam')


def func():
    X = 'NI'

    def nested():
        nonlocal X
        X = 'Spam'
    nested()
    print(X)


func()


def changer(a, b, c):  # Arguments assigned references to objects
    a = 2  # Changes local name's value only
    b[0] = c


x = 1
y = [1, 2, 3]
changer(x, y, 'spam')
print(x, y)  # => 1 ['spam', 2, 3]
changer(x, y[:], 'hello')
print(x, y)  # => 1 ['spam', 2, 3]; y does not change

# multi output parameter
x = 1
y = [1, 2, 3]


def swap(x, y):
    x, y = y, x
    return x, y


x, y = swap(x, y)
print(x, y)  # => [1, 2, 3] 1

# Keyword and Default


def f(a, b, c): print(a, b, c)


f(c=3, b=2, a=1)  # => 1 2 3


def f(a, b=2, c=3): print(a, b, c)


f(a=1)  # => 1 2 3

# Arbitrary Arguments


def sum(*args):
    print(type(args))
    result = 0
    for x in args:
        result += x
    return result


sum(1, 2, 3)


def f(**kargs):
    print(kargs)


f(a=1, b=2)
D = {'a': 1, 'b': 2, 'c': 3}
f(**D)
# combination


def f(a, *pargs, **kargs): print(a, pargs, kargs)


f(1, 2, 3, x=1, y=2)  # => 1 (2, 3) {'y': 2, 'x': 1}

# Unpacking arguments
a = (1, 2, 3, 4)
print(sum(*a))


def sum_value_dict(**kwargs):
    result = 0
    for key, value in kwargs.items():
        result += value
    return result


D = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(sum_value_dict(**D))


def combination_sum(*args, **kwargs):
    result = 0
    for value in args:
        result += value
    for key, value in kwargs.items():
        result += value
    return result


print(combination_sum(1, 2, 3, a=1, b=2, c=3))


def kwonly(a, *d, b, c):
    print(a, b, c, d)


kwonly(1, 2, 3, 4, b=5, c=6)  # => 1 5 6 (2, 3, 4)


def kwonly(a, *, b, c, **args):
    print(a, b, c)


# kwonly(1, 2, 3, 4, b=5, c=6) #=> error
# kwonly(1, 5, c=6)  # => error
kwonly(1, b=5, c=6)  # => 1 5 6
kwonly(1, **dict(b=2, c=3))  # Keyword-only in **


def sum(positive=True, *args):
    result = 0
    for x in args:
        result += x
    return result if positive == True else -result


print(sum(*[1, 2, 3, 4]))  # => 9 because positive=1 and args=[2,3,4]


def sum(*args, positive=True):
    result = 0
    for x in args:
        result += x
    return result if positive == True else -result


print(sum(*[1, 2, 3, 4]))  # => 10
print(sum(*[1, 2, 3, 4], positive=False))  # => -10


def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y


def minmax(*args, key=lessthan):
    res = args[0]
    for arg in args:
        if key(arg, res):
            res = arg
    return res


print(minmax(*[1, 2, 3, 4, 5, 6, 7]))  # => 1
print(minmax(*[1, 2, 3, 4, 5, 6, 7], key=grtrthan))  # => 7
print(minmax(*[1, 2, 3, 4, 5, 6, 7], key=lambda x, y: x < y))  # => 1


def intersect(*args):
    res = []
    for x in args[0]:  # Scan first sequence
        if x in res:
            continue  # Skip duplicates
        for other in args[1:]:  # For all other args
            if x not in other:
                break  # Item in each one?
        else:  # No: break out of loop
            res.append(x)  # Yes: add items to end
    return res


def union(*args):
    res = []
    for seq in args:  # For all args
        for x in seq:  # For all nodes
            if not x in res:
                res.append(x)  # Add new items to result
    return res


s1, s2, s3 = "SPAM", "SCAML", 'SPAL'
print(intersect(s1, s2, s3))

# Emulating the Python 3.X print Function


def print1(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


print1(s1, s2, s3, sep='...')

# Recursion


def sumtree(L):
    tot = 0
    for x in L:  # For each item at this level
        if not isinstance(x, list):
            tot += x  # Add numbers directly
        else:
            tot += sumtree(x)  # Recur for sublists
    return tot


L = [1, [2, [3, 4], 5], 6, [7, 8]]  # Arbitrary nesting
print(sumtree(L))

# lamda


def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)  # Title in enclosing def scope
    return action


act = knights()
msg = act('robin')
print(msg)
L = [lambda x: x ** 2,  # Inline function definition
     lambda x: x ** 3,
     lambda x: x ** 4]
for f in L:
    print(f(2))

# List Comprehensions
L = [ord(x) for x in 'spam']
L1 = list(map(ord, 'spam'))
print(L == L1)
# => [100, 200, 300, 101, 201, 301, 102, 202, 302]
res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
# access the column in matrix
matrix = [[1, 2, 3],
          [2, 3, 4],
          [4, 5, 6]]
column = [row[0] for row in matrix]
print(column)  # => 1,2,4
# access the Diagonals
diagonals = [matrix[i][i] for i in range(len(matrix))]
print(diagonals)  # 1,3,6

# generator


def gensquares(N):
    for i in range(N):
        yield i ** 2


print(type(gensquares(5)))  # => class generator
for res in gensquares(5):
    print(res, sep=',', end='')
# => 0,1,4,9,16


def gensquares1(N):
    for i in range(N):
        return i ** 2


print(type(gensquares1(5)))  # => class int
print(gensquares1(5))  # => 0
# generator is a iterator
gensq = gensquares(5)
print(next(gensq))  # => 0
print(next(gensq))  # => 1
print(iter(gensq) == gensq)  # => true
print(tuple(gensquares(5)))  # => 0,1,4,9,16

# generator expression
a = (x * x for x in range(5))
print(type(a))  # => class generator
list(print(x, end=' ') for x in 'spam')


def scramble(seq):
    return (seq[i:] + seq[:i] for i in range(len(seq)))


print(list(scramble([1, 2, 3, 1])))
print(dir1.main)
print(dir1.x)


class person:
    def __init__(self, first_name, last_name, age, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f"[person: {self.first_name}, {self.last_name}, {self.age}, {self.job}]"

    def __str__(self):
        return f'hello my name is {self.last_name}, I\'m {self.age}, I\'m {self.job}'

    def speak(self):
        pass


per1 = person('Nguyen The', 'Hanh', 22, 'developer')
print(per1)
print(repr(per1))
print(per1.full_name())


class VietNamPerson(person):
    def speak(self):
        print('i speak vietnamese')


class JapanesePerson(person):
    def speak(self):
        print('i speak japanese')


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def showAll(self):
        for person in self.members:
            print(person)


per1 = VietNamPerson('Nguyen The', 'Hanh', 22, 'developer')
per2 = JapanesePerson('Uzumaki', 'Naruto', 22, 'ninja')
per1.speak()
per2.speak()

depart= Department(per1,per2)
depart.showAll()
per1.first_name='Hanh'
print(depart.members[0])

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    def __str__(self):
        return str(self.items_list)
    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
    __update = update   # private copy of original update() method


a = Mapping((1, 2, 3, 4, 5))
a.update((1, 2))
print(a)  # => [1, 2, 3, 4, 5, 1, 2]
a = MappingSubclass((1, 2, 3, 4, 5))
a.update(['a', 'b'], [1, 2])
print(a)  # => [1, 2, 3, 4, 5, ('a', 1), ('b', 2)]
print(type(MappingSubclass._Mapping__update))
a._Mapping__update((1, 2))
print(a)  # => [1, 2, 3, 4, 5, ('a', 1), ('b', 2), 1, 2]
