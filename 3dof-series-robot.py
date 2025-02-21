try:
    import numpy as np
    import matplotlib.pyplot as plt
except ModuleNotFoundError as e:
    print("Required modules not found. Please install them using: pip install numpy matplotlib")
    raise e

def forward_kinematics(theta1, theta2, theta3, l1=1, l2=1, l3=1):
    """Compute the forward kinematics of a 3R planar robot."""
    
    # Joint positions
    x0, y0 = 0, 0  # Base
    x1 = l1 * np.cos(theta1)
    y1 = l1 * np.sin(theta1)
    x2 = x1 + l2 * np.cos(theta1 + theta2)
    y2 = y1 + l2 * np.sin(theta1 + theta2)
    x3 = x2 + l3 * np.cos(theta1 + theta2 + theta3)
    y3 = y2 + l3 * np.sin(theta1 + theta2 + theta3)
    
    return [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]

def plot_robot(joint_positions):
    """Plot the 3R planar robot."""
    
    x_vals, y_vals = zip(*joint_positions)
    
    plt.figure(figsize=(5, 5))
    plt.plot(x_vals, y_vals, '-o', markersize=8, linewidth=3)
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.grid(True)
    plt.title("3R Planar Robot")
    plt.show()

# Example usage
theta1, theta2, theta3 = np.radians([30, 45, -30])  # Joint angles in degrees
joint_positions = forward_kinematics(theta1, theta2, theta3)
plot_robot(joint_positions)
