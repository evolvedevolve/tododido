# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 08:33:07 2021

@author: Patty Whack
"""
import dash
import dash_table as dt
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate as pu
import plotly_express as px
import pandas as pd
import csv
from datetime import datetime

# collect todo
# to do need to add a sum at the end to total how much you will plan to do
# after this table is built, the user saves it
# then is loaded up by the doing portion of the app

# a list of activities to select from - to do make this its own spreadsheet which can be overwritten to! add new activity
sample_activities = ["Learn Python", "Make Food", "Recap", "Plan", "Errands",
                     "Groceries", "Make Food", "Eat", "Walk", "Game", "Cat Care", "Portfolio"]

family_activities = ["Baby Planning", "Baby Reading"]

# should do activities 
shoulddo_activities = ["Maintain Home", "Plan Future", "Organization",
                       "Financials", "Taxes", "Home Improvement"]

# health activities
healthy_activities = ["Meditate", "Work Out", 
                      "Journal", "Walk", "Physio",
                      "Phone PPL", "Clean House"
                      ]

# productive hobbies 
productive_hobbies = ["Video Edit", "Draw", "Writing"]

# relaccs/earned activities
earned_activites = ["Watch TV", "Watch Movies", "Game", "Socialize"]

# breaks that are good for you
good_breaks = ["Wim Hof", "Romance Ideas", "5min Meditate", 
               "10min Free Drawing", "10min Journal", "Write Poetry"]

# daily activities
daily_activities = ["Make Food", "Eat", "Tidy Kitchen"]

# weekly activities
weekly_activities = ["Meal Plan", "Tidy House", "Laundry"]

# add any appointments, tasks, events, goals, must-dos, should-dos, want-tos

# a master list (probabaly a dictionary) of sequencial activities defined by the user
routines = ["Morning", "Bedtime", "After Work"]


# sample 
historical_data_df = pd.read_csv('Activity  - Daily Log.csv')
standard_activities = historical_data_df['Action'].unique()
standard_activities_df = pd.DataFrame(data=standard_activities)
print(standard_activities)
#'Activity','Description','Estimated_Duration'

# a baseline empty csv to start from
todo_df = pd.read_csv('ToDo.csv')
    
print(todo_df)

app = dash.Dash(__name__)
# layout: title, dropdown to select activity, input to set description and est duration w add to day button, data table below
app.layout = html.Div(children = [
    html.H1('Today I Will-'),
    html.H2('Create list of activities you plan to do today:'),
    dt.DataTable(
        id='datatable_log',
        data=todo_df.to_dict('records'),
        columns=[
                {'name': 'Activity', 'id': 'Activity', 'deletable': False, 'renamable': False, 'presentation':'dropdown'},
                  {'name': 'Description', 'id': 'Description', 'deletable': True, 'renamable': True},
                  {'name': 'Estimated_Duration', 'id': 'Estimated_Duration', 'deletable': True, 'renamable': True}   
                
            ],
        dropdown = {                      #dictionary of keys that represent column IDs,
            'Activity': {                #its values are 'options' and 'clearable'
                'options': [            #'options' represents all rows' data under that column
                    {'label': i, 'value': i}
                    for i in sample_activities
                ],

                'clearable':True
            }},
        editable=True),
    html.Button('Add Activity', id='add_activity_button', n_clicks=0),
    html.Button('Export to Excel', id='save_to_csv', n_clicks=0),
    #html.Button('Calculate Totals', id='calc_totals_button', n_clicks=0),
    
    # Create notification when saving to excel
    html.Div(id='placeholder', children=[]),
    dcc.Store(id="store", data=0),
    #dcc.Interval(id='interval', interval=1000),

    #html.Div(id='display_sum_output',children=[]),
    dcc.Graph(id='todo_graph')
    ])

@app.callback(
    Output('datatable_log', 'data'),
    [Input('add_activity_button','n_clicks')],
    [State('datatable_log','data'),
     State('datatable_log','columns')]
    )
def add_activity_row(n_clicks, rows, columns):
    print(rows)
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    print(rows)
    return rows

@app.callback(
    Output('todo_graph', 'figure'),
    [Input('datatable_log','data')]
    )
def display_todo_graph(data):
    df_fig = pd.DataFrame(data)
    fig = px.pie(df_fig, names='Activity', values='Estimated_Duration')
    return fig
# need to add a state for storage so stuff doesnt get update so many times
# currently many csv files get generated but we need to limit
# the update soley to when the whole table state is complete or something
# dcc.Store(id='session', storage_type='session'), 
# likely need to store the whole table 
@app.callback(    
     [
      Output('placeholder','children'),
     Output('store','data')],
    [Input('save_to_csv','n_clicks')],
    [State('datatable_log','data'),
     State('store','data')]     
    )
def save_todo_to_csv(n_clicks, data, s):
    current_time = datetime.now().strftime("%Y%m%d-%H%M_")
    store_df = pd.DataFrame(data)
    store_df.to_csv(current_time+'todo.csv')
    # this is super broken and doesnt actually use the button!
    if n_clicks > 0:
            output = html.Plaintext("The TO DO list has been created and saved.")
    else:
        output = html.Plaintext("")
    return output, s

# @app.callback(
#     Output('display_sum_output','children'),
#     [Input('calc_totals_button','n_clicks'),
#      Input('datatable_log','data')]
#     )
# def calc_est_sum(clicks, data):
#     if clicks < 1:
#         raise pu
#     tmp_df = pd.DataFrame(data)
#     sum_value = tmp_df['Estimated_Duration'].sum()
#     print(tmp_df['Estimated_Duration'].sum())
#     #sum_value_string = str(sum_value)
#     tmp_string = "Estimated x hours planned today: "
#     return html.Plaintext(tmp_string)
# dcc.Dropdown(id='activity_dropdown',
#                     options=[                    
#                         {'label':i, 'value':i} for i in sample_activities
#                     ],
#                     value='activity',
#                     multi=False,
#                     clearable=False,
#                     placeholder='Activity'
#                 ),
#{"name": i, "id": i, "deletable": False, "selectable": False} for i in todo_df().columns
# callback which takes the button n_clicks + the value of the 3 fields
# 0. new instance of activity
# 1. writes the activity (row) to the spreadsheet 
# 2. updates the dataframe
# creates a new row in the table / appends the three values to the dataframe
# outputs to the datatable
# [{'name': 'Activity', 'id': 'Activity', 'deletable': False, 'renamable': False},
#                   {'name': 'Description', 'id': 'Description', 'deletable': True, 'renamable': True},
#                   {'name': 'Estimated_Duration', 'id': 'Estimated_Duration', 'deletable': True, 'renamable': True}          
#             ]

#{"name": i, "id": i, "deletable": False, "selectable": False} for i in todo_df.columns

# @app.callback(
#     Output(component_id='datatable_log', component_property='data'),
#     [Input(component_id='activity_dropdown', component_property='value'),
#     Input(component_id='description_input',component_property='value'),
#     Input(component_id='est_duration_input',component_property='value'),
#     Input(component_id='add_activity_button', component_property='n_clicks')],
#     State('datatable_log', 'data'),
#     State('datatable_log', 'columns'))
# def update_todo_list(activity, description, est_duration, add_new,rows,columns):
#     # issue: after you click this once it will update every field update
#     if add_new < 1:
#         raise pu
#     # 
#     # create a tmp dff
#     todo_dff = todo_df
#     activity_df = pd.DataFrame(
#         {0: [activity], 1:[description], 2: [est_duration]}
#         )
#     #print(activity_df)
    
#     todo_dff.append(activity_df) 
#     #ret = todo_dff().to_json(orient='records')
#     #today_todo_list.add_activity(tmp_activity)    
#     #print(tmp_activity.describe())
#     # then we add it into the spreadsheet
#     #update_csv_file = open(today_todo_list.path,'w')
#     #writer = csv.writer(update_csv_file)
#     # there is a describe method that returns a list of the values (hopefully)
#     #write_me = "%s,%s,%s",tmp_activity.activity,tmp_activity.description,tmp_activity.est_duration
#     #writer.writerow(tmp_activity.describe())
    
#     # good practice to close things after you are done
#     #update_csv_file.close()
    
#     # do i need to append this row? 
#     # now that csv is updated, we can get a fresh copy of the dataframe
    
#     print(todo_dff)
    
#     return todo_dff()

if __name__ == '__main__':
    app.run_server(debug=True)