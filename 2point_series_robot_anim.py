import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# Link lengths
L1 = 1.0  # Length of first link
L2 = 1.0  # Length of second link

def forward_kinematics(theta1, theta2):
    """Computes the (x, y) positions of the two links."""
    x1 = L1 * np.cos(np.radians(theta1))
    y1 = L1 * np.sin(np.radians(theta1))
    
    x2 = x1 + L2 * np.cos(np.radians(theta1 + theta2))
    y2 = y1 + L2 * np.sin(np.radians(theta1 + theta2))
    
    return (0, 0), (x1, y1), (x2, y2)

def update(val):
    theta1 = theta1_slider.val
    theta2 = theta2_slider.val
    
    joint1, joint2, end_effector = forward_kinematics(theta1, theta2)
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("2-Point Serial Robot")
    ax.grid()
    
    ax.plot([joint1[0], joint2[0]], [joint1[1], joint2[1]], 'bo-', linewidth=3)
    ax.plot([joint2[0], end_effector[0]], [joint2[1], end_effector[1]], 'ro-', linewidth=3)
    ax.scatter(*end_effector, color='g', s=100, label="End Effector")
    ax.legend()
    fig.canvas.draw_idle()

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)

ax_theta1 = plt.axes([0.2, 0.1, 0.65, 0.03])
ax_theta2 = plt.axes([0.2, 0.15, 0.65, 0.03])

theta1_slider = Slider(ax_theta1, 'Theta1', -180, 180, valinit=0)
theta2_slider = Slider(ax_theta2, 'Theta2', -180, 180, valinit=0)

theta1_slider.on_changed(update)
theta2_slider.on_changed(update)

update(None)
plt.show()