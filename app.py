import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import collections

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='''
        Interactive Chart:
    '''),
    dcc.Dropdown(
        id = "input",
        options=[
            {'label': 'January', 'value': 1},
            {'label': 'Febuary', 'value': 2},
            {'label': 'March', 'value': 3}
        ], value = 1
    ),
    dcc.Graph( id="output-graph")
])

@app.callback(
    Output(component_id='output-graph', component_property='figure'),
    [Input(component_id='input', component_property='value')])
def update_value(value):

    start = datetime.datetime(2018, value, 1, 0, 0, 0, 1)
    end = datetime.datetime(2018,  value + 1, 1, 0, 0, 0, 1)
    subset_df = df[ (df["lost_time"] > start) & (df["lost_time"] < end) ]
    x = pd.value_counts(subset_df.deal_source).index
    y = pd.value_counts(subset_df.deal_source).values

    return({'data': [
                {'x': x, 'y': y, 'type': 'bar', 'name': value},
            ],
            'layout': {
                'title': "Deal Flow source for {} 2018".format(months[value-1])
            }
        }
    )

if __name__ == "__main__":
    app.run_server(debug = True)
