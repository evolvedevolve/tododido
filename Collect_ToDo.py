# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:29:36 2021

@author: Patty Whack
"""

import dash
import dash_table as dt
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate as pu
import pandas as pd
import csv
from datetime import datetime
#import webbrowser as wxb

# when script is called
# 1. create a new spreadsheet for %today-todo
# 2. give it the header row as expected ["activity","description","duration"]
# 3. new dataframe from the sheet
# interface to collec the data for a table
# consisting on varoius action items

class Activity:
    def __init__(self, activity, est_duration, description):
        self.activity = activity
        self.est_duration = est_duration
        self.description = description
        
    def describe(self):
        ret = {'Activity' : self.activity, 'Description': self.description, 'Estimated_Duration': self.est_duration}
        print(ret)
        return ret

# a list of activities to select from 
sample_activities = ["Learn Python", "Make Food", "Recap", "Plan", "Errands",
                     "Groceries", "Make Food", "Eat", "Walk", "Game", "Cat Care"] #todo make add to activities
print(sample_activities)

class ToDo_List:
    def __init__(self,path):
        self.start_date_time = datetime.now().strftime("%Y%m%d-%H%M_")
        self.path = self.start_date_time+path
        self.activities = []
        self.create_csv()
        
    def create_csv(self):
        headers =  ['Activity','Description','Estimated_Duration']
        first_row = ['Plan Day','Use awesome tool', '0.25']
        print(self.path)
        new_file = open(self.path, 'w')
        new_writer = csv.writer(new_file)
        new_writer.writerow(headers)
        new_writer.writerow(first_row)
        new_file.close()
        
    def add_activity(self, activity):
        self.activities.append(activity)
        print('in add_activity')
        update_csv_file = open(self.path,'w')
        update_writer = csv.writer(update_csv_file)
        tmp = activity.describe()
        print(tmp)
        update_writer.writerow(tmp)
        update_csv_file.close()
        
    def read_activities(self):
        pass
    
    def get_dataframe(self):
        print(self.path)
        df = pd.read_csv(self.path)
        #print(df)
        # call this to get the current state of the csv
        return df
        
app = dash.Dash(__name__)

today_todo_list = ToDo_List('ToDo.csv')
todo_df = today_todo_list.get_dataframe()

# layout: title, dropdown to select activity, input to set description and est duration w add to day button, data table below
app.layout = html.Div(children = [
    html.H1('Today I Will-'),
    html.H2('Create list of activities you plan to do today:'),
    html.Div(children=[
        dcc.Dropdown(id='activity_dropdown',
                    options=[                    
                        {'label':i, 'value':i} for i in sample_activities
                    ],
                    value='activity',
                    multi=False,
                    clearable=False,
                    placeholder='Activity'
                ),
        dcc.Input(id='description_input',placeholder='Description'),
        dcc.Input(id='est_duration_input',placeholder='Est. Duration'),
        html.Button('Add Activity', id='add_activity_button', n_clicks=0)
        ],style={'width': '25%', 'display': 'inline-block'}),
    dt.DataTable(
        id='datatable_log',        
        data=todo_df.to_dict('records'),
        columns=[
                {"name": i, "id": i, "deletable": False, "selectable": False} for i in todo_df.columns
            ],
        editable=True
    )])
#Value provided: "{\"Make Food\":{},\"ddd\":{},\"ddd.1\":{}}"
# callback which takes the button n_clicks + the value of the 3 fields
# 0. new instance of activity
# 1. writes the activity (row) to the spreadsheet 
# 2. updates the dataframe
# creates a new row in the table / appends the three values to the dataframe
# outputs to the datatable
#omponent_property='n_rows'),#activity_dropdown
#n_clicks
@app.callback(
    Output(component_id='datatable_log', component_property='data'),
    [Input(component_id='activity_dropdown', component_property='value'),
    Input(component_id='description_input',component_property='value'),
    Input(component_id='est_duration_input',component_property='value'),
    Input(component_id='add_activity_button', component_property='n_clicks')],
    State('datatable_log', 'data'),
    State('datatable_log', 'columns'))
def update_todo_list(activity, description, est_duration, add_new,rows,columns):
    # issue: after you click this once it will update every field update
    if add_new < 1:
        raise pu
    # when add row is called
    # we create a new activity object
    tmp_activity = Activity(activity, est_duration, description)
    today_todo_list.add_activity(tmp_activity)
    
    #print(tmp_activity.describe())
    # then we add it into the spreadsheet
    #update_csv_file = open(today_todo_list.path,'w')
    #writer = csv.writer(update_csv_file)
    # there is a describe method that returns a list of the values (hopefully)
    #write_me = "%s,%s,%s",tmp_activity.activity,tmp_activity.description,tmp_activity.est_duration
    #writer.writerow(tmp_activity.describe())
    
    # good practice to close things after you are done
    #update_csv_file.close()
    
    # do i need to append this row? 
    # now that csv is updated, we can get a fresh copy of the dataframe
    tmp_todo_list_dataframe = today_todo_list.get_dataframe()
    print(tmp_todo_list_dataframe)
    
    return tmp_todo_list_dataframe

# make a today_todo_csv file
# which is the list of the activities we will take as input for the 
# day planner, extend it to contain time information- and executor, 
if __name__ == '__main__':
    app.run_server(debug=True)

    