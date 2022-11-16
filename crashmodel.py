# Link model proses analisa. crash analisis
# from kaggle
# -----------------------------------------
# https://colab.research.google.com/drive/1qjZRoYuzmFIXE3AAatoFsA5duUzmoRyh?usp=sharing

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as stat

sns.set()

# data frame 
data = pd.read_csv('/home/mulyono/projects/belajar_git/datacsv/ped_crashes.csv')
dx = data.head(10)
print(dx)

# describe data 
d1 = data.describe();
print(d1)

# data info
d2 = data.info()
print (d2)

# injury crash
plt.figure(figsize=(15,10))
sns.set_palette("Set3")
plt.title("Worst Injury in Crash", fontsize=25)
sns.countplot(x="Worst Injury in Crash", data=data)
plt.show()

# parametaer

injury_num = []
for i in data["Worst Injury in Crash"]:
    if i == "No injury (O)":
        injury_num.append(0)
    elif i == "Possible injury (C)":
        injury_num.append(1)
    elif i == "Suspected minor injury (B)":
        injury_num.append(2)
    elif i == "Suspected serious injury (A)":
        injury_num.append(3)
    else:
        injury_num.append(5)

data["Injury"] = injury_num
        
plt.figure(figsize=(15,10))
plt.title("Year", fontsize=25)
sns.histplot(x="Crash Year", kde=True, data=data)
plt.show()  

# plot
plt.figure(figsize=(15,10))
plt.title("How injured with year", fontsize=25)
sns.barplot(x="Crash Year", y="Injury", data=data)
plt.show()


plt.figure(figsize=(15,10))
plt.title("Month", fontsize=25)
sns.countplot(x="Crash Month", data=data)
plt.show()

plt.figure(figsize=(15,10))
plt.title("Day", fontsize=25)
sns.histplot(x="Crash Day", hue="Person Gender", kde=True, bins=31, data=data)
plt.show()

# person age ============
plt.figure(figsize=(15,10))
plt.title("Person Age", fontsize=25)
sns.histplot(x="Person Age", kde=True, hue="Person Gender", data=data, bins=100)
plt.xlim(0,100)
plt.ylim(0,150)
plt.show()

# hit and run case ======
plt.figure(figsize=(15,10))
plt.title("Crash: Hit-and-Run", fontsize=25)
sns.countplot(x="Crash: Hit-and-Run", hue="Person Gender", data=data)
plt.show()

# place crash
plt.figure(figsize=(15,20))
plt.title("Place", fontsize=25)
sns.countplot(y="City or Township", data=data)
plt.show()