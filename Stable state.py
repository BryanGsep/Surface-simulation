import numpy as np
import matplotlib.pyplot as plt
import os
import random

len_x = 10
len_y  = 10
dx  = 0.1

x = np.arange(0,len_x+dx, dx)
y = np.arange(0,len_y+dx, dx)
X,Y = np.meshgrid(x,y)
T = np.zeros_like(X)
g = 9.8
omega = 1.5
k = 1000
alpha = 7
fig = plt.figure()

def graph3D(name:str):
    """ Make a 3D graph for T """
    ax = plt.axes(projection = '3d')
    # Plot the surface.
    surf = ax.plot_surface(X, Y, T, cmap='rainbow',linewidth=0, antialiased=False, vmin = -3, vmax = 0.5)
    ax.set_zlim([-10, 0.5])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("T")
    ax.set_title(name)

def stablestate(T,g,omega,k,alpha,dx):
    c = (dx**2)*g/alpha
    os.chdir("C:\PDE Final report\Problem 1\Stablestate")
    for i in np.arange(k):
        for j in np.arange(1,len(T)-2):
            for q in np.arange(1,len(T[0])-2):
                T[j][q] =T[j][q] + omega*((T[j+1][q]+T[j-1][q]+T[j][q+1]+T[j][q-1]-c)/4.0 - T[j][q])
        
        graph3D(f"System after {i} iteration")
        plt.savefig('%04d.png'%(i))
        plt.cla()
        plt.clf()
        
stablestate(T,g,omega,k,alpha,dx)

os.system("ffmpeg -framerate 200 -y -i ./%04d.png ./sucessive.mp4")


