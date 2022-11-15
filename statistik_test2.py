from turtle import color
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#fig, ax = plt.subplots()  # Create a figure containing a single axes.
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.pip
# plt.show()

#plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
#plt.show()

x = np.arange(1,20,0.5)
y = x**2

#cara pertama ---
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_title("Judul Graphik")
axes.set_xlabel("sumbu x")
axes.set_ylabel("sumbu y")
plt.show()


#dua graphic
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes1.plot(x,y,color="red")
axes1.set_title("Judul Graphik A")
axes1.set_xlabel("sumbu x A")
axes1.set_ylabel("sumbu y A")

axes1 = fig.add_axes([0.2,0.5,0.3,0.3])
axes1.plot(y,x,color="blue")
axes1.set_title("Judul Graphik B")
axes1.set_xlabel("sumbu x B")
axes1.set_ylabel("sumbu y B")


plt.show()

#cara kedua ---
fig, axes = plt.subplots(1,2)

axes[0].plot(x,y,color="red")
axes[0].set_title("Judul Graphik A")
axes[0].set_xlabel("sumbu x A")
axes[0].set_ylabel("sumbu y A")

axes[1].plot(y,x,color="green")
axes[1].set_title("Judul Graphik B")
axes[1].set_xlabel("sumbu x B")
axes[1].set_ylabel("sumbu y B")
plt.show()