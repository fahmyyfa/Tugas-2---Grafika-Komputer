import plotly.graph_objects as go
import numpy as np

def create_sphere(x0, y0, z0, r, color):
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = x0 + r * np.cos(u) * np.sin(v)
    y = y0 + r * np.sin(u) * np.sin(v)
    z = z0 + r * np.cos(v)
    return go.Surface(x=x, y=y, z=z, colorscale=[[0, color], [1, color]], showscale=False)

def create_cylinder(x0, y0, z0, r, h, axis='z', color='blue'):
    theta = np.linspace(0, 2*np.pi, 20)
    z = np.linspace(0, h, 2)
    theta, z = np.meshgrid(theta, z)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    if axis == 'z':
        x += x0
        y += y0
        z += z0
    elif axis == 'x':
        z, x = x + x0, z + z0
        y += y0
    elif axis == 'y':
        z, y = y + y0, z + z0
        x += x0
    return go.Surface(x=x, y=y, z=z, colorscale=[[0, color], [1, color]], showscale=False)

def create_cone(x0, y0, z0, r, h, color='orange'):
    theta = np.linspace(0, 2*np.pi, 30)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = np.zeros_like(theta)
    x = np.vstack((x, np.zeros_like(x))) + x0
    y = np.vstack((y, np.zeros_like(y))) + y0
    z = np.vstack((z, np.full_like(z, h))) + z0
    return go.Surface(x=x, y=y, z=z, colorscale=[[0, color], [1, color]], showscale=False)

def build_scene():
    shapes = []

    # Kepala
    shapes.append(create_sphere(0, 0, 8, 1, 'darkblue'))

    # Badan
    shapes.append(create_cylinder(0, 0, 4, 0.8, 4, 'z', 'black'))

    # Tangan kiri menyerang ke depan
    shapes.append(create_cylinder(-1.2, 0, 5.5, 0.3, 2, 'x', 'darkblue'))
    # Bola api tangan kiri
    shapes.append(create_sphere(-3.5, 0, 5.5, 0.6, 'orange'))

    # Tangan kanan ke samping
    shapes.append(create_cylinder(1.2, 0, 5.5, 0.3, 2, 'x', 'darkblue'))

    # Kaki
    shapes.append(create_cylinder(-0.4, 0, 1, 0.3, 2.5, 'z', 'black'))
    shapes.append(create_cylinder(0.4, 0, 1, 0.3, 2.5, 'z', 'black'))

    # Sayap kiri
    shapes.append(create_cone(-1, -1.5, 6, 0.5, 2, 'gray'))
    # Sayap kanan
    shapes.append(create_cone(1, -1.5, 6, 0.5, 2, 'gray'))

    # Platform (tanah)
    x, y = np.meshgrid(np.linspace(-5, 5, 10), np.linspace(-5, 5, 10))
    z = np.zeros_like(x)
    shapes.append(go.Surface(x=x, y=y, z=z, colorscale=[[0, '#222'], [1, '#222']], showscale=False))

    fig = go.Figure(data=shapes)
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            aspectmode='data'
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        paper_bgcolor='black'
    )
    import plotly.io as pio
    pio.renderers.default = "iframe_connected"

    fig.show()

if __name__ == '__main__':
    build_scene()
