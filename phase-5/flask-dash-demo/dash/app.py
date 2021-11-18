import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pickle
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px



# load in pretrained objects

# TSNE Model
with open('tsne3.pkl', 'rb') as f:
    tsne3 = pickle.load(f)

# TSNE Data
tsne3D = pd.read_csv('tsne3D.csv')
ids = [{'label': appid, 'value': appid} for appid in tsne3D.appid.tolist()]


# HTML ELEMENTS

grid_pad = {'padding-bottom': '730px', 'text-align': 'center'}


header = html.Div(className="jumbotron-fluid text-center",
style = {'padding-bottom': '20px'},
children=[
    html.H1(children='This is My Dashboard'),
    ])

dropdown = html.Div(style = {'padding-bottom': '20px'},children=[
    dcc.Dropdown(id='id-selector',
    options = ids,
    multi=True,
    placeholder="Choose ID"
    )
])

text_input = html.Div(style = {'padding-bottom': '20px'},children=[
    dcc.Input(id='raw-text',
    placeholder='Enter sample search terms',
    value='Sample searches',
    style={'width': '100%'}
)
])



subhead = dbc.Row([
    dbc.Col(dropdown),
    dbc.Col(text_input),

])

grid = dbc.Row([
    dbc.Col(dcc.Graph(style={'opacity': '0.75'},id='graph')),
    dbc.Col(html.Div(id='user-details')),

])



####################### main site ###########################

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.title = 'Dashboard'

app.layout = html.Div(id='body', children = [
    header, subhead, grid
])


####################### callbacks ###########################

@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='id-selector', component_property='value')]
)
def make_figure(input_value):

    return px.scatter_3d(
        tsne3D,
        x='x',
        y='y',
        z='z',
        color='cluster',
        hover_data=['searches','cluster'],
        height=700,
    )

@app.callback(
    Output(component_id='user-details', component_property='children'),
    [Input(component_id='raw-text', component_property='value')]
)
def output_div(input_value):

    return html.H3("Sample search: "+input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
