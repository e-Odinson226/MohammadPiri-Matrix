
import numpy as np
from numpy import linalg
n = int(input("Enter n = "))
s = np.random.randint(-1000, 1000)
a = np.random.rand(n,n)
b = np.random.rand(n)
A = s*a
B = s*b

print("A = ")
print(A)
print("B = ")
print(B)
z=linalg.solve(A,B)
print('The solution is:')
print(z)
file = "َABn.txt"
file = open('ABn.txt', "w")

file.write(" n is : ")
file.write(str(n))

file.write(" A is : ")
file.write(str(A))
file.write(" B is : ")
file.write(str(B))

file.write(" The solution is: ")
file.write(str(z))
file.close()


