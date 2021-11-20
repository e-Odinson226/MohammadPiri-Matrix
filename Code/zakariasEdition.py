import numpy as np
dimention = int(input("Enter matrix dimention: "))
#s = np.random.randint(-1000, 1000)

mat_1 = np.random.rand(dimention, dimention,)
print("Mat_1: ")
print(mat_1)

# ---------- Trace ----------
print(f"Mat-1[3]:{mat_1[2]}")
print(f"Mat-1[3][2]:{mat_1[2][1]}")

answer = np.random.rand(dimention)
print(answer)

#A = s*a
#B = s*b

#print("A = ")
#print(A)
#print("B = ")
#print(B)
z=np.linalg.solve(A,B)
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


