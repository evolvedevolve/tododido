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
import pandas as pd
#import plotly

# todo  need to use store='session' as an output so the page doesnt clear
# dcc.Store(id='session', storage_type='session'),
# local might also work

activity_list = []
#, debounce=True
app = dash.Dash(__name__)
app.layout = html.Div(children = [
    html.H1('Add items to a list'),
    dcc.Input(id="current_item", placeholder="Thing to do"),
    html.Button('Add...', id='add_button', n_clicks=0),
    html.Div(id="items_output_container", children = []),
    html.Button('Save to CSV', id='save_to_csv_button', n_clicks=0),
    html.Div(id='saved_message_div', children=[]),
    dcc.Store(id='session_store', storage_type='local')
    ])

@app.callback(
    Output('items_output_container', 'children'),
    [Input('add_button','n_clicks')],
     [State('current_item','value'),
     State('session_store','data')]
    )
def add_to_list(n_clicks, current_item_value, session_store):
    if n_clicks is None:
        raise PreventUpdate
    temporary_item = html.P(current_item_value)
    activity_list.append(temporary_item)    
    
    return activity_list

@app.callback(
    Output('saved_message_div','children'),
    [Input('save_to_csv_button','n_clicks'),
     Input('items_output_container','children')]
    )
def save_to_csv(n_clicks, children):
    if n_clicks is None:
        raise PreventUpdate
    # p is still getting created
    save_df = pd.DataFrame(children)
    # so this is creating a full on frame with 
    # ,props,type,namespace    looks like first is an index
    # instead need to use dict.get('props') for value or something

    save_df.to_csv('simple.csv')
    # need to make this only displayed if it exists
    output = html.Plaintext("The Simple List has been created and saved.")
    return output

app.run_server(debug=True)