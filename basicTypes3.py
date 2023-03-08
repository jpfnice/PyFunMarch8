
"""
Basic types:
    
int: 12, -4, 0
float: 34.56, 2.3E+12
complex: 3.4+4.5j

bool
NoneType

"""
nb = 3.4+4.5j
print(nb, type(nb))
nb = complex(3.2, 6.7)
print(nb, type(nb))

print(nb.real) # real is a readonly attribute
print(nb.imag)

# + - * / % ** // += -= *= /= 
# module cmath

