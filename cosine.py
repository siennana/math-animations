import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))

# Circle parameters
radius = 1
theta = np.linspace(0, 2*np.pi, 100)

# Initial point positions
point_radius = 0.05
point_x_circle = radius
point_y_circle = 0
point_x_xaxis = 0
point_y_xaxis = 0

# Create circle plot
circle = ax1.plot(radius * np.cos(theta), radius * np.sin(theta), 'b-')[0]
point_circle = ax1.plot(point_x_circle, point_y_circle, 'ro')[0]
point_xaxis = ax1.plot(point_x_xaxis, point_y_xaxis, 'go')[0]

# Set axis limits for circle plot
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax1.set_aspect('equal')

# Text annotations
theta_text = ax1.text(1.2, 1.4, '', fontsize=12)
x_axis_text = ax1.text(1.2, 1.3, '', fontsize=12)

# Create x-axis plot
x_data = np.linspace(0, 2*np.pi, 1000)
y_data = np.cos(x_data)
cosine_curve, = ax2.plot(x_data, y_data, 'b-')

# Set axis limits for x-axis plot
ax2.set_xlim(0, 2*np.pi)
ax2.set_ylim(-1.2, 1.2)

# Text annotation
theta_cos_text = ax2.text(6, 0.5, '', fontsize=12)

# Set aspect ratio for cosine plot to be equal to circle plot
ax2.set_aspect('equal')

# Initialization function: plot the background of each frame
def init():
    point_circle.set_data([], [])
    point_xaxis.set_data([], [])
    theta_text.set_text('')
    x_axis_text.set_text('')
    cosine_curve.set_data([], [])
    theta_cos_text.set_text('')
    return point_circle, point_xaxis, theta_text, x_axis_text, cosine_curve, theta_cos_text

# Animation function: this is called sequentially
def animate(i):
    # Update point position on circle
    angle = 2 * np.pi * i / 200
    point_x_circle = radius * np.cos(angle)
    point_y_circle = radius * np.sin(angle)
    point_circle.set_data(point_x_circle, point_y_circle)
    
    # Update x-axis point position
    point_x_xaxis = radius * np.cos(angle)
    point_xaxis.set_data(point_x_xaxis, point_y_xaxis)
    
    # Update text annotations
    theta_text.set_text(r'$\theta$: {:.2f}'.format(angle))
    x_axis_text.set_text(r'$x$: {:.2f}'.format(point_x_xaxis))
    
    # Update cosine curve
    cosine_curve.set_data(x_data, np.cos(x_data - angle))
    theta_cos_text.set_text(r'$\theta$: {:.2f}'.format(angle))
    
    return point_circle, point_xaxis, theta_text, x_axis_text, cosine_curve, theta_cos_text

# Create the animation object
ani = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

# Show the animation
plt.show()

