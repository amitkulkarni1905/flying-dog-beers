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
h_rockc = [46.4,	31.7,	17.9,	45.2,	86.4,	0,	38,	34.7]
v_hard = [286,	266,	235,	116,	294,	1030,	296,	231]
t_ultima = [1120,	716,	310,	344,	941,	1230,	902,	512]
t_yield = [896,	519,	124,	278,	669,	1.55,	585,	384]
e_break = [14.30,	20.20,	6.67,	9.94,	26.50,	94.60,	33.80,	22.60]
mod_e = [200,	202,	118,	77.4,	196,	0,	207,   119]
s_mod = [79.9,	79.7,	47.6,	19.9,	77.6,	3.11,	77.5,	44.9]
b_mod = [160,	160,	0,	0,	166,	0,	0,	140]
p_ratio = [0.292,	0.29,	0.294,	0.327,	0.289,	0.293,	0.316,	0.317]
fy_strength = [2260,	0,	575,	260,	0,	999,	689,	525]
cy_strength = [2160,	0,	943,	95.7,	0,	725,	0,	529]
m = [53.05,	61.30,	48.80,	55.90,	31.70,	0,	0,	32.60]
i_impact = [8.9,	96.5,	29.7,	0,	115,	10.4,	131,	33.7]
c_impact = [34.1,	54.9,	0,	7.91,	115,	0,	151,	47.8]
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
    y=p_size,
    name=label2,
    marker={'color':'blue'}
)
g_d3 = [p_size1]
g_layout3 = go.Layout(
    barmode='group',
    title = 'Hardness(Brinell)'
)

g_fig3 = go.Figure(data=g_d3, layout=g_layout3)



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
        id='f2',
        figure=g_fig3
    ),
    
   
    ]
)

if __name__ == '__main__':
    app.run_server()
