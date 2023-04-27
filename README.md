Chapter 1:
6 main reasons that people choose to use python:
- software quality
- developer productivity
- program portability
- support libraries
- component intergration
- enjoyment
4 notable companies use python:
- google
- dropbox
- youtube
- BitTorrent
Why might you not want to use Python in an application?
- execution speed may not always be as fast as that of fully compiled and lower-level
languages such as C and C++
What can you do with Python?
- game programming
- Serial port communication on Windows, Linux
- image processing
- Robot control
- Natural language analysis
- Mobile computing with ports of Python to the Google Android and Apple iOS
platforms
- Mobile computing with ports of Python to the Google Android and Apple iOS
platforms
- Excel spreadsheet function and macro programming with the PyXLL or DataNitro add-ins
- Media file content and metadata tag processing with PyMedia, ID3, PIL/Pillow,
and more
- JSON and CSV file processing with the json and csv modules
- XML parsing with the xml library package, the xmlrpclib module, and third-party
extensions
- Data mining with the Orange framework, the Pattern bundle, Scrapy, and custom
code
4 way to run script file:
- command line
- import module
- exec file
- file icon click
why might you need  to reload a module:
- because python imports a module only once per process
What is a namespace, and how does it relate to module files?
- A namespace is just a package of variables (i.e., names). It takes the form of an
object with attributes in Python. Each module file is automatically a namespace—
that is, a package of variables reflecting the assignments made at the top level of
the file. Namespaces help avoid name collisions in Python programs: because each
module file is a self-contained namespace, files must explicitly import other files
in order to use their names
part 2:
built core data types:
Number,Strings,Lists,Dictionaries,tuples,Files,Sets,Booleans,tupes,Nones,Program unit types(functions,modules,classes),implementation-related types(compiled code,stack tracebacks)
Numeric types include:
- integer and floating-point object
- complex number object
- decimal
- fraction
- sets
- booleans
Set:
- A set object is an unordered collection of distinct hashable objects
Strings:
S.capitalize() S.ljust(width [, fill])
S.casefold() S.lower()
S.center(width [, fill]) S.lstrip([chars])
S.count(sub [, start [, end]]) S.maketrans(x[, y[, z]])
S.encode([encoding [,errors]]) S.partition(sep)
S.endswith(suffix [, start [, end]]) S.replace(old, new [, count])
S.expandtabs([tabsize]) S.rfind(sub [,start [,end]])
S.find(sub [, start [, end]]) S.rindex(sub [, start [, end]])
S.format(fmtstr, *args, **kwargs) S.rjust(width [, fill])
S.index(sub [, start [, end]]) S.rpartition(sep)
S.isalnum() S.rsplit([sep[, maxsplit]])
S.isalpha() S.rstrip([chars])
S.isdecimal() S.split([sep [,maxsplit]])
S.isdigit() S.splitlines([keepends])
S.isidentifier() S.startswith(prefix [, start [, end]])
S.islower() S.strip([chars])
S.isnumeric() S.swapcase()
S.isprintable() S.title()
S.isspace() S.translate(map)
S.istitle() S.upper()
S.isupper() S.zfill(width)
S.join(iterable)
Lists method:
L = [] An empty list
L = [123, 'abc', 1.23, {}] Four items: indexes 0..3
L = ['Bob', 40.0, ['dev', 'mgr']] Nested sublists
L = list('spam')
L = list(range(-4, 4))
List of an iterable’s items, list of successive integers
L[i]
L[i][j]
L[i:j]
len(L)
Index, index of index, slice, length
L1 + L2 Concatenate, repeat
Operation Interpretation
L * 3
for x in L: print(x)
3 in L
Iteration, membership
L.append(4)
L.extend([5,6,7])
L.insert(i, X)
Methods: growing
L.index(X)
L.count(X)
Methods: searching
L.sort()
L.reverse()
L.copy()
L.clear()
Methods: sorting, reversing,
copying (3.3+), clearing (3.3+)
L.pop(i)
L.remove(X)
del L[i]
del L[i:j]
L[i:j] = []
Methods, statements: shrinking
L[i] = 3
L[i:j] = [4,5,6]
Index assignment, slice assignment
L = [x**2 for x in range(5)]
list(map(ord, 'spam'))
dict method
D = {} Empty dictionary
D = {'name': 'Bob', 'age': 40} Two-item dictionary
E = {'cto': {'name': 'Bob', 'age': 40}} Nesting
D = dict(name='Bob', age=40)
D = dict([('name', 'Bob'), ('age', 40)])
D = dict(zip(keyslist, valueslist))
D = dict.fromkeys(['name', 'age'])
Alternative construction techniques:
keywords, key/value pairs, zipped key/value pairs, key lists
D['name']
E['cto']['age']
Indexing by key
'age' in D Membership: key present test
D.keys()
D.values()
D.items()
D.copy()
D.clear()
D.update(D2)
D.get(key, default?)
D.pop(key, default?)
D.setdefault(key, default?)
D.popitem()
Methods: all keys,
all values,
all key+value tuples,
copy (top-level),
clear (remove all items),
merge by keys,
fetch by key, if absent default (or None),
remove by key, if absent default (or error)
fetch by key, if absent set default (or None),
remove/return any (key, value) pair; etc.
len(D) Length: number of stored entries
D[key] = 42 Adding/changing keys
del D[key] Deleting entries by key
list(D.keys())
D1.keys() & D2.keys()
Dictionary views (Python 3.X)
D.viewkeys(), D.viewvalues() Dictionary views (Python 2.7)
D = {x: x*2 for x in range(10)} Dictionary comprehensions (Python 3.X, 2.7)
Tuples method:
() An empty tuple
T = (0,) A one-item tuple (not an expression)
T = (0, 'Ni', 1.2, 3) A four-item tuple
T = 0, 'Ni', 1.2, 3 Another four-item tuple (same as prior line)
Operation Interpretation
T = ('Bob', ('dev', 'mgr')) Nested tuples
T = tuple('spam') Tuple of items in an iterable
T[i]
T[i][j]
T[i:j]
len(T)
Index, index of index, slice, length
T1 + T2
T * 3
Concatenate, repeat
for x in T: print(x)
'spam' in T
[x ** 2 for x in T]
Iteration, membership
T.index('Ni')
T.count('Ni')
Methods in 2.6, 2.7, and 3.X: search, count
namedtuple('Emp', ['name', 'jobs']) Named tuple extension type