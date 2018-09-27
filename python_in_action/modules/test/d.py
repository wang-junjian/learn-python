import b
import c

print('d.py')
print(dir())
print(b.a.i)
print(c.a.i)

import a
print(a.i)

import sys
print(sys.modules)

import imp
imp.reload(a)
print(a.i)
