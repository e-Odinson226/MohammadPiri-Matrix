from numpy import random, zeros ,fabs
import os
from pathlib import Path
import json

import numpy


BaseDir = Path(__file__).resolve().parent
try:
    with open(os.path.join(BaseDir, "Computed.json"), 'r') as file:
        readDict = json.load(file)

except FileNotFoundError as e:
    print("فایل یافت نشد!")

dimention = readDict['dimention']
matA = numpy.array(readDict['matrixA'])
matB = numpy.array(readDict['matrixA'])

print("Create matrix[A]:")
baze = [readDict["min"], readDict["max"],]

matA = random.random_integers(baze[0], baze[1], size=(dimention, dimention))
print("|------------------------------|")
print("matrix[A]: ")
print(matA)
print("|------------------------------|")

# ---------- Trace ----------
#print(f"matrix[A][3]:   {matA[2]}")
#print(f"matrix[A][3][2]:{matA[2][1]}")

matB = random.random_integers(baze[0], baze[1], (dimention))
print("|------------------------------|")
print("matrix[B]: ")
print(matB)
print("|------------------------------|")


#solved = linalg.solve(matA, matB)
x = zeros(dimention , float);

for k in range(dimention-1):
    if fabs(matA[k,k]) < 1.0e-12 :
      for i in range(k+1,dimention):
        if fabs (matA[i,k]) > fabs(matA[k,k]):
           matA[k,i] = matA[i,k]
           matB[k,i] = matB[i,k]
           break
        
        
    for i in range(k+1,dimention):
        if matA[i,k] == 0:continue
        factor = matA[k,k]/matA[i,k]
        for j in range(k,dimention):
            matA[i,j] = matA[k,j]-matA[i,j]*factor
        matB[i] = matB[k]-matB[i]*factor  

        
x[dimention-1] = matB[dimention-1] / matA[dimention-1,dimention-1]
for i in range(dimention-2,-1,-1):
    sum_Ax = 0
    for j in range(i+1,dimention):
        sum_Ax += matA[i,j] * x[j]
    x[i] = (matB[i]-sum_Ax) / matA[i,i]


print('----- The solution is: -----')
print(x)

matAj = json.dumps(matA.tolist())
matBj = json.dumps(matB.tolist())
solvedj = json.dumps(x.tolist())

mainDict = {
    "type" : "Calculated",
    "min" : baze[0],
    "max" : baze[1],
    "dimention" : dimention,
    "matrixA" : matAj,
    "matrixB" : matBj,
    "solution" : solvedj
    
}
#-----------------------------------------------------------

BaseDir = Path(__file__).resolve().parent
try:
    with open(os.path.join(BaseDir, "Calculated.json"), 'w') as file:
        json.dump(mainDict, file, indent=4)

except FileNotFoundError as e:
    print("فایل یافت نشد!")