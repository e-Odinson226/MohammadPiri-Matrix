from numpy import mat, promote_types, random, linalg
import os
from pathlib import Path
import json
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


matAj = json.dumps(matA.tolist())
matBj = json.dumps(matB.tolist())
solvedj = json.dumps(solved.tolist())

mainDict = {
    "dimention" : dimention,
    "matrixA" : matAj,
    "matrixB" : matBj,
    "solution" : solvedj
    
}
#-----------------------------------------------------------

BaseDir = Path(__file__).resolve().parent
try:
    with open(os.path.join(BaseDir, "Computed.json"), 'w') as file:
        
        json.dump(mainDict, file, indent=4)

except FileNotFoundError as e:
    print("فایل یافت نشد!")
