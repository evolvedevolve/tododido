# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 17:51:41 2021
Prototype for building a todo list

Usage: User informally adds tasks and activities or notes for the day
    this is output to a csv after it is complete
    then the plan todo page is called and anything that matches is autofill?

@author: Patty Whack
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
#import plotly

# todo  need to use store='memory' as an output so the page doesnt clear

activity_list = []
#, debounce=True
app = dash.Dash(__name__)
app.layout = html.Div(children = [
    html.H1('Add items to a list'),
    dcc.Input(id="current_item", placeholder="Thing to do"),
    html.Button('Add...', id='add_button', n_clicks=0),
    html.Div(id="current_item_output_container", children = [])
    ])

@app.callback(
    Output('current_item_output_container', 'children'),
    [Input('add_button','n_clicks')],
     State('current_item','value')
    )
def add_to_list(n_clicks, current_item_value):
    if n_clicks is None:
        raise PreventUpdate    
    temporary_item = html.P(current_item_value)
    activity_list.append(temporary_item)
    
    return activity_list

app.run_server(debug=True)