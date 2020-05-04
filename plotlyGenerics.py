

def hist_2d(x, y):

    import plotly.graph_objects as go
    import numpy as np

    fig = go.Figure(go.Histogram2d(x=x, y=y, histnorm='probability',
            autobinx=False,
            xbins=dict(start=-3, end=3, size=0.1),
            autobiny=False,
            ybins=dict(start=-2.5, end=4, size=0.1),
            colorscale=[[0, 'rgb(12,51,131)'], [0.25, 'rgb(10,136,186)'], [0.5, 'rgb(242,211,56)'], [0.75, 'rgb(242,143,56)'], [1, 'rgb(217,30,30)']]
        ))
    fig.show()


def contour_hist_2d(x, y):

    import plotly.graph_objects as go
    import numpy as np

    fig = go.Figure(go.Histogram2dContour(
            x = x,
            y = y
    ))
    fig.show()


def bubble_3d(x, y, z, text, size, color, title):
    import plotly.graph_objects as go
    import pandas as pd

    fig = go.Figure(data=go.Scatter3d(
        x=x,
        y=y,
        z=z,
        text=text,
        mode='markers',
        marker=dict(
            sizemode='diameter',
            sizeref=750,
            size=size,
            color = color,
            colorscale = 'Viridis',
            colorbar_title = 'Life<br>Expectancy',
            line_color='rgb(140, 140, 170)'
        )
    ))

    fig.update_layout(height=800, width=800,
                    title=title)
    fig.show()



def isosurface_3d(x, y, z):
    import plotly.graph_objects as go

    fig= go.Figure(data=go.Isosurface(
        x=x,
        y=y,
        z=z,
        value=[1,2,3,4,5,6,7,8],
        isomin=2,
        isomax=6,
    ))

    fig.show()



    