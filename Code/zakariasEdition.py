from numpy import promote_types, random, linalg
#import numpy as np
dimention = int(input("Enter matrix dimention: "))

print("Create matrix[A]:")
baze = [int(input("Min matrix[A]:")), int(input("Max matrix[A]:")),]

matA = random.random_integers(baze[0], baze[1], size=(dimention, dimention))
print("|------------------------------|")
print("matrix[A]: ")
print(matA)
print("|------------------------------|")

# ---------- Trace ----------
#print(f"matrix[A][3]:   {matA[2]}")
#print(f"matrix[A][3][2]:{matA[2][1]}")

print("\nCreate matrix[B]:")
baze2 = [int(input("Min matrix[B]:")), int(input("Max matrix[B]:")),]
matB = random.random_integers(baze2[0], baze2[1], (dimention))
print("|------------------------------|")
print("matrix[B]: ")
print(matB)
print("|------------------------------|")

solved = linalg.solve(matA, matB)
print('----- The solution is: -----')
print(solved)



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
