import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def lotka_volterra(t, r, alpha, beta, rho):
    """
    Lotka-Volterra model for competition derivatives.
    """
    x, y = r
    dx = x * (1 - x - beta * y)
    dy = rho * y * (1 - y - alpha * x)
    return dx, dy

# Set parameter values
alpha_init = 1.5
beta_init = 1.5
rho_init = 1.0

# Set up the grid
x = np.linspace(0, 1.2, 20)
y = np.linspace(0, 1.2, 20)
X, Y = np.meshgrid(x, y)

# Create the figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.35)  # Adjust the position of the sliders

# Set the axis limits
ax.set_xlim([-0.1, 1.3])
ax.set_ylim([-0.1, 1.3])

# Plot the vector field
quiver = ax.quiver(X, Y, X * (1 - X - beta_init * Y), rho_init * Y * (1 - Y - alpha_init * X))

# Plot the steady states
ax.plot([0, 0, 1, (1 - beta_init) / (1 - alpha_init * beta_init)],
        [0, 1, 0, (1 - alpha_init) / (1 - alpha_init * beta_init)],
        'o', color="C1")

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Lotka-Volterra Model - Vector Field of Derivatives')

# Make axis equally sized
ax.set_aspect('equal')

# Create sliders
ax_alpha = plt.axes([0.25, 0.2, 0.65, 0.03])
slider_alpha = Slider(ax_alpha, 'Alpha', 0.1, 3.0, valinit=alpha_init)

ax_beta = plt.axes([0.25, 0.15, 0.65, 0.03])
slider_beta = Slider(ax_beta, 'Beta', 0.1, 3.0, valinit=beta_init)

ax_rho = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_rho = Slider(ax_rho, 'Rho', 0.1, 3.0, valinit=rho_init)

# Update the vector field when sliders are changed
def update(val):
    alpha = slider_alpha.val
    beta = slider_beta.val
    rho = slider_rho.val
    quiver.set_UVC(X * (1 - X - beta * Y), rho * Y * (1 - Y - alpha * X))

    # Update the positions of the steady states
    ss1 = [0, 0]
    ss2 = [0, 1]
    ss3 = [1, 0]
    ss4 = [(1 - beta) / (1 - alpha * beta), (1 - alpha) / (1 - alpha * beta)]

    ax.lines[0].set_data([ss1[0], ss2[0], ss3[0], ss4[0]], [ss1[1], ss2[1], ss3[1], ss4[1]])

    fig.canvas.draw_idle()

slider_alpha.on_changed(update)
slider_beta.on_changed(update)
slider_rho.on_changed(update)

# Show the plot
plt.show()