# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:47:51 2020

@author: artmenlope

Fun with scipy's odeint
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint


def acel_x(x, y):
    
    """X-component of the acceleration vector."""
    
    a_x = -np.cos(y)*np.sin(x)
    
    return a_x


def acel_y(x, y):
    
    """Y-component of the acceleration vector."""
    
    a_y = -np.sin(y)*np.cos(x)
    
    return a_y


def Mechanics(PositVeloc, t, n):
    
    """
    Function defining the mechanics of the points. Created to be used with the
    scipy.integrate.odeint function.
    
    Letting xi and yi be the x and y coordinates of the point i and vxi and vyi 
    its velocity components on each axis:
        
    PositVeloc must be a 1D Numpy array or a list of the form 
    [x1, vx1, y1, vy1, x2, vx2, y2, vy2, x3, vx3, y3, vy3, ...].
    
    Calling axi and ayi to the components of the acceleration of the point i,
    Mechanics returns an array ddt of the form 
    [vx1, ax1, vy1, ay1, vx2, ax2, vy2, ay2, vx3, ax3, vy3, ay3, ...]
    """
       
    PositVeloc = np.asarray(PositVeloc) # Array of positions and velocities.
    
    xs  = PositVeloc[0::4] # Set of x coordinates.
    vxs = PositVeloc[1::4] # Set of vx velocities.
    ys  = PositVeloc[2::4] # Set of y coordinates.
    vys = PositVeloc[3::4] # Set of vy velocities.
            
    axs = acel_x(xs, ys) # X-component of the accelerations. The acel_x function is defined externally.
    ays = acel_y(xs, ys) # Y-component of the accelerations. The acel_y function is defined externally.
    
    ddt_aux = np.stack((vxs, axs, vys, ays), axis=1) # Create a 2D Numpy array containing [vxi, axi, vyi, ayi] in each row.
    ddt = np.reshape(ddt_aux, (4*n**2)) # Reshape ddt_aux to be of the form [vx1, ax1, vy1, ay1, vx2, ax2, vy2, ay2, ...]

    return ddt


n = 50 # Number of points
lim = 1 # Limits of the point generation. The points will be generated on the square [-lim,lim]x[-lim,lim]
plotlim = lim # Plot visualization limits. Square of the form [-plotlim,plotlim]x[-plotlim,plotlim]

# Make a grid of points located at their initial positions.
x0 = np.linspace(-lim,lim,n)
y0 = np.linspace(-lim,lim,n)
X0, Y0 = np.meshgrid(x0, y0) 

# Reshape the grid to obtain an array containing in each row the initial 
# coordinates [x0i,y0i] of each point.
points = np.stack((X0, Y0), axis=-1).reshape((n**2,2))

x0s = points[:,0] # Set of initial x-coordinates. 1D array.
y0s = points[:,1] # Set of initial y-coordinates. 1D array.

# Initial velocity components of the points.
vx0s = np.zeros(n**2)
vy0s = np.zeros(n**2)

tf = 50 # Final time value.
dt = 0.1 # Time step.
t = np.arange(0, tf+dt, dt) # 1D array of time values.
nt = len(t) # Number of time steps.

# Create a 1D array of initial conditions for odeint. 
initCond_aux = np.stack((x0s, vx0s, y0s, vy0s), axis=1) # Create a 2D Numpy array containing [xi, vxi, yi, vyi] in each row. See the Mechanics() function for more details.
init_cond = np.reshape(initCond_aux, (4*n**2)) # Reshape initCond_aux to be of the form [x1, vx1, y1, vy1, x2, vx2, y2, vy2, ...].

# We solve the position of all the dots at any given time.
abserr = 1.0e-6
relerr = 1.0e-4
solutions = odeint(Mechanics, init_cond, t, args=(n,), atol=abserr, rtol=relerr)

# Get the coordinates and velocities of the points at each time step.
xs  = solutions.T[0::4]
vxs = solutions.T[1::4]
ys  = solutions.T[2::4]
vys = solutions.T[3::4]

# Create the figure and the axes objects.
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, xlim=(-plotlim,plotlim), ylim=(-plotlim,plotlim))
ax.set_aspect("equal")
ax.tick_params(axis='both',          
               which='both',      
               bottom=False,
               left=False, 
               labelbottom=False,
               labelleft=False) # Hide the ticks of each axis.


def anim(i):

        """
        Animation function. Used together with the FuncAnimation() function.
        i is the frame's number (or the time step).
        """
        
        # Clear the axes elements (delete the points of the previous frame).
        #ax.collections = []
        #ax.artists = []
        ax.lines = []
        
        # Get the point coordinates at the present time step i.
        x = np.asarray(xs[:,i])
        y = np.asarray(ys[:,i])
        
        # 'Plot with markers' is sometimes faster than a 'scatterplot'. 
        # See https://pybonacci.org/2014/09/09/microentrada-rendimiento-de-scatterplots-en-matplotlib/
        dots = ax.plot(x, y, 
                       color="black", 
                       alpha=1, 
                       linewidth=0,
                       marker="o",
                       markersize=3#,
                       #markerfacecolor="black"
                       )
                    
        # Scatter alternative
        # dots = ax.scatter(x, y, c="black", alpha=0.8, s=5)
        
        return dots


# Make the animation.
anim = FuncAnimation(fig, 
                     func=anim, 
                     frames=nt, 
                     interval=0, 
                     blit=True, 
                     repeat=False)



# Snippet for saving the results.

# anim.save('<Path-where-the-video-will-be-stored>.mp4', writer="ffmpeg", fps=60)
# import os
# os.system("ffmpeg -i <Path-where-the-video-will-be-stored>.mp4 <Path-where-the-video-will-be-stored>.gif")