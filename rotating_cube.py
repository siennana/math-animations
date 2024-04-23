import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Function to update the rotation angle
def update_angle(num, ax, fig):
    ax.cla()  # Clear current axes
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])

    # Define cube vertices
    vertices = np.array([[1, 1, 1],
                         [-1, 1, 1],
                         [-1, -1, 1],
                         [1, -1, 1],
                         [1, 1, -1],
                         [-1, 1, -1],
                         [-1, -1, -1],
                         [1, -1, -1]])

    # Define cube edges
    edges = [[0, 1, 2, 3, 0],
             [4, 5, 6, 7, 4],
             [0, 4],
             [1, 5],
             [2, 6],
             [3, 7]]

    # Rotate cube vertices
    angle = np.deg2rad(num)
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                [np.sin(angle), np.cos(angle), 0],
                                [0, 0, 1]])
    rotated_vertices = np.dot(vertices, rotation_matrix)

    # Plot cube
    for edge in edges:
        ax.plot3D(rotated_vertices[edge, 0], rotated_vertices[edge, 1], rotated_vertices[edge, 2], color='b')

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set axis limits
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Set initial view angle
ax.view_init(elev=10., azim=30)

# Create animation
ani = animation.FuncAnimation(fig, update_angle, frames=np.arange(0, 360, 1), fargs=(ax, fig), interval=50)

# Show animation
plt.show()

