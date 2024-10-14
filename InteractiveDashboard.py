from dash import dcc, html
import plotly.express as px
import pandas as pd
from jupyter_dash import JupyterDash

data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 15, 13, 17, 14]})
app = JupyterDash(__name__)
app.layout = html.Div([dcc.Graph(id='example_graph', figure=px.scatter(data, x='x', y='y', title='Scatter Plot in Dash'))])
app.run_server(mode='inline')
