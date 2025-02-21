import numpy as np
import matplotlib.pyplot as plt

def rotation_matrix(theta):
    """Returns the 2D rotation matrix for a given angle theta."""
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

def inverse_kinematics(theta_p, l=2, platform_width=2, extension=1):
    """Compute the inverse kinematics of a 2-RPS parallel manipulator with extended platform."""
    # Base joint positions (fixed)
    base1 = np.array([1, 1])
    base2 = np.array([5, 1])
    
    # Platform attachment points relative to its center (corrected order)
    p1_local = np.array([-1, 0])
    p2_local = np.array([1, 0])
    
    # Extend platform beyond joints
    p1_ext_local = np.array([-1 - extension, 0])
    p2_ext_local = np.array([1 + extension, 0])
    
    # Apply rotation to platform points
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
    
    # Compute lengths of s1 and s2
    s1 = np.linalg.norm(b1 - base1)
    s2 = np.linalg.norm(b2 - base2)
    
    return s1, s2, [tuple(base1), tuple(b1), tuple(b2), tuple(base2), tuple(b1_ext), tuple(b2_ext)]

def plot_manipulator(joint_positions):
    """Plot the 2-RPS parallel manipulator with extended platform."""
    x_vals, y_vals = zip(*joint_positions)
    
    plt.figure(figsize=(6, 6))
    plt.plot([x_vals[0], x_vals[1]], [y_vals[0], y_vals[1]], '-o', markersize=8, linewidth=3, label='Base to S1')
    plt.plot([x_vals[3], x_vals[2]], [y_vals[3], y_vals[2]], '-o', markersize=8, linewidth=3, label='Base to S2')
    plt.plot([x_vals[1], x_vals[2]], [y_vals[1], y_vals[2]], '-o', markersize=8, linewidth=3, label='Platform')
    plt.plot([x_vals[4], x_vals[5]], [y_vals[4], y_vals[5]], '--', linewidth=2, label='Extended Platform')
    
    plt.xlim(-3, 9)
    plt.ylim(-2, 4)
    plt.grid(True)
    plt.title("2-RPS Parallel Manipulator with Extended Platform")
    plt.legend()
    plt.show()

# User input for platform rotation angle
theta_p_deg = float(input("Enter the platform rotation angle (-90 to 90 degrees): "))
while theta_p_deg < -90 or theta_p_deg > 90:
    print("Invalid input! Please enter a value between -90 and 90.")
    theta_p_deg = float(input("Enter the platform rotation angle (-90 to 90 degrees): "))

theta_p = np.radians(theta_p_deg)  # Convert degrees to radians
s1, s2, joint_positions = inverse_kinematics(theta_p)
print(f"Computed lengths: s1 = {s1:.3f}, s2 = {s2:.3f}")
plot_manipulator(joint_positions)
