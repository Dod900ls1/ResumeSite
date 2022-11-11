import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)


layout = html.Div([
    dcc.Markdown('# Yehor Boiar', style={'textAlign': 'center'}),
    dcc.Markdown('Scotland, Dundee', style={'textAlign': 'center'}),

    dcc.Markdown('### Professional Summary', style={'textAlign': 'center'}),
    html.Hr(),
    dcc.Markdown(
        'Novice data analyst. I love learning new things. Analytical mindset. I easily endure stressful situations.\n',
        style={'textAlign': 'center', 'white-space': 'pre'}),

    dcc.Markdown('### Skills', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('* Python. Familiar with libraries such as: pandas, numpy, dash.\n'
                         '* I have knowledge of mathematics at the level of the second year of the university\n'
                         '(integrals, series, differential equations)\n')
        ], width={"size": 3, "offset": 1}),
    ], justify='center'),

    dcc.Markdown('### Work History', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('01/09/2022 to current', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('* Junior python developer \n'
                         'Swetrix ',
                         style={'white-space': 'pre'},
                         className='ms-3')
        ], width=5)
    ], justify='center'),

    dcc.Markdown('### Education', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2013',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Computer Science and Technology: Systems Analysis\n'
                         'Zaporizhzhia Polytechnic National University - Ukraine, Zaporizhzhia',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
])
