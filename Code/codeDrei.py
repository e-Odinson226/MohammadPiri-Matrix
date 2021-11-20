# Drived By: Zakaria
import json
import os
from pathlib import Path
from numpy import promote_types, zeros, fabs
BaseDir = Path(__file__).resolve().parent

try:
    with open(os.path.join(BaseDir, "Computed.json"), 'r') as computed:
        with open(os.path.join(BaseDir, "Calculated.json"), 'r') as calculated:
            computedDict = json.load(computed)
            calculatedDict = json.load(calculated)
            
            difList = zeros(computedDict['dimention'] , float)
            
            for i in range(computedDict['dimention']):
                print(f"Computed[{i}]  :    {computedDict['solvedj'][i]}")
                print(f"Calculated[{i}]:    {calculatedDict['solution'][i]}")
                print("                 --------------------")
                
                diff = fabs(computedDict['solvedj'][i] - calculatedDict['solution'][i])
                print(f"Difference:        {diff}")
                print("|----------------------------------|")
                difList[i] = diff
                
                if difList[i] < 0.00000000001:
                    print("OK")
                else:
                    print("Not OK")
                    
    print(f"List of differences: ")
    for num in range(len(difList)):
        print(f"{num+1}: {difList[i]}")
                
            
        

except FileNotFoundError as e:
    print("فایل یافت نشد!")