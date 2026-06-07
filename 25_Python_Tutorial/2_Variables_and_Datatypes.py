# Variables - 1
a = 25
b = 40
print(a, b)

# Variables - 2
# Underscore (_) is the only special character allowed in variable names
a_b = 5
print(a_b)

# Variables - 3
# Variable name can only start with alphabet a-z or A-Z or "_" (Lexical rule), Variable name Can't start with numbers but can have numbers
a5b = 8
A_b = 6
_aB = 7
print(a5b, A_b, _aB)

# Variables - 4
# Multiple variables can be assigned in single line
x = y = 9
c, d = 10, 11
print(x, y, c, d)

# Datatypes - 1
# String, Integer, Float, Boolean, None
a = "Rohit"                  # str
b = 4                        # int
c = 3.5                      # float
d = True                     # bool
e = None                     # NoneType

# Datatypes - 2
# List, Set, Tuple, Dictionary
f = [1000, 4.567, "Rohit"]   # list
g = {1, 1, 2, 2, 3}          # set
h = (1, 2, 3)                # tuple
i = {1: "One", "Two": 2}     # dict

# Get Data type
print(type(a), type(b), type(c))
print(type(d), type(e), type(f))
print(type(g), type(h), type(i))
