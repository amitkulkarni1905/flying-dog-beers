import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
elements=['High carbon steel', 'Low carbon steel', 'Cast iron', 'Aluminium alloys', 'Stainless steel','Carbon fibre composite','Nickle alloy','Copper alloys']
density=[7.5,7.6,7.2,2.54,7.8,1.4,8.42,8.64]
p_size=[9.27, 0,0,51,18.1,0,39,18.3]
h_brinell = [260,247,217,97.1,251,63.3,282,146]
h_rockb = [75.7,	89.4,	0,	69.3,	54,	88.3,	88.2,	69.2]
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
g_d = [p_size1]
g_layout2 = go.Layout(
    barmode='group',
    title = 'Particle Size'
)

g_fig2 = go.Figure(data=g_d, layout=g_layout2)

"""....................................................................................."""

h_brinell = go.Bar(
    x=elements,
    y=h_brinell,
    name=label3,
    marker={'color':'darkblue'}
)
g_d3 = [h_brinell]
g_layout3 = go.Layout(
    barmode='group',
    title = 'Hardness(Brinell)'
)

g_fig3 = go.Figure(data=g_d3, layout=g_layout3)

"""....................................................................................."""
"""h_rockb = go.Bar(
    x=elements,
    y=h_rockb,
    name=label4,
    marker={'color':'lightblue'}
)
g_d4 = [h_rockb]
g_layout4 = go.Layout(
    barmode='group',
    title = 'Hardness (Rockwell B)'
)

g_fig4 = go.Figure(data=g_d4, layout=g_layout4)"""



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
        id='f3',
        figure=g_fig3
    ),
   """ dcc.Graph(
        id='f4',
        figure=g_fig4
    ),"""
    
   
    ]
)

if __name__ == '__main__':
    app.run_server()
