import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

# Function to define the equations of motion 
def model(phi, time, rotation_speed):
    gamma = radius * rotation_speed ** 2 / g
    dphi = np.sin(phi) * (gamma * np.cos(phi) - 1)
    return dphi

# Define the parameters
radius = 1.0  # Radius of the circle
theta = np.linspace(0, 2 * np.pi, 100)  # Angle values from 0 to 2*pi
time = np.linspace(0, 50, 5000)
g = 9.8  # Acceleration due to gravity (m/s^2)
rotation_speed = 1 * np.sqrt(g / radius)

# Initial conditions
phi0 = 3.14

sol = odeint(model, phi0, time, args=(rotation_speed,))
phi = sol[:, 0]

# Generate the coordinates
x = radius * np.cos(theta)
z = radius * np.sin(theta)
y = np.zeros_like(x)  # Z-coordinate is set to 0 for all points

# Create a figure with two subplots
fig = plt.figure(figsize=(12,6))

# First subplot: 3D animation of the overdamped bead on rotating hoop
ax1 = fig.add_subplot(121, projection='3d')

# Initialize the plot objects
circle, = ax1.plot([], [], [])
bead, = ax1.plot([], [], [], 'o', color="C2")
ax1.plot([0, 0], [0, 0], [-1.2, 1.2], color="C1")
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Overdamped bead on rotating hoop')
ax1.set_box_aspect([1, 1, 1])
ax1.set_xlim(-1, 1)
ax1.set_ylim(-1, 1)
ax1.set_zlim(-1, 1)
ax1.xaxis.set_ticks([])
ax1.yaxis.set_ticks([])
ax1.zaxis.set_ticks([])

# Define the rotation matrix
rotation_matrix = np.array([[np.cos(0), -np.sin(0), 0],
                            [np.sin(0), np.cos(0), 0],
                            [0, 0, 1]])

# Function to update the plot for each animation frame
def update_3d(frame):
    rotation_angle = time[frame] * rotation_speed

    rotation_matrix[0, 0] = np.cos(rotation_angle)
    rotation_matrix[0, 1] = -np.sin(rotation_angle)
    rotation_matrix[1, 0] = np.sin(rotation_angle)
    rotation_matrix[1, 1] = np.cos(rotation_angle)

    coordinates = np.column_stack([x, y, z])
    rotated_coordinates = np.dot(coordinates, rotation_matrix.T)

    x_rotated = rotated_coordinates[:, 0]
    y_rotated = rotated_coordinates[:, 1]
    z_rotated = rotated_coordinates[:, 2]

    bead_coordinates = np.array([radius * np.sin(phi[frame]), 0, -radius * np.cos(phi[frame])])
    rotated_bead_coordinates = np.dot(bead_coordinates, rotation_matrix.T)

    x_bead_rotated = rotated_bead_coordinates[0]
    y_bead_rotated = rotated_bead_coordinates[1]
    z_bead_rotated = rotated_bead_coordinates[2]

    circle.set_data(x_rotated, y_rotated)
    circle.set_3d_properties(z_rotated)
    bead.set_data(x_bead_rotated, y_bead_rotated)
    bead.set_3d_properties(z_bead_rotated)

    return circle, bead

# Calculate the total number of frames
total_frames = len(time)

# Create the animation for the first subplot
animation_3d = FuncAnimation(fig, update_3d, frames=total_frames, interval=50, blit=True)

# Second subplot: Animation of the time evolution of variable phi
ax2 = fig.add_subplot(122)
ax2.set_xlim(0, max(time))
ax2.set_ylim(-0.05, 3.2)
ax2.set_xlabel('Time')
ax2.set_ylabel(r'$\phi$')
ax2.set_title(r'Time Evolution of $\phi$')

line, = ax2.plot([], [], color='C0')

def update_phi(frame):
    line.set_data(time[:frame], phi[:frame])
    return line,

# Create the animation for the second subplot
animation_phi = FuncAnimation(fig, update_phi, frames=total_frames, interval=50, blit=True)

# Display the animations
plt.tight_layout()
plt.show()