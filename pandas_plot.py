import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
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
o2 = df[['A','B']].plot(kind='line')

print(o1)
print(o2)

o3 = df.plot(x='A', y='B', kind='scatter')

print(o3)


plt.figure(figsize=(15,10))
plt.title("Pandas Plot", fontsize=25)
sns.histplot(x="A", hue="B", kde=True, bins=31, data=df)
plt.show()