
"""
Loading CSV File in Python

"""

## Using the Standard Python Library

with open('vehicle.csv', 'r') as f:
    column_names = f.readline().strip().split(',')
    data = []
    
    for line in f:
        
        data.append(line.strip().split(','))
    

import pandas as p

A = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
     'year': [2000, 2001, 2002, 2001, 2002],
     'pop': [1.5,1.7, 3.6, 2.4, 2.9]
     
     }

data2 = p.DataFrame(A)

input_number = input(int("PLease Enter a number: "))

for i in range(1,input_number):
    
    print(i)
    
    
