import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import animation
##Initital setting
u = 1.0
dx = 1.0
len_x = 100
t = 600
def upwind(y,dt):
    y = y + (u*dt/dx)*(np.roll(y,1,axis = 0)-y)
    return y


def leith(y,dt):
    c = y.copy()
    b = (np.roll(y,-1,axis = 0) - np.roll(y,1,axis = 0))/(2*dx)
    a = (np.roll(y,-1,axis = 0) + np.roll(y,1,axis = 0)-2*y)/(2*(dx**2))
    y = a*(u*dt)**2-b*(u*dt)+c
    return y

def CIP(y,g,dt):
    a = 2*(np.roll(y,1,axis = 0)-y)/(dx**3) + (g+np.roll(g,1,axis = 0))/(dx**2)
    b = -3*(y-np.roll(y,1,axis = 0))/(dx**2) + (2*g+np.roll(g,1,axis = 0))/dx
    xi = -u*dt
    y = a*(xi**3)+b*(xi**2)+g*xi+y
    g = 3*a*(xi**2)+2*b*xi+g
    return y,g
    
def analytical(i,dt):
    bmin = int((40+i*dt)%100)+1
    bmax = int((60+i*dt)%100)
    y = np.zeros_like(x)
    if bmin < 80:
        y[bmin:bmax] = 1
    else:
        y[bmin:] = 1
        y[:bmax] = 1
    return y

def plotupwind(dt):
    y = np.zeros_like(x)
    y[40:60] = 1
    for it in np.arange(0,t+dt,dt):
        plt.plot(x,y,'k-',linewidth = 5)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.xlim([0,100])
        plt.ylim([-0.4,1.2])
        plt.title("Time = %4.4d"%(it))
        y = upwind(y,dt)
        if np.round(it) in [10,200,400,600]:
            plt.savefig(f'upwind{np.round(it)}({dt}).png')
        plt.clf()
        plt.cla()
            

def plotleith(dt):
    y = np.zeros_like(x)
    y[40:60] = 1
    for it in np.arange(0,t+dt,dt):
        plt.plot(x,y,'k-',linewidth = 5)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.xlim([0,100])
        plt.ylim([-0.4,1.2])
        plt.title("Time = %4.4d"%(it))
        y = leith(y,dt)
        if np.round(it) in [10,200,400,600]:
            plt.savefig(f'Leith{np.round(it)}({dt}).png')
        plt.clf()
        plt.cla()
        

def plotCIP(dt):
    y = np.zeros_like(x)
    y[40:60] = 1
    g = np.zeros_like(x)
    g[40] = 1
    g[61] = -1
    for it in np.arange(0,t+dt,dt):
        plt.plot(x,y,'k-',linewidth = 5)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.xlim([0,100])
        plt.ylim([-0.4,1.2])
        plt.title("Time = %4.4d"%(it))
        y,g = CIP(y,g,dt)
        if np.round(it) in [10,200,400,600]:
            plt.savefig(f'CIP{np.round(it)}({dt}).png')
        plt.clf()
        plt.cla()
        

def plotanalytical(dt):
    y = np.zeros_like(x)
    y[40:60] = 1
    counter = -1
    for it in np.arange(0,t+dt,dt):
        counter += 1
        plt.plot(x,y,'k-',linewidth = 5)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.xlim([0,100])
        plt.ylim([-0.4,1.2])
        plt.title("Time = %4.4d"%(it))
        if np.round(it) in [10,200,400,600]:
            plt.savefig(f'analytical({dt}){np.round(it)}.png')
        plt.clf()
        plt.cla()
        y = analytical(counter+1,dt)

##Main program
x = np.arange(0,len_x+dx,dx)
fig = plt.figure(figsize = (10,10))
for dt in [0.5, 0.75, 1, 1.1]:
    plotupwind(dt)
    plotleith(dt)
    plotCIP(dt)
    plotanalytical(dt)

