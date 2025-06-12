import numpy as np
import plotly.graph_objects as go

# Helper function to create sphere
def create_sphere(center, radius, resolution=20):
    u, v = np.mgrid[0:2*np.pi:resolution*1j, 0:np.pi:resolution*1j]
    x = radius * np.cos(u) * np.sin(v) + center[0]
    y = radius * np.sin(u) * np.sin(v) + center[1]
    z = radius * np.cos(v) + center[2]
    return go.Surface(x=x, y=y, z=z, colorscale='Blues', showscale=False)

# Helper function to create cylinder
def create_cylinder(start, height, radius, axis='z', resolution=20):
    theta = np.linspace(0, 2*np.pi, resolution)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = np.linspace(0, height, resolution)
    
    if axis == 'z':
        x, y = np.meshgrid(x, y)
        z = np.full_like(x, height) + start[2]
        return go.Surface(x=x + start[0], y=y + start[1], z=z, colorscale='Reds', showscale=False)

# Helper function to create cube
def create_cube(center, size):
    x0, y0, z0 = center
    d = size / 2
    vertices = [
        [x0-d, y0-d, z0-d], [x0+d, y0-d, z0-d], [x0+d, y0+d, z0-d], [x0-d, y0+d, z0-d],
        [x0-d, y0-d, z0+d], [x0+d, y0-d, z0+d], [x0+d, y0+d, z0+d], [x0-d, y0+d, z0+d],
    ]
    I = [0, 0, 0, 7, 4, 5, 2, 3, 1, 6, 6, 6]
    J = [1, 2, 3, 4, 5, 1, 3, 0, 5, 2, 7, 3]
    K = [2, 3, 0, 0, 1, 2, 0, 1, 6, 3, 6, 7]
    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    z = [v[2] for v in vertices]
    return go.Mesh3d(x=x, y=y, z=z, i=I, j=J, k=K, color='green', opacity=0.5)

# Assemble the hero
fig = go.Figure()

# Head (sphere)
fig.add_trace(create_sphere(center=[0, 0, 4], radius=0.8))

# Eyes (spheres)
fig.add_trace(create_sphere(center=[-0.3, 0.7, 4.2], radius=0.1))
fig.add_trace(create_sphere(center=[0.3, 0.7, 4.2], radius=0.1))

# Body (cube)
fig.add_trace(create_cube(center=[0, 0, 2.5], size=1.2))

# Left arm (cylinder)
fig.add_trace(create_cylinder(start=[-1.1, 0, 2.5], height=1.2, radius=0.2))

# Right arm (cylinder)
fig.add_trace(create_cylinder(start=[1.1, 0, 2.5], height=1.2, radius=0.2))

# Left leg (cylinder)
fig.add_trace(create_cylinder(start=[-0.4, 0, 0], height=1.5, radius=0.2))

# Right leg (cylinder)
fig.add_trace(create_cylinder(start=[0.4, 0, 0], height=1.5, radius=0.2))

# Layout settings
fig.update_layout(scene=dict(
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    zaxis=dict(visible=False),
    aspectratio=dict(x=1, y=1, z=1.5)
))

fig.show()