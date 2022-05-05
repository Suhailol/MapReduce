
import sys
import pandas as pd
df = pd.read_csv('heart_disease_data.csv')
age = df['age']
for word in age:
    print(word, "\t", 1)



# import sys
# for line in sys.stdin:
#     line = line.strip()
    
#     words = line.split(',')

#     for word in words:
#         print("%s\t%s"%(word, 1))
