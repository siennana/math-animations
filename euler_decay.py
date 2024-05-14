import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 2.5, 250)
f = np.exp(2*np.pi*4/2.5*1j*t)
e = np.exp(-0.5*t)
fe = f * e

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update(frame):
    ax.clear()
    ax.plot3D(t, np.real(fe), np.imag(fe), linewidth=2)
    ax.plot3D(t, np.real(fe), np.zeros_like(t)-1.5)
    ax.plot3D(t, np.zeros_like(t)-2, np.imag(fe))
    ax.grid(True)
    ax.set_xlim([-1, 3])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-1.5, 1.5])
    ax.view_init(elev=10, azim=frame)

ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)
plt.show()

