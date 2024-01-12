import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define the function for the vector field (van der Pol model)
def vector_field(x, y, mu):
    u = y
    v = mu * (1 - x**2) * y - x
    return u, v

# Create the figure and axes
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.45)  # Adjust the bottom margin for sliders

# Set the initial parameter values and axes ranges
mu_init = 1.0
x_min, x_max = -3, 3
y_min, y_max = -3, 3

# Generate the initial vector field
x = np.linspace(x_min, x_max, 20)
y = np.linspace(y_min, y_max, 20)
X, Y = np.meshgrid(x, y)
U, V = vector_field(X, Y, mu_init)

# Plot the quiver plot of the vector field
quiver = ax.quiver(X, Y, U, V, scale=200, pivot='mid', color='blue')  # Set the color to blue

# Create sliders for parameter values
ax_mu = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_mu = Slider(ax_mu, 'mu', 0.0, 10.0, valinit=mu_init)

# Create sliders for axes ranges
ax_x_min = plt.axes([0.25, 0.2, 0.65, 0.03])
slider_x_min = Slider(ax_x_min, 'x_min', -10.0, 0.0, valinit=x_min)

ax_x_max = plt.axes([0.25, 0.15, 0.65, 0.03])
slider_x_max = Slider(ax_x_max, 'x_max', 0.0, 10.0, valinit=x_max)

ax_y_min = plt.axes([0.25, 0.3, 0.65, 0.03])
slider_y_min = Slider(ax_y_min, 'y_min', -10.0, 0.0, valinit=y_min)

ax_y_max = plt.axes([0.25, 0.25, 0.65, 0.03])
slider_y_max = Slider(ax_y_max, 'y_max', 0.0, 10.0, valinit=y_max)

# Update the vector field when sliders are changed
def update(val):
    mu = slider_mu.val
    x_min = slider_x_min.val
    x_max = slider_x_max.val
    y_min = slider_y_min.val
    y_max = slider_y_max.val

    x = np.linspace(x_min, x_max, 20)
    y = np.linspace(y_min, y_max, 20)
    X, Y = np.meshgrid(x, y)
    U, V = vector_field(X, Y, mu)

    quiver.set_UVC(U, V)

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    fig.canvas.draw_idle()

slider_mu.on_changed(update)
slider_x_min.on_changed(update)
slider_x_max.on_changed(update)
slider_y_min.on_changed(update)
slider_y_max.on_changed(update)

# Set the initial axis ranges
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_aspect('equal', adjustable='box')

# Show the plot
plt.show()