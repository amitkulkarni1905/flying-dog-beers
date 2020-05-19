import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
beers=['High carbon steel', 'Low carbon steel', ' Cast iron']
ibu_values=[7.5,7.6,7.2]
abv_values=[9.27,0,0]
i_values = [260,247,217]
j_values = [75.7,89.4,0]
k_values = [46.4,31.7,17.9]
l_values = [286,266,235]
m_values = [1120,716,310]
n_values = [896,519,124]
o_values = [14.30,20.20,6.67]
p_values = [200,202,118]

color1='lightblue'
color2='darkgreen'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='Flying Dog Beers'
label1='IBU'
label2='ABV'
label3 = 'I'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'

########### Set up the chart
bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name='Density',
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name='Particle Size',
    marker={'color':color2}
)
i = go.Bar(
    x = beers,
    y=i_values,
    name = 'Hardness (Brinell)',
    marker={'color':'red'}
)
j = go.Bar(
    x = beers,
    y = j_values,
    name = 'Hardness (Rockwell B)',
    marker={'color':'gold'}
)
k  = go.Bar(
    x = beers,
    y = k_values,
    name = 'Hardness(Rockwell C)',
    marker = {'color':'indigo'}
)
l  = go.Bar(
    x = beers,
    y = l_values,
    name = 'Vickers Hardness',
    marker = {'color':'blueviolet'}
)
m  = go.Bar(
    x = beers,
    y = m_values,
    name = 'Tensile Strength(Ultimate)',
    marker = {'color':'dodgerblue'}
)
n  = go.Bar(
    x = beers,
    y = n_values,
    name = 'Tensile strength(Yield)%',
    marker = {'color':'deeppink'}
)
o = go.Bar(
    x = beers,
    y = o_values,
    name = 'Elongation at break',
    marker = {'color' : 'maroon'}
)
p = go.Bar(
    x = beers,
    y = p_values,
    name = 'Modulus of elastisity',
    marker = {'color' : 'teal'}
)
beer_data = [bitterness, alcohol,i,j,k,l,m,n,o,p]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

"""beer_data1 = [j,k,l]
beer_layout1 = go.Layout(
    barmode = 'group',
    title = mytitle
)

beer_fig1 = go.Figure(data = beer_data1, layout=beer_layout1)"""

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    
    ]
)

if __name__ == '__main__':
    app.run_server()
