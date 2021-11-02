# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 15:51:09 2021

Create_Activity
in which we use dash to create unique new activities,
which can then be used on a to do list
parameters -
    id - serialized number for lookup (uhg then this means that category has its own class...)
    category - a generalized classification of the type of activity
    activity_name - Short one or two word name
    description - (optional) longer form details of the activity (likely filled out when the day is executed)
    est_duration - standard amount of time you will do this thing    
    relaccs_factor - a multiplier used to calcuate earned_relaccs for a day (is this really what i want?)
    status - complete?incomplete? ongoing? just a quoto? quota met?    
    recurring?
    

layout
    h1 - Create Actitivity
    input - category
    daily_things[]
    
    thing
    
    input - activity_name_input 
    
    datatable - activities

callback controls
on load - do nothing until create new is clicked
    

@author: Patty Whack
"""

