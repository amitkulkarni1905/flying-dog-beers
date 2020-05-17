import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
beers=['High carbon steel', 'Low carbon steel', 'Cast iron', 'Aluminium alloys', 'Stainless steel','carbon fibre composite','Nickle alloy','Copper alloys']
ibu_values=[7.5,7.6,7.2,2.54,7.8,1.4,8.42,8.64]
abv_values=[9.27, 0,0,51,18.1,0,39,18.3]
tabtitle='Mech Project'
myheading='Mech Project'
label1='IBU'
label2='ABV'

########### Set up the chart
bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name=label1,
    marker={'color':'red'}
)
beer_data = [bitterness]
beer_layout = go.Layout(
    barmode='group',
    title = 'Density'
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name=label2,
    marker={'color':'darkgreen'}
)

beer_d = [alcohol]
beer_layout2 = go.Layout(
    barmode='group',
    title = 'Particle Size'
)

beer_fig2 = go.Figure(data=beer_d, layout=beer_layout2)



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
    dcc.Graph(
        id='flying',
        figure=beer_fig2
    ),
   
    ]
)

if __name__ == '__main__':
    app.run_server()
