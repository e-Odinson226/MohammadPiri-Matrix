from numpy import mat, promote_types, random, linalg
import os
from pathlib import Path
import json

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
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

matB = random.random_integers(baze[0], baze[1], (dimention))
print("|------------------------------|")
print("matrix[B]: ")
print(matB)
print("|------------------------------|")

solved = linalg.solve(matA, matB)
print('----- The solution is: -----')
print(solved)

matAj = matA.tolist()
matBj = matB.tolist()
solvedj = solved.tolist()


mainDict = {
    "type" : "Computed",
    "min" : baze[0],
    "max" : baze[1],
    "dimention" : dimention,   
    "matAj" : matAj,   
    "matBj" : matBj,   
    "solvedj" : solvedj,   
}
#-----------------------------------------------------------

BaseDir = Path(__file__).resolve().parent
try:
    with open(os.path.join(BaseDir, "Computed.json"), 'w') as file:
        
        json.dump(mainDict, file, indent=4)
        

except FileNotFoundError as e:
    print("فایل یافت نشد!")
