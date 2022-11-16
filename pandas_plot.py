import pandas as pd
import numpy as np

#penerapan ploting di pandas
n_row = 46
n_col = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1,20,size=(n_row,n_col)),columns = cols)
print(df.head())

#bar 
o1 = df.plot(kind='bar')

#plot A B
o2 = df[['A','B']].plot(kind='bar')

print(o1)
print(o2)