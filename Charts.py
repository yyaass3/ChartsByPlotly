import plotly.express as px

# line chart
df = px.data.iris()
fig = px.line(df, y='sepal_width', line_dash='species', color='species')
fig.show()

# bar chart
df2 = px.data.tips()
fig2 = px.bar(df2, x='day', y='total_bill', color='sex', facet_col='sex', facet_row='time')
fig2.show()

# scatter plot
df3 = px.data.tips()
fig3 = px.scatter(df3, x='total_bill', y='tip', color='time', symbol='sex', size='size',facet_row='day', facet_col='time')
fig3.show()

# histogram
df4 = px.data.tips()
fig4 = px.histogram(df4, x='total_bill', color='sex', nbins=50, histnorm='percent', barmode='overlay')
fig4.show()

# pie chart
df5 = px.data.tips()
fig5 = px.pie(df5, values='total_bill', names='day', color_discrete_sequence=px.colors.sequential.RdBu, opacity=0.7, hole=0.5)
fig5.show()

# box plot
df6 = px.data.tips()
fig6 = px.box(df6, x='day', y='tip', color='sex', facet_row='time', boxmode='group', notched=True)
fig6.show()

# violin plot
df7 = px.data.tips()
fig7 = px.violin(df7, x='day', y='tip', color='sex', facet_row='time', box=True)
fig7.show()

# 3D Scatter Plot
df8 = px.data.tips()
fig8 = px.scatter_3d(df8, x='total_bill', y='sex', z='tip', color='day', size='total_bill', symbol='time')
fig8.show()
