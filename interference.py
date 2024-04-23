import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)

# Initialize line objects for the two sine waves and the interference wave
line1, = ax.plot([], [], lw=2, label='Sine wave 1')
line2, = ax.plot([], [], lw=2, label='Sine wave 2')
line_interference, = ax.plot([], [], lw=2, label='Interference wave', linestyle='--')

# Set legend
ax.legend()

# Initialization function: plot the background of each frame
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line_interference.set_data([], [])
    return line1, line2, line_interference

# Animation function: this is called sequentially
def animate(i):
    x = np.linspace(0, 10, 1000)
    # Wave parameters
    amplitude1 = 1
    frequency1 = 1
    phase1 = 0.05 * i  # Move wave 1 to the right
    
    amplitude2 = 1
    frequency2 = 1
    phase2 = -0.05 * i  # Move wave 2 to the left
    
    # Calculate wave values
    y1 = amplitude1 * np.sin(2 * np.pi * frequency1 * x + phase1)
    y2 = amplitude2 * np.sin(2 * np.pi * frequency2 * x + phase2)
    y_interference = y1 + y2  # Interference
    
    # Update line data
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    line_interference.set_data(x, y_interference)
    
    return line1, line2, line_interference

# Create the animation object
ani = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

# Show the animation
plt.show()

