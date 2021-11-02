# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:39:39 2021

create ToDo_df - open the sheet (with dash we will use a picker or pass data between pages)

create a new Day instance
    (eventually to be replaced by a Day Class that's accessible to all pages')
inside of a while !Todo.list_done = True loop:
    for activity in todo_list.activities[]:
        populate activity_name, est_duration
        prompt for start, set start_time when pressed
        wait for stop, set stop_time
        

@author: Patty Whack
"""
#from Google import Create_Service
from datetime import datetime as dt
import time 

# quick prompt for activity name (will get replaced by live field later)
activity_name = input("What activity are you doing? ")

# get current date time today
start_time = dt.now()
# format the date 
start_date_formatted = start_time.strftime("%Y/%m/%d")
# format the time 
start_time_formatted = start_time.strftime("%H:%M")

counter_start = time.perf_counter()
print("initial_date", str(start_time))

# output 'timer started' (to be replaced with the green button, maybe a star_tmer function)
print("Starting timer...")

# press 'y' to stop session (to be replaced by the stop session button)
# unsure if this really needs to be here at this stage

# prompt "enter some thoughts on the session" (to be replaced by a live field on the page)
session_thoughts = input("Enter some thoughts on the session. When you press enter, the session will end. ")

# prompt "enter any follow up tasks" 
follow_up_tasks = input("Are there any follow up tasks for this activity? ")

# get the stop session time
end_time = dt.now()
counter_stop = time.perf_counter()
print("stop_date", str(end_time))

# subtract the end time from the start time
total_time = end_time - start_time # this is for confirmation but not accurate
counter_total = counter_stop - counter_start # this is the accurate number

print("total_time", total_time)

# format the string to be in increments of quarter hours (0.25)
total_hours = round((counter_total / 3600), 1)
print(total_hours, " worked in this session")


# create a string with each field followed by a comma ,  (to be used for creating a row in a csv)
output_string = start_date_formatted + "," + start_time_formatted + "," + str(total_hours) + "," + activity_name + "," + session_thoughts + "," + follow_up_tasks 
output_string_tabs = start_date_formatted + "\t" + start_time_formatted + "\t" + str(total_hours) + "\t" + activity_name + "\t" + session_thoughts + "\t" + follow_up_tasks 
print(output_string_tabs)
# df cat the string
# pd.to_csv() # over write the csv

# add to our sheet
# link: https://docs.google.com/spreadsheets/d/1Hze5LlqmZpmmxJy5OHQmvWkuNOG7m-1znNINdUiVuaw

# class activity

#class day_plan

# how would value work?
# ideally you do 7-9 hours of actual work in a day 
# the healthy amount of relaxation with that is 15,30,15 
# every 2hr you get a 15 min break in the regular world
# so i need a categorization system 
# could add a simple "is the this productive" then if productive earned_time = total_hours * 0.25 
# so in practice you'd be selecting existing activities or making a new one
# when you make a new one it prompts for is this productive
