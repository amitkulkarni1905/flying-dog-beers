import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
beers=['High carbon steel', 'Low carbon steel', ' Cast iron']
beers1=['Aluminium alloys', 'Stainless steel', ' Carbon fibre composite']
beers2 = ['Nickle alloy','Copper alloys']
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
mytitle='Elements : High carbon steel,Low carbon steel, Cast iron'
mytitle1 = 'Elements : Aluminium alloys,Stainless steel,Carbon fibre composite'
mytitle2 = 'Elements : Nickle alloy, Copper alloys'
color1='lightblue'
color2='darkgreen'

tabtitle='Mech Project'
myheading='Elements Comparison'
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
    name = 'Tensile strength(Yield)',
    marker = {'color':'deeppink'}
)
o = go.Bar(
    x = beers,
    y = [o_values[0],o_values[1],o_values[2]],
    name = 'Elongation at break in %',
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
    name = 'Machinability in %',
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
j1 = go.Bar(
    x = beers1,
    y = [j_values[3],j_values[4],j_values[5]],
    name = 'Hardness (Rockwell B)',
    marker={'color':'gold'}
)
k1  = go.Bar(
    x = beers1,
    y = [k_values[3],k_values[4],k_values[5]],
    name = 'Hardness(Rockwell C)',
    marker = {'color':'indigo'}
)
l1  = go.Bar(
    x = beers1,
    y = [l_values[3],l_values[4],l_values[5]],
    name = 'Vickers Hardness',
    marker = {'color':'blueviolet'}
)
m1  = go.Bar(
    x = beers1,
    y = [m_values[3],m_values[4],m_values[5]],
    name = 'Tensile Strength(Ultimate)',
    marker = {'color':'dodgerblue'}
)
n1  = go.Bar(
    x = beers1,
    y = [n_values[3],n_values[4],n_values[5]],
    name = 'Tensile strength(Yield)',
    marker = {'color':'deeppink'}
)
o1 = go.Bar(
    x = beers1,
    y = [o_values[3],o_values[4],o_values[5]],
    name = 'Elongation at break in %',
    marker = {'color' : 'maroon'}
)
p1 = go.Bar(
    x = beers1,
    y = [p_values[3],p_values[4],p_values[5]],
    name = 'Modulus of elastisity',
    marker = {'color' : 'teal'}
)
q1 = go.Bar(
    x = beers1,
    y = [q_values[3],q_values[4],q_values[5]],
    name = 'Shear Modulus',
    marker = {'color' : 'dodgerblue'}
)
r1 = go.Bar(
    x = beers1,
    y = [r_values[3],r_values[4],r_values[5]],
    name = 'Bulk Modulus',
    marker = {'color' : 'green'}
)
s1 = go.Bar(
    x = beers1,
    y = [s_values[3],s_values[4],s_values[5]],
    name = 'Poissons Ratio*100',
    marker = {'color' : 'limegreen'}
)
t1 = go.Bar(
    x = beers1,
    y = [t_values[3],t_values[4],t_values[5]],
    name = 'Flexture Yield strength',
    marker = {'color' : 'Chartreuse'}
)
u1 = go.Bar(
    x = beers1,
    y = [u_values[3],u_values[4],u_values[5]],
    name = 'Compressive yield strength',
    marker = {'color' : 'tomato'}
)
v1 = go.Bar(
    x = beers1,
    y = [v_values[3],v_values[4],v_values[5]],
    name = 'Machinability in %',
    marker = {'color' : 'lightcoral'}
)

w1 = go.Bar(
    x = beers1,
    y = [w_values[3],w_values[4],w_values[5]],
    name = 'Izod Impact*10',
    marker = {'color' : 'darkorange'}
)
z1 = go.Bar(
    x = beers1,
    y = [z_values[3],z_values[4],z_values[5]],
    name = 'Charpy Impact',
    marker = {'color' : 'sienna'}
) 


beer_data1 = [bitterness1, alcohol1,i1,j1,k1,l1,m1,n1,o1,p1,q1,r1,s1,t1,u1,v1,w1,z1]
beer_layout1 = go.Layout(
    barmode='group',
    title = mytitle1
)

beer_fig1 = go.Figure(data=beer_data1, layout=beer_layout1)
###########################################################################################
bitterness2 = go.Bar(
    x=beers2,
    y=[ibu_values[6],ibu_values[7]],
    name='Density*10',
    marker={'color':color1}
)
alcohol2 = go.Bar(
    x=beers2,
    y=[abv_values[6],abv_values[7]],
    name='Particle Size',
    marker={'color':color2}
)
i2 = go.Bar(
    x = beers2,
    y=[i_values[6],i_values[7]],
    name = 'Hardness (Brinell)',
    marker={'color':'red'}
)
j2 = go.Bar(
    x = beers2,
    y = [j_values[6],j_values[7]],
    name = 'Hardness (Rockwell B)',
    marker={'color':'gold'}
)
k2  = go.Bar(
    x = beers2,
    y = [k_values[6],k_values[7]],
    name = 'Hardness(Rockwell C)',
    marker = {'color':'indigo'}
)
l2  = go.Bar(
    x = beers2,
    y = [l_values[6],l_values[7]],
    name = 'Vickers Hardness',
    marker = {'color':'blueviolet'}
)
m2  = go.Bar(
    x = beers2,
    y = [m_values[6],m_values[7]],
    name = 'Tensile Strength(Ultimate)',
    marker = {'color':'dodgerblue'}
)
n2  = go.Bar(
    x = beers2,
    y = [n_values[6],n_values[7]],
    name = 'Tensile strength(Yield)',
    marker = {'color':'deeppink'}
)
o2 = go.Bar(
    x = beers2,
    y = [o_values[6],o_values[7]],
    name = 'Elongation at break in %',
    marker = {'color' : 'maroon'}
)
p2 = go.Bar(
    x = beers2,
    y = [p_values[6],p_values[7]],
    name = 'Modulus of elastisity',
    marker = {'color' : 'teal'}
)
q2 = go.Bar(
    x = beers2,
    y = [q_values[6],q_values[7]],
    name = 'Shear Modulus',
    marker = {'color' : 'dodgerblue'}
)
r2 = go.Bar(
    x = beers2,
    y = [r_values[6],r_values[7]],
    name = 'Bulk Modulus',
    marker = {'color' : 'green'}
)
s2 = go.Bar(
    x = beers2,
    y = [s_values[6],s_values[7]],
    name = 'Poissons Ratio*100',
    marker = {'color' : 'limegreen'}
)
t2 = go.Bar(
    x = beers2,
    y = [t_values[6],t_values[7]],
    name = 'Flexture Yield strength',
    marker = {'color' : 'Chartreuse'}
)
u2 = go.Bar(
    x = beers2,
    y = [u_values[6],u_values[7]],
    name = 'Compressive yield strength',
    marker = {'color' : 'tomato'}
)
v2 = go.Bar(
    x = beers2,
    y = [v_values[6],v_values[7]],
    name = 'Machinability in %',
    marker = {'color' : 'lightcoral'}
)

w2 = go.Bar(
    x = beers2,
    y = [w_values[6],w_values[7]],
    name = 'Izod Impact*10',
    marker = {'color' : 'darkorange'}
)
z2 = go.Bar(
    x = beers2,
    y = [z_values[6],z_values[7]],
    name = 'Charpy Impact',
    marker = {'color' : 'sienna'}
)

beer_data2 = [bitterness2, alcohol2,i2,j2,k2,l2,m2,n2,o2,p2,q2,r2,s2,t2,u2,v2,w2,z2]
beer_layout2 = go.Layout(
    barmode='group',
    title = mytitle2
)

beer_fig2 = go.Figure(data=beer_data2, layout=beer_layout2)


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
    ),
    dcc.Graph(
        id = 'f3',
        figure = beer_fig2
    )
    
    ]
)

if __name__ == '__main__':
    app.run_server()
