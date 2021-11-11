# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:46:48 2021

Review Activities

eventual goal: Using a slider selection we can interactively see time distributions

Given a todo text file
Iterate through each line and find the groups 
take anything with m- and add it to the next to do
anything with a d- is counted "you completed x things yesterday"

# identify groups:
    tabs indicte new groups of lines 
    (each line can be treated as an activity, can skip)
    
    
    (when interface the groups can be editable fields)
    (when have tie to phone screentime data you that gets grouped?)
    
    

@author: Patty Whack
"""
#import re


# turn this into a 'get done and missed' function
m_reggie = "m-"
d_reggie = "d-"

missed_list = []
done_list = []

with open('data/2021-11-05-sample.txt', 'r') as today_list:
    
    # use the map function to do this smarter eventually
    #something = map(re.findall(m_reggie, today_list[]), today_list)
    split_lines = today_list.read().split("\n")
    
    for line in split_lines:
        # tabs are being replaced but could be used to structure an object
        line = line.replace('\t', '')
        # count the tabs?
        
        print(line)
        # todo use map() function to do this work
        
        if m_reggie in line:
            #print(line + " missed activity")
            missed_list.append(line)
            
        elif d_reggie in line:
            #print(line + " done activity")
            done_list.append(line)

print("you completed " + str(len(done_list)) + " activities and missed " + str(len(missed_list)) + " activties")

# this might need to be a raw r
t_reggie = "\t"
colon_reggie = ":\n"
empty_line_reggie = ""
#print(str(missed_list))
#print(str(done_list))

# next we gather the detail_groups 
# each group has a title followed by : 
# group ends where there is a blank line
'''
with open('data/2021-11-05-sample.txt', 'r') as detail_grouper_list:
    #details_split_lines = detail_grouper_list.read().split("\n")
    
    # for now ill do this a stupid wat 
    i = 0
    for a_line in detail_grouper_list:
        if colon_reggie in a_line:
            
            print(str(i) + " " + a_line)  
            # so we've found the group starts but now 
            # need to crawl ahead until the next empty line for the next
            # start new loop until the next empty line
            # this sounds really stupid
            
            i += 1          

'''
#?into json?