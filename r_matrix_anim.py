import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def rotate_point(x, y, theta):
    theta = np.radians(theta)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                [np.sin(theta), np.cos(theta)]])
    new_x, new_y = np.dot(rotation_matrix, np.array([x, y]))
    return new_x, new_y

# Original point
x, y = 3, 2
theta = 10  # Rotation angle
new_x, new_y = rotate_point(x, y, theta)

fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Rotation of Axes by 45 Degrees")
ax.grid()

# Initial point
point, = ax.plot(x, y, 'bo', markersize=8, label='Original Point')
rotated_point, = ax.plot([], [], 'ro', markersize=8, label='Rotated Point')

# Initial axes
x_axis, = ax.plot([-5, 5], [0, 0], 'k-', linewidth=1.5, label='Original Axes')
y_axis, = ax.plot([0, 0], [-5, 5], 'k-', linewidth=1.5)
rotated_x_axis, = ax.plot([], [], 'g--', linewidth=1.5, label='Rotated Axes')
rotated_y_axis, = ax.plot([], [], 'g--', linewidth=1.5)

text_original = ax.text(x + 0.2, y, f'({x}, {y})', fontsize=12, color='blue')
text_rotated = ax.text(new_x + 0.2, new_y, f'({new_x:.2f}, {new_y:.2f})', fontsize=12, color='red', visible=False)

def animate(i):
    angle = i * (theta / 100)  # Smooth rotation
    rx1, ry1 = rotate_point(5, 0, angle)
    rx2, ry2 = rotate_point(-5, 0, angle)
    ry1_x, ry1_y = rotate_point(0, 5, angle)
    ry2_x, ry2_y = rotate_point(0, -5, angle)
    
    rotated_x_axis.set_data([rx2, rx1], [ry2, ry1])
    rotated_y_axis.set_data([ry2_x, ry1_x], [ry2_y, ry1_y])
    
    if i == 100:
        rotated_point.set_data(new_x, new_y)
        text_rotated.set_visible(True)
    
    return rotated_x_axis, rotated_y_axis, rotated_point, text_rotated

ani = animation.FuncAnimation(fig, animate, frames=101, interval=50, blit=False)
ax.legend()
plt.show()
