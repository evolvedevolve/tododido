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
import re

m_reggie = "m-"
d_reggie = "d-"


missed_list = []
done_list = []


with open('data/2021-11-05-sample.txt', 'r') as today_list:
    #missed_list = []
    
    #something = map(re.findall(m_reggie, today_list[]), today_list)
    split_lines = today_list.read().split("\n")
    
    for line in split_lines:
        #line = 
        line = line.replace('\t', '')
        # count the tabs?
        
        #print(line)
        # todo use map() function to do this work
        
        if m_reggie in line:
            #print(line + " missed activity")
            missed_list.append(line)
            
        elif d_reggie in line:
            #print(line + " done activity")
            done_list.append(line)
        #missed_match = re.findall(m_reggie, line_now, flags=0)
        #print(missed_match)
        
        '''
        if missed_match is None:
            print('no match')
            
        else:
            print('match')
            missed_list.append(line)
        '''

print("you completed " + str(len(done_list)) + " activities and missed " + str(len(missed_list)) + " activties")

#print(str(missed_list))
#print(str(done_list))