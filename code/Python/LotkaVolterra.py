import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to define the equations of motion for the Lotka-Volterra Model
def Lotka_Volterra(u, t, alpha_xy, alpha_yx, rho):
    x, y = u
    dydt = [x*(1-x-alpha_xy*y), rho*y*(1-y-alpha_yx*x)]
    return dydt

# Parameters
alpha_xy = 0.5  
alpha_yx = 0.5  # Length of the pendulum (m)
rho = 1.0  # Damping coefficient

# Time span
t_start = 0.0
t_end = 10.0
t_step = 0.01
t_span = np.arange(t_start, t_end, t_step)

# Create subplots for animations and plots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Initial conditions
x0 = 0.01  # Initial angle (radians)
y0 = 0.0001       # Initial angular velocity (radians/s)
u0 = [x0, y0]

# Solve the differential equations
sol = odeint(Lotka_Volterra, u0, t_span, args=(alpha_xy, alpha_yx, rho))

# Extract the solution
x = sol[:, 0]
y = sol[:, 1]

# Phase space trajectory
axs[0, 1].set_xlim(0, 0)
axs[0, 1].set_ylim(0, 0)
axs[0, 1].set_xlabel(r'$x$')
axs[0, 1].set_ylabel(r'$y$')
phase_space_line, = axs[0, 1].plot([], [])
axs[0, 1].set_title('Phase Space Trajectory')

# x variation over time
axs[1, 0].set_xlim(0, t_end)
axs[1, 0].set_ylim(0, 2)
axs[1, 0].set_xlabel('Time')
axs[1, 0].set_ylabel(r'$x$')
x_line, = axs[1, 0].plot([], [])
axs[1, 0].set_title(r'$x$ Variation over Time')

# y variation over time
axs[1, 1].set_xlim(0, t_end)
axs[1, 1].set_ylim(0, 0)
axs[1, 1].set_xlabel('Time')
axs[1, 1].set_ylabel(r'$y$')
y_line, = axs[1, 1].plot([], [])
axs[1, 1].set_title(r'$y$ Variation over Time')

# Animation function
def animate(i):

    # Angle variation over time
    x_line.set_data(t_span[:i], x[:i])

    # Angular speed variation over time
    y_line.set_data(t_span[:i], y[:i])

    # Phase space trajectory
    phase_space_line.set_data(x[:i], y[:i])

# Set up the animation
ani = FuncAnimation(fig, animate, frames=len(t_span), interval=1)

# Show the plot
plt.tight_layout()
plt.show()