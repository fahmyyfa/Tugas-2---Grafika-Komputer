import numpy as np
import plotly.graph_objects as go
import math
from js import document
import plotly.io as pio

# Fungsi primitif dasar
def create_cylinder(x0, y0, z0, r, h, color='blue'):
    theta = np.linspace(0, 2*np.pi, 30)
    z = np.linspace(0, h, 2)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = r * np.cos(theta_grid) + x0
    y_grid = r * np.sin(theta_grid) + y0
    z_grid += z0
    return go.Surface(x=x_grid, y=y_grid, z=z_grid, colorscale=[[0, color], [1, color]], showscale=False)

def create_cone(x0, y0, z0, r, h, color='red'):
    theta = np.linspace(0, 2*np.pi, 30)
    z = np.linspace(0, h, 2)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = (r * (1 - z_grid/h)) * np.cos(theta_grid) + x0
    y_grid = (r * (1 - z_grid/h)) * np.sin(theta_grid) + y0
    z_grid += z0
    return go.Surface(x=x_grid, y=y_grid, z=z_grid, colorscale=[[0, color], [1, color]], showscale=False)

def create_box(x0, y0, z0, dx, dy, dz, color='green'):
    x = np.array([0, 1, 1, 0, 0, 1, 1, 0]) * dx + x0 - dx/2
    y = np.array([0, 0, 1, 1, 0, 0, 1, 1]) * dy + y0 - dy/2
    z = np.array([0, 0, 0, 0, 1, 1, 1, 1]) * dz + z0 - dz/2
    i = [0, 0, 0, 7, 4, 5]
    j = [1, 2, 4, 6, 5, 6]
    k = [2, 3, 5, 2, 6, 7]
    return go.Mesh3d(x=x, y=y, z=z, i=i, j=j, k=k, color=color, opacity=1)

# Bangun roket dari primitif
badan = create_cylinder(0, 0, 0, 1, 5, color='silver')
kepala = create_cone(0, 0, 5, 1, 2, color='red')
sayap1 = create_box(-1.5, 0, 1, 0.2, 2, 1, color='blue')
sayap2 = create_box(1.5, 0, 1, 0.2, 2, 1, color='blue')
sayap3 = create_box(0, -1.5, 1, 2, 0.2, 1, color='blue')
ekor = create_cylinder(0, 0, -1.5, 0.5, 1, color='orange')

# Gabungkan ke dalam satu scene
fig = go.Figure(data=[badan, kepala, sayap1, sayap2, sayap3, ekor])
fig.update_layout(scene=dict(
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    zaxis=dict(visible=False)
))

# Render ke elemen HTML
div = document.getElementById("plot")
html = pio.to_html(fig, include_plotlyjs=False, full_html=False)
div.innerHTML = html
