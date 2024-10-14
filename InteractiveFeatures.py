import plotly.graph_objects as pg
import plotly.express as px


# Dropdown Menu
df = px.data.tips()
plot = pg.Figure(data=[pg.Scatter(x=df['day'], y=df['tip'], mode='markers')])
plot.update_layout(updatemenus=[dict(buttons=list([dict(args=['type', 'scatter'], label='scatter plot', method='restyle'),
                                                   dict(args=['type', 'bar'], label='bar chart', method='restyle')]),
                                     direction='down')])
plot.show()


# Add Buttons
df = px.data.tips()
plot = pg.Figure(data=[pg.Scatter(x=df['day'], y=df['tip'], mode='markers')])
plot.update_layout(updatemenus=[dict(buttons=list([dict(args=['type', 'scatter'], label='scatter plot', method='restyle'),
                                                   dict(args=['type', 'bar'], label='bar chart', method='restyle')]),
                                     direction='left', type='buttons')])
plot.show()


# Sliders and Selectors
data = px.data.tips()
plot = pg.Figure(data=[pg.Scatter(x=data['total_bill'], y=['tip'], mode='markers')])
plot.update_layout(xaxis=dict(rangeselector=dict(buttons=list([dict(count=1, step='day', stepmode='backward')])),
                              rangeslider=dict(visible=True)))
plot.show()
