import numpy as np
import matplotlib.pyplot as plt
import os
# Initial setting

d = 0.2
alpha  = 0.1
dx = 0.1
len_x = 5.0
len_y = 5.0
dt = d*(dx**2)/alpha

x = np.arange(0,len_x+dx, dx)
y = np.arange(0,len_y+dx, dx)
X,Y = np.meshgrid(x,y)

T = np.zeros_like(X)

t = 10
plt.figure(figsize = (10,10))

icounter = -1
T = np.zeros_like(X)
T[20:60,20:60]  = 10.0

for it in np.arange(0, t+dt, dt):
    ax = plt.axes(projection = '3d')
    p = ax.plot_surface(X, Y, T, cmap= 'rainbow',linewidth=0, antialiased=False, vmax = 10, vmin = 0)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('T')
    ax.set_zlim([0.0,10.0])
    plt.colorbar(p)
    ax.set_title('Time = %.5f'%(it))
    icounter = icounter + 1
    plt.savefig('%04d.png'%(icounter))
    plt.cla()
    plt.clf()
    T = T + d*(np.roll(T,-1,axis=1)+np.roll(T,1,axis=1)+np.roll(T,-1,axis=0)+np.roll(T,1,axis = 0) - 4*T)
    T[0,:] = 0
    T[-1,:] = 0
    T[:, 0] = 0
    T[:,-1] = 0

os.system("ffmpeg -framerate 100 -y -i ./%04d.png ./Dirichlet.mp4")
