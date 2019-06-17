def swap(a, b):
    c = a
    a = b
    b = c

A = [1]
B = [2]
print(id(A), id(B))
swap(A, B)
print(id(A), id(B))

