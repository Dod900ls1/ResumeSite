import dash
from dash import dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3)

green_text = {'color': 'green'}


def layout():
    return dbc.Row([
        dbc.Col([
            dcc.Markdown('### Personal info', style={'color': 'gray'}),
            dcc.Markdown('Address', style=green_text),
            dcc.Markdown('Scotland, Dundee'),
            dcc.Markdown('Phone Number', style=green_text),
            dcc.Markdown('+44 7393284577'),
            dcc.Markdown('Email', style=green_text),
            dcc.Markdown('boyaregor1@gmail.com'),
            dcc.Markdown('Linkedin', style=green_text),
            dcc.Markdown('[https://www.linkedin.com/in/%D0%B5%D0%B3%D0%BE%D1%80-%D0%B1%D0%BE%D1%8F%D1%80-634266241/]',
                         link_target='_blank'),
            dcc.Markdown('GitHub', style=green_text),
            dcc.Markdown('[https://github.com/Dod900ls1]', link_target='_blank'),
        ], width={'size': 6, 'offset': 2})
    ], justify='center')
