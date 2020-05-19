import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ibu_values=[35, 0, 85, 75]
abv_values=[5.4, 7.1, 0, 4.3]
i_values = [122,43,0,78,134]
j_values = [10,0,30,40,50]
k_values = [0,123,456,97,23]
l_values = [260,247,217,97.1,251,63.3,282,146]
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
beer_data = [bitterness, alcohol,i,j,k]
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
