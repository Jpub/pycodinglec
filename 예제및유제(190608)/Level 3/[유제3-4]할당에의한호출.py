a = 1
b = 2
print(id(a), id(b))
c = a
a = b
b = c
print(id(a), id(b))


#
