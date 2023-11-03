import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to define the equations of motion for the damped pendulum
def damped_pendulum(y, t, g, L, b):
    theta, omega = y
    dydt = [omega, -b * omega - g / L * np.sin(theta)]
    return dydt

# Parameters
g = 9.8  # Acceleration due to gravity (m/s^2)
L = 1.0  # Length of the pendulum (m)
b = 0.  # Damping coefficient

# Initial conditions
theta0 = 0  # Initial angle (radians)
omega0 = 0.5*np.sqrt(4*g/L)       # Initial angular velocity (radians/s)
y0 = [theta0, omega0]

# Time span
t_start = 0.0
t_end = 10.0
t_step = 0.01
t_span = np.arange(t_start, t_end, t_step)

# Solve the differential equations
sol = odeint(damped_pendulum, y0, t_span, args=(g, L, b))

# Extract the solution
theta = sol[:, 0]
omega = sol[:, 1]

# Create subplots for animations and plots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Pendulum animation
axs[0, 0].set_xlim(-1.1*L, 1.1*L)
axs[0, 0].set_ylim(-1.1*L, 1.1*L)
axs[0, 0].set_aspect('equal', adjustable='box')
pendulum_line, = axs[0, 0].plot([], [], '-o')
axs[0, 0].set_title('Pendulum Movement')

# Phase space trajectory
axs[0, 1].set_xlim(-1.1*np.pi, 1.1*np.pi)
axs[0, 1].set_ylim(-1.1*np.sqrt(4*g/L), 1.1*np.sqrt(4*g/L))
axs[0, 1].set_xlabel('Angle (radians)')
axs[0, 1].set_ylabel('Angular Speed (radians/s)')
phase_space_line, = axs[0, 1].plot([], [])
axs[0, 1].set_title('Phase Space Trajectory')

# Angle variation over time
axs[1, 0].set_xlim(-0.1, 1.1*t_end)
axs[1, 0].set_ylim(-1.1*np.pi, 1.1*np.pi)
axs[1, 0].set_xlabel('Time (s)')
axs[1, 0].set_ylabel('Angle (radians)')
angle_line, = axs[1, 0].plot([], [])
axs[1, 0].set_title('Angle Variation over Time')

# Angular speed variation over time
axs[1, 1].set_xlim(-0.1, 1.1*t_end)
axs[1, 1].set_ylim(-1.1*np.sqrt(4*g/L), 1.1*np.sqrt(4*g/L))
axs[1, 1].set_xlabel('Time (s)')
axs[1, 1].set_ylabel('Angular Speed (radians/s)')
angular_speed_line, = axs[1, 1].plot([], [])
axs[1, 1].set_title('Angular Speed Variation over Time')

# Animation function
def animate(i):
    # Pendulum movement
    x = L * np.sin(theta[i])
    y = -L * np.cos(theta[i])
    pendulum_line.set_data([0, x], [0, y])

    # Angle variation over time
    angle_line.set_data(t_span[:i], theta[:i])

    # Angular speed variation over time
    angular_speed_line.set_data(t_span[:i], omega[:i])

    # Phase space trajectory
    phase_space_line.set_data(theta[:i], omega[:i])

# Set up the animation
ani = FuncAnimation(fig, animate, frames=len(t_span), interval=1)

# Show the plot
plt.tight_layout()
plt.show()