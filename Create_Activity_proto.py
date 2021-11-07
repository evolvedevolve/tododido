# -*- coding: utf-8 -*-
"""
Created on Sat Nov 06 13:34:09 2021

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
  
@author: Patty Whack
"""
import pandas as pd
#import os

# load the activities dataframe
df =  pd.read_csv('data/Activity-Daily-Log_October.csv')

#dir_tmp = os.listdir()
#print(dir_tmp)
#print(df)
#print(df['Action'].value_counts())


''' this is for better usage 

data_url = 'http://vincentarelbundock.github.io/Rdatasets/csv/carData/Salaries.csv'
df = pd.read_csv(data_url, index_col=0)

'''


#https://docs.google.com/spreadsheets/d/1Hze5LlqmZpmmxJy5OHQmvWkuNOG7m-1znNINdUiVuaw/edit#gid=0
# get all of the unique activities and
# get the mean time for each activity
activities = df.Action.unique()
#print(activities)

# one option 
activity_means = []
activity_groups = df.groupby(['Action'])
for activity in activities:
     tmp_group = activity_groups.get_group(activity)
     group_mean = tmp_group.mean()
     activity_means.append(str(group_mean.mean()))
     #print(activity + "," + str(group_mean.mean()))

#print(activities)

# smarter option once i understand pandas and numpy better
#activity_means = activity_groups.agg({"Duration","mean"})
#print(activity_means)
#output_dict = {'Activity': activities, 'Mean Duration': activity_means}
#data = output_dict
unsorted_df = pd.DataFrame({
    'activity_name' : activities,
    'mean_duration' : activity_means
    })
sorted_activities = unsorted_df.sort_values('mean_duration', ascending=False)
indexed_sorted_activities = sorted_activities.reset_index(drop=True)
# okay there is this dumb extra index but im just selecting a column anyway
indexed_sorted_activities.to_csv('data/activities.csv')
print(indexed_sorted_activities.head())

#, 'Mean Duration': activity_means