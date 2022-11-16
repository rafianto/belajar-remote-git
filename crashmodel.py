# Link model proses analisa.
# https://colab.research.google.com/drive/1qjZRoYuzmFIXE3AAatoFsA5duUzmoRyh?usp=sharing

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as stat

sns.set()
data = pd.read_csv('/home/mulyono/projects/belajar_git/datacsv/ped_crashes.csv')
dx = data.head(10)
print(dx)

#describe data 
d1 = data.describe();
print(d1)

