# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 18:13:45 2022

@author: kelse
"""
# #==================
# # KEYPRESS EXCERSICES
# #==================

# from psychopy import core, gui, visual, event, monitors                         # core for this lesson
# # from psychopy import core, gui, visual, event, monitors
# #-define the monitor settings using psychopy functions
# mon = monitors.Monitor('myMonitor',
#                        width=48.93,
#                        distance=75)                                            #defines name, width, and viewing distance from monitor
# mon.setSizePix([1920,1080])                                                    #defines the pixel resolution with (x,y) coordinates
# win = visual.Window(monitor=mon)                                               #define a window


# nTrials=3
# my_text=visual.TextStim(win)
# fix=visual.TextStim(win, text='+')

# # event.clearEvents()                                                         #no responses were being collected from first trial with the line of code here.

# for trial in range(nTrials):
    
#     keys = event.getKeys(keyList=['1','2'])                                     #define getkeys
#     my_text.text = ("Trial " + str(trial) + "...Press keys 1 or 2")                
    
#     fix.draw()
#     win.flip()
#     core.wait(2)
    
#     event.clearEvents()                                                         #clear any keys presses just prior to collecting responses
    
#     my_text.draw()
#     win.flip()
#     core.wait(1)
    
#     print("The keys pressed were ", keys)                                       #which key did the subject were press?
    
#     if keys:
#         sub_resp = keys[0]                                                      #if more than one key pressed only take the first response
#         print("Only this key press counted: ", sub_resp)

# # if keys:
# #     sub_resp = keys[0]                                                      #not indented properly leads to only last response collected
# #     print("Only this key press counted: ", sub_resp)
    
# win.close()


#==================
# DATA COLLECTION
#==================

from psychopy import core, event, visual, monitors
import numpy as np
import os, csv
# from datetime import datetime


#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()                                                          # C:\Users\kelse\Google Drive\00 University of Alberta\2022- Fall\PSYCH 403
#-define the directory where you will save your data
data_dir = os.path.join(main_dir, 'experiments','exercise_data')                # C:\Users\kelse\Google Drive\00 University of Alberta\2022- Fall\PSYCH 403\experiments\exercise_data
#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'experiments','exercise_stimulus')            # C:\Users\kelse\Google Drive\00 University of Alberta\2022- Fall\PSYCH 403\experiments\exercise_stimulus
#-check that these directories exist >>> SEE BELOW (Lines 57-63)

#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor',
                        width=48.93,
                        distance=75)                                            # defines name, width, and viewing distance from monitor
mon.setSizePix([1920,1080])                                                     # defines the pixel resolution with (x,y) coordinates
win = visual.Window(monitor=mon)                                                # define a window

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=3
my_text=visual.TextStim(win)
rt_clock = core.Clock()                                                         # create a response time clock
cd_timer = core.CountdownTimer()                                                # add countdown timer

# prefill lists for responses 
sub_resp = [[0]*nTrials]*nBlocks
sub_acc = [[0]*nTrials]*nBlocks
prob = [[0]*nTrials]*nBlocks
resp_time = [[0]*nTrials]*nBlocks
corr_resp = [[0]*nTrials]*nBlocks

#create problems and solutions to show
math_problems = ['1+1=','3-2=','4-1=']                                   # write a list of simple arithmetic
solutions = [2,1,3]                                                           # write solutions
prob_sol = list(zip(math_problems,solutions))

#set-up blank dictionaries
sub_resp = {}
sub_acc = {}
prob = {}
resp_time = {}
corr_resp = {}

for block in range(nBlocks):
    sub_resp[block] = [0]*nTrials
    sub_acc[block] = [0]*nTrials
    prob[block] = [0]*nTrials
    resp_time[block] = [0]*nTrials
    corr_resp[block] = [0]*nTrials
    for trial in range(nTrials):
        # corr_resp[trial] = [0]*nTrials
        # sub_resp[trial] = [0]*nTrials
        # sub_acc[trial] = [0]*nTrials
        # prob[trial] = [0]*nTrials
        # resp_time[trial] = [0]*nTrials
        # corr_resp[trial] = [0]*nTrials
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(3)]                      # select problem at random from zip list
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()                                                        # reset timing for every trial
        cd_timer.add(2)                                                         # add 3 seconds

        event.clearEvents(eventType='keyboard')                                 # reset keys for every trial
        
        count = -1                                                              # for counting keys
        while cd_timer.getTime() > 0:                                           # for 2 seconds

            my_text.text = prob[block][trial][0]                                # present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','escape'])

            if keys:
                count = count + 1                                               # count up the number of times a key is pressed

                if count == 0:                                                  # first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0]                            # remove from list

        #record subject accuracy
        #correct-                                                               # remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1                                           # arbitrary number for accurate response
        #incorrect-                                                             # remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2                                           # arbitrary number for inaccurate response 
                                                                                # (should be something other than 0 to distinguish from non-responses)                  
        #print results
        print('Problem =', prob[block][trial], 'Correct response =', 
              corr_resp[block][trial], 'Subject response =',sub_resp[block][trial], 
              'Subject accuracy =',sub_acc[block][trial], 'Response time =',resp_time[block][trial])
        
win.close()
print(sub_resp)
print(dict.values(sub_resp))
print(dict.keys(sub_resp))
#==================
# .CSV EXERCISE
#==================
   
filename = 'testDataNov292022'
fullAddress = os.path.join(data_dir, filename)                                  #instead of typing a file name in the 'with open', this creates a filename and the place to save it

with open(fullAddress + '.csv', mode='w', newline='') as csvFile:
    fieldnames = ['block', 'trial', 'problem','correct_answer','subject_response','subject_accuracy', 'response_time']
    data_writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    
    data_writer.writeheader()
    for iBlock in range(nBlocks):
        for iTrial in range(nTrials):
            data_writer.writerow({'block':iBlock, 'trial':iTrial,
                                  'problem':prob[iBlock]['problem'][iTrial],
                                  'correct_answer':corr_resp[iBlock]['correct_answer'][iTrial],
                                  'subject_response': sub_resp[iBlock]['subject_response'][iTrial],
                                  'subject_accuracy': sub_acc[iBlock]['subject_accuracy'][iTrial],
                                  'response_time': resp_time[iBlock]['response_time'][iTrial]})
            # data_writer.writerow({'problem':prob[1],
            #                       'correct_answer':corr_resp[1],
            #                       'subject_response': sub_resp[1],
            #                       'subject_accuracy': sub_acc[1],
            #                       'response_time': resp_time[1]})
            # data_writer.writerow({'problem':prob[0],
            #                       'correct_answer':corr_resp[0],
            #                       'subject_response': sub_resp[0],
            #                       'subject_accuracy': sub_acc[0],
            #                       'response_time': resp_time[0]})
            # data_writer.writerow({'problem':prob[1],
            #                       'correct_answer':corr_resp[1],
            #                       'subject_response': sub_resp[1],
            #                       'subject_accuracy': sub_acc[1],
            #                       'response_time': resp_time[1]})