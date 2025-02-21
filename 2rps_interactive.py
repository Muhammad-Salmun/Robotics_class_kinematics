import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def rotation_matrix(theta):
    """Returns the 2D rotation matrix for a given angle theta."""
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

def inverse_kinematics(theta_p, l=2, extension=1):
    """Compute the inverse kinematics of a 2-RPS parallel manipulator with extended platform."""
    base1 = np.array([1, 1])
    base2 = np.array([5, 1])
    
    # Platform attachment points relative to its center
    p1_local = np.array([-1, 0])
    p2_local = np.array([1, 0])
    
    # Extended platform attachment points
    p1_ext_local = np.array([-1 - extension, 0])
    p2_ext_local = np.array([1 + extension, 0])
    
    # Apply rotation
    rot = rotation_matrix(theta_p)
    p1_global = rot @ p1_local
    p2_global = rot @ p2_local
    p1_ext_global = rot @ p1_ext_local
    p2_ext_global = rot @ p2_ext_local
    
    # Global positions of platform joints
    platform_center = (base1 + base2) / 2 + np.array([0, l])
    b1 = platform_center + p1_global
    b2 = platform_center + p2_global
    b1_ext = platform_center + p1_ext_global
    b2_ext = platform_center + p2_ext_global
    
    return [tuple(base1), tuple(b1), tuple(b2), tuple(base2), tuple(b1_ext), tuple(b2_ext)]


def update_plot(val):
    """Update plot based on slider value."""
    theta_p_deg = theta_slider.val  # Get value from slider
    theta_p = np.radians(theta_p_deg)
    joint_positions = inverse_kinematics(theta_p)
    
    x_vals, y_vals = zip(*joint_positions)
    
    ax.clear()
    ax.plot([x_vals[0], x_vals[1]], [y_vals[0], y_vals[1]], '-o', markersize=8, linewidth=3, label='Base to S1')
    ax.plot([x_vals[3], x_vals[2]], [y_vals[3], y_vals[2]], '-o', markersize=8, linewidth=3, label='Base to S2')
    ax.plot([x_vals[1], x_vals[2]], [y_vals[1], y_vals[2]], '-o', markersize=8, linewidth=3, label='Platform')
    ax.plot([x_vals[4], x_vals[5]], [y_vals[4], y_vals[5]], '--', linewidth=2, label='Extended Platform')

    ax.set_xlim(-3, 9)
    ax.set_ylim(-2, 4)
    ax.grid(True)
    ax.set_title(f"2-RPS Parallel Manipulator (θ = {theta_p_deg:.1f}°)")
    ax.legend()
    plt.draw()

# Create plot
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)  # Space for the slider

# Add slider
ax_theta = plt.axes([0.1, 0.1, 0.8, 0.03])  # Position of the slider
theta_slider = Slider(ax_theta, 'Theta', -90, 90, valinit=0)

# Initial plot setup
theta_slider.on_changed(update_plot)  # Call update function on change

update_plot(None)
plt.show()
