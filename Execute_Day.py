# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 15:31:21 2021

need to use dunder methods 
repr and str for describe (repr is for devs str is for user reading)

Execute Day 
A day consists of:
    ToDo List (multiple activities currently with status of incomplete)
    list_complete (a boolean that is flipped once the Todo_List is complete)
    total_hours
    earned_relaccs = 
    should_do list? 
    __getitem__  for the activities individually
    
Program Flow -
    Todo_list is displayed in table
    first row is highlighted 
    current_activity is populated
    nothing happens until user presses start_activity_button
    user can enter follow up notes and details
    when stop button is pressed:
        stop_time is defined for the activity
        activity_duration is calculated
        activity_duration and relacc_factor are returned
    next row is loaded
    repeat until all of Todo_List has been iterated through
    progress graph displayed at the top or bototm gets more green every completed

would be nice to have a way to add more activites on the fly during execute_day    
    

could be able to drag things as blocks out of the lists until they are gone
    while planning then while doing

Laypout -
    h1 - execute your day
    datatable - todo_table_pre
    div 
        h2 - Curreny Activity: {activity_name}
        text_area - 
        button - start_activity_button / 
        button - end_activity_button
    progress_graph
    
    
Callback Structure -
    
    start_activity_button
    
    end_activity_button
    
    

@author: Patty Whack
"""

# execute day

# starts by defining a dataframe from your todo list

# loads up first activity - with start button and finish button and fields
# sets the h1 title to the activity 
# gives bigger text area for notes and follow up

# you press finish, loads up the next activity

# logs start_time and end_time and duration etc 

# want to be able to override values, 
#1 for the activities to be able to make new activity  with explicit fields 
#2 for the datetime picker so can override an actual end or start time 
#3 insert an activity - 

# moves onto next item 

# adds to a new pie chart of % done or a bar chart moving towards 100% horizontal green

# stuff to reserach on session 
# datetime picker 
# optional fields 
# horitOnatal bar chart
# reoder rows in a datatable
# row number of this needs to come that number



