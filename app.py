import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
beers=['High carbon steel', 'Low carbon steel', ' Cast iron', 'Aluminium alloys']
ibu_values=[7.5,7.6,7.2,2.54]
abv_values=[9.27,0,0,51]
i_values = [260,247,217,97.1]
j_values = [75.7,89.4,0,69.3]
k_values = [46.4,31.7,17.9,45.2]
l_values = [286,266,235,116]
m_values = [1120,716,310,344]
n_values = [896,519,124,278]
o_values = [14.30,20.20,6.67,9.94]
p_values = [200,202,118,77.4]

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
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name=label2,
    marker={'color':color2}
)
i = go.Bar(
    x = beers,
    y=i_values,
    name = 'I',
    marker={'color':'red'}
)
j = go.Bar(
    x = beers,
    y = j_values,
    name = 'J',
    marker={'color':'gold'}
)
k  = go.Bar(
    x = beers,
    y = k_values,
    name = 'K',
    marker = {'color':'indigo'}
)
l  = go.Bar(
    x = beers,
    y = l_values,
    name = 'L',
    marker = {'color':'blueviolet'}
)
m  = go.Bar(
    x = beers,
    y = m_values,
    name = 'M',
    marker = {'color':'dodgerblue'}
)
n  = go.Bar(
    x = beers,
    y = n_values,
    name = 'N',
    marker = {'color':'deeppink'}
)
o = go.Bar(
    x = beers,
    y = o_values,
    name = 'O',
    marker = {'color' : 'maroon'}
)
p = go.Bar(
    x = beers,
    y = p_values,
    name = 'P',
    marker = {'color' : 'teal'}
)
beer_data = [bitterness, alcohol,i,j,k,l,m,n,o,p]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)


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
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
