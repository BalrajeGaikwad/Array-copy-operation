import numpy as np
a=np.array([[3,3,7],[1,5,2]])
b=a
print("array of a")
print(a)

print(b is a )
b[0][0]=100
print("value of b")
print(b)

c=a.view()
print("Array of c")
print(c)
print(c is a)
c[0][0]=50

d=np.copy(a)
print(d)
print(d is a)
d[0][0]=150



a=np.array([[3,7,6],[1,5,2]])
b=np.array([[3,7,6],[1,5,2]])
a.sort()
b.sort(axis=0)