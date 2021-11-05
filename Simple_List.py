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
#description_list = []  #probabbly can do this in a better way with pandas
#, debounce=True
# dcc.Textarea(id="current_item_details", placeholder="Details or notes",
#                  style={'width': 250, 'height': 15, 'padding':10}),
# State('current_item_details','value'),


app = dash.Dash(__name__)
app.layout = html.Div(children = [
    html.H1('Add items to a list'),
    html.Div(id='input_fields_container', children=[
        dcc.Input(id="current_item", placeholder="Thing to do"),        
    html.Button('Add...', id='add_button', n_clicks=0),
        ]),    
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
    ''' when the add_button is clicked, return the value from current_item'''
    if n_clicks is None:
        raise PreventUpdate
    temporary_item = html.P(current_item_value)
    activity_list.append(temporary_item)
    #temp_desc = html.P(cur_item_desc)
    #description_list.append(temp_desc)
    print(activity_list)
    
    return activity_list

@app.callback(
    Output('saved_message_div','children'),
    [Input('save_to_csv_button','n_clicks'),
     Input('items_output_container','children')]
    )
def save_to_csv(n_clicks, children):
    # this is still firing before click need prevent initial update
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