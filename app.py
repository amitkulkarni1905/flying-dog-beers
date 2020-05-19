import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
beers=['High carbon steel', 'Low carbon steel', ' Cast iron']
beers1=['Aluminium alloys', 'Stainless steel', ' Carbon fibre composite']
ibu_values=[75,76,72,254,78,14,842,864]
abv_values=[9.27,0,0,51,18.1,0,9,18.3]
i_values = [260,247,217,97.1,251,63.3,282,146]
j_values = [75.7,89.4,0,69.3,54,88.3,88.2,69.2]
k_values = [46.4,31.7,17.9,45.2,86.4,0,38,34.7]
l_values = [286,266,235,116,294,1030,296,231]
m_values = [1120,716,310,344,941,1230,902,512]
n_values = [896,519,124,278,669,1.55,585,384]
o_values = [14.30,20.20,6.67,9.94,26.50,94.60,33.80,22.60]
p_values = [200,202,118,77.4,196,0,207,119]
q_values = [79.9,79.7,47.6,19.9,77.6,3.11,77.5,44.9]
r_values = [160,160,0,0,166,0,0,140]
s_values = [29.2,29,29.4,32.7,28.9,29.3,31.6,31.7]
t_values = [2260,0,575,260,0,999,689,525]
u_values = [2160,0,943,95.7,0,725,0,529]
v_values = [53.05,61.30,48.80,55.90,31.70,0.00,0.00,32.60]
w_values = [89,965,297,0,115,10.4,131,33.7]
z_values = [34.1,54.9,0,7.91,115,0,151,47.8]

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
    y = [n_values[0],n_values[1],n_values[2]],
    name = 'Tensile strength(Yield)%',
    marker = {'color':'deeppink'}
)
o = go.Bar(
    x = beers,
    y = [o_values[0],o_values[1],o_values[2]],
    name = 'Elongation at break',
    marker = {'color' : 'maroon'}
)
p = go.Bar(
    x = beers,
    y = [p_values[0],p_values[1],p_values[2]],
    name = 'Modulus of elastisity',
    marker = {'color' : 'teal'}
)
q = go.Bar(
    x = beers,
    y = [q_values[0],q_values[1],q_values[2]],
    name = 'Shear Modulus',
    marker = {'color' : 'dodgerblue'}
)
r = go.Bar(
    x = beers,
    y = [r_values[0],r_values[1],r_values[2]],
    name = 'Bulk Modulus',
    marker = {'color' : 'green'}
)
s = go.Bar(
    x = beers,
    y = [s_values[0],s_values[1],s_values[2]],
    name = 'Poissons Ratio*100',
    marker = {'color' : 'limegreen'}
)
t = go.Bar(
    x = beers,
    y = [t_values[0],t_values[1],t_values[2]],
    name = 'Flexture Yield strength',
    marker = {'color' : 'Chartreuse'}
)
u = go.Bar(
    x = beers,
    y = [u_values[0],u_values[1],u_values[2]],
    name = 'Compressive yield strength',
    marker = {'color' : 'tomato'}
)
v = go.Bar(
    x = beers,
    y = [v_values[0],v_values[1],v_values[2]],
    name = 'Machinability',
    marker = {'color' : 'lightcoral'}
)

w = go.Bar(
    x = beers,
    y = [w_values[0],w_values[1],w_values[2]],
    name = 'Izod Impact*10',
    marker = {'color' : 'darkorange'}
)
z = go.Bar(
    x = beers,
    y = [z_values[0],z_values[1],z_values[2]],
    name = 'Charpy Impact',
    marker = {'color' : 'sienna'}
) 


beer_data = [bitterness, alcohol,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,z]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)
#######################################################################
bitterness1 = go.Bar(
    x=beers1,
    y=[ibu_values[3],ibu_values[4],ibu_values[5]],
    name='Density*10',
    marker={'color':color1}
)
alcohol1 = go.Bar(
    x=beers1,
    y=[abv_values[3],abv_values[4],abv_values[5]],
    name='Particle Size',
    marker={'color':color2}
)
i1 = go.Bar(
    x = beers1,
    y=[i_values[3],i_values[4],i_values[5]],
    name = 'Hardness (Brinell)',
    marker={'color':'red'}
)

beer_data1 = [bitterness1, alcohol1,i1]
beer_layout1 = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig1 = go.Figure(data=beer_data1, layout=beer_layout1)


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
        id = 'f2',
        figure=beer_fig1
    )
    
    ]
)

if __name__ == '__main__':
    app.run_server()
