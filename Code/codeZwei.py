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

min = readDict['min']
max = readDict['max']
dimention = readDict['dimention']
matA = readDict['matAj']
matA_backup = readDict['matAj']
matB = readDict['matBj']
solvedj = readDict['solvedj']



x = zeros(dimention , float);

for k in range(dimention-1):
    if fabs(matA[k][k]) < 1.0e-12 :
      for i in range(k+1,dimention):
        if fabs (matA[i][k]) > fabs(matA[k][k]):
           matA[k][i] = matA[i][k]
           matB[k][i] = matB[i][k]
           break
        
        
    for i in range(k+1,dimention):
        if matA[i][k] == 0:continue
        factor = matA[k][k]/matA[i][k]
        for j in range(k,dimention):
            matA[i][j] = matA[k][j]-matA[i][j]*factor
        matB[i] = matB[k]-matB[i]*factor  

        
x[dimention-1] = matB[dimention-1] / matA[dimention-1][dimention-1]
for i in range(dimention-2,-1,-1):
    sum_Ax = 0
    for j in range(i+1,dimention):
        sum_Ax += matA[i][j] * x[j]
    x[i] = (matB[i]-sum_Ax) / matA[i][i]


print('----- The solution is: -----')
print(x)

matAj = json.dumps(matA_backup)
matBj = json.dumps(matB)
solvedj = json.dumps(x.tolist())

mainDict = {
    "type" : "Calculated",
    "solution" : solvedj
    
}
#-----------------------------------------------------------

BaseDir = Path(__file__).resolve().parent
try:
    with open(os.path.join(BaseDir, "Calculated.json"), 'w') as file:
        json.dump(mainDict, file, indent=4)

except FileNotFoundError as e:
    print("فایل یافت نشد!")
