import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
wavelength = 0.5
slit_distance = 10.0
screen_distance = 200.0
screen_size = 400

# Function to calculate intensity at a point (x, y)
def intensity(x, y, t):
    slit1 = np.sin(2 * np.pi * (x - slit_distance * np.sin(t)) / wavelength)
    slit2 = np.sin(2 * np.pi * (x + slit_distance * np.sin(t)) / wavelength)
    return (slit1 + slit2)**2

# Create figure
fig, ax = plt.subplots()

# Initial plot
x = np.linspace(-screen_size/2, screen_size/2, screen_size)
y = np.linspace(-screen_size/2, screen_size/2, screen_size)
X, Y = np.meshgrid(x, y)
Z = intensity(X, Y, 0)
im = ax.imshow(Z, cmap='gray', interpolation='nearest')

# Animation update function
def update(t):
    Z = intensity(X, Y, t)
    im.set_array(Z)
    return im,

# Animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 100),
                              interval=50, blit=True)

plt.show()

