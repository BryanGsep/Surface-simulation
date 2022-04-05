import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D

##Inital setting

dx = 0.1
len_x = 10
len_y = 10
x = np.arange(0,len_x+dx, dx)
y = np.arange(0,len_y+dx, dx)
alpha = 0.1
nu = 0.02
dt = 0.1
A = alpha*dt/dx
B = nu*dt/(dx**2)
t = 25
X,Y = np.meshgrid(x,y)
u = np.zeros_like(X)
fig = plt.figure(figsize = (10,10))
icounter = -1
u[20:80,20:80] = 10
for it in np.arange(0,t+dt,dt):
    icounter += 1
    ax = plt.axes(projection = '3d')
    ax.plot_surface(X,Y,u, cmap = 'rainbow', vmax = 10, vmin = 0,linewidth=0, antialiased=False)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("u")
    ax.set_zlim([0.0,10.0])
    ax.set_title('Time = %.5f'%(it))
    plt.savefig('cyclic%04d.png'%(icounter))
    plt.cla()
    plt.clf()
    u = u + A*(np.roll(u,1,0)+np.roll(u,1,1)-2*u)+B*(np.roll(u,1,0)+np.roll(u,-1,0)+np.roll(u,1,1)+np.roll(u,-1,1)-4*u)

os.system("ffmpeg -framerate 50 -y -i ./cyclic%04d.png ./linearalpha.mp4")



    

