import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
beers=['High carbon steel', 'Low carbon steel', ' Cast iron']
ibu_values=[75,76,72,254,78,14,842,864]
abv_values=[9.27,0,0,51	18.1,0,9,18.3]
i_values = [260,247,217,97.1,251,63.3,282,146]
j_values = [75.7,89.4,0,69.3,54,88.3,88.2,69.2]
k_values = [46.4,31.7,17.9,45.2,86.4,0,38,34.7]
l_values = [286,266,235,116,294,1030,296,231]
m_values = [1120,716,310,344,941,1230,902,512]
n_values = [896,519,124]
o_values = [14.30,20.20,6.67]
p_values = [200,202,118]
q_values = [79.9,79.7,47.6]
r_values = [160,160,0]
s_values = [29.2,29,29.4]
t_values = [2260,0,575]
u_values = [2160,0,943]
v_values = [53.05,61.30,48.80]
w_values = [89,965,297]
z_values = [34.1,54.9,0]

color1='lightblue'
color2='darkgreen'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='Flying Dog Beers'
label1='IBU'
label2='ABV'


########### Set up the chart
bitterness = go.Bar(
    x=beers,
    y=[ibu_values[0],ibu_values[1],ibu_values[2]],
    name='Density*10',
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=[abv_values[0],abv_values[1],abv_values[2]],
    name='Particle Size',
    marker={'color':color2}
)
i = go.Bar(
    x = beers,
    y=[i_values[0],i_values[1],i_values[2]],
    name = 'Hardness (Brinell)',
    marker={'color':'red'}
)
j = go.Bar(
    x = beers,
    y = [j_values[0],j_values[1],j_values[2]],
    name = 'Hardness (Rockwell B)',
    marker={'color':'gold'}
)
k  = go.Bar(
    x = beers,
    y = [k_values[0],k_values[1],k_values[2]],
    name = 'Hardness(Rockwell C)',
    marker = {'color':'indigo'}
)
l  = go.Bar(
    x = beers,
    y = [l_values[0],l_values[1],l_values[2]],
    name = 'Vickers Hardness',
    marker = {'color':'blueviolet'}
)
m  = go.Bar(
    x = beers,
    y = [m_values[0],m_values[1],m_values[2]],
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
q = go.Bar(
    x = beers,
    y = q_values,
    name = 'Shear Modulus',
    marker = {'color' : 'dodgerblue'}
)
r = go.Bar(
    x = beers,
    y = r_values,
    name = 'Bulk Modulus',
    marker = {'color' : 'green'}
)
s = go.Bar(
    x = beers,
    y = s_values,
    name = 'Poissons Ratio*100',
    marker = {'color' : 'limegreen'}
)
t = go.Bar(
    x = beers,
    y = t_values,
    name = 'Flexture Yield strength',
    marker = {'color' : 'Chartreuse'}
)
u = go.Bar(
    x = beers,
    y = u_values,
    name = 'Compressive yield strength',
    marker = {'color' : 'tomato'}
)
v = go.Bar(
    x = beers,
    y = v_values,
    name = 'Machinability',
    marker = {'color' : 'lightcoral'}
)

w = go.Bar(
    x = beers,
    y = w_values,
    name = 'Izod Impact*10',
    marker = {'color' : 'darkorange'}
)
z = go.Bar(
    x = beers,
    y = z_values,
    name = 'Charpy Impact',
    marker = {'color' : 'sienna'}
) 


beer_data = [bitterness, alcohol,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,z]
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
    )
    
    ]
)

if __name__ == '__main__':
    app.run_server()
