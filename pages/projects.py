import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from .side_bar import sidebar
from dataManipulation.GraphSketch import Sketch

dash.register_page(__name__, title='App1', order=1)

def update_graph_card():
    ChoroplethGraph = Sketch('ChoroplethData.json')
    ChoroplethGraph = ChoroplethGraph.ChoroplethGraph(locations='cc', hover_name='countryName', color='unique')
    return ChoroplethGraph


def layout():
    return html.Div([
        dbc.Row(
            [
                dbc.Col(
                    [
                        sidebar()
                    ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

                dbc.Col(
                    [
                        html.H3('Swetrix visities', style={'textAlign': 'center'}),
                        html.Hr(),
                        dcc.Graph(id='choropleth', figure=update_graph_card()),

                    ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
            ]
        )
    ])

