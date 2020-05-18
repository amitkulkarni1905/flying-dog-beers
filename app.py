import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
elements=['High carbon steel', 'Low carbon steel', 'Cast iron', 'Aluminium alloys', 'Stainless steel','Carbon fibre composite','Nickle alloy','Copper alloys']
density=[7.5,7.6,7.2,2.54,7.8,1.4,8.42,8.64]
p_size=[9.27, 0,0,51,18.1,0,39,18.3]
h_brinell = [260,247,217,97.1,251,63.3,282,146]

tabtitle='Mech Project'
myheading='Mech Project'
label1='Density'
label2='Particle Size'

########### Set up the chart
density1 = go.Bar(
    x=elements,
    y=density,
    name=label1,
    marker={'color':'red'}
)
g_data = [density1]
g_layout = go.Layout(
    barmode='group',
    title = 'Density'
)

g_fig = go.Figure(data=g_data, layout=g_layout)

"""....................................................................................."""

p_size1 = go.Bar(
    x=elements,
    y=p_size,
    name=label2,
    marker={'color':'darkgreen'}
)
g_d2 = [p_size1]
g_layout2 = go.Layout(
    barmode='group',
    title = 'Particle Size'
)

g_fig2 = go.Figure(data=g_d2, layout=g_layout2)

"""....................................................................................."""
h_brinell = go.Bar(
       x = elements,
       y = h_brinell,
       marker = {'color' : 'cyan'}
)
g_d3 = [h_brinell]
g_layout3 = go.Layout(
    barmode = 'group',
    title = 'h_brinell'
)

g_fig3 = go.Figure(data=g_d3,layout=g_layout3)



########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='f1',
        figure=g_fig
    ),
    dcc.Graph(
        id='f2',
        figure=g_fig2
    ),
    dcc.Graph(
        id = 'f3',
        figure = g_fig3
    )

   
    ]
)

if __name__ == '__main__':
    app.run_server()
