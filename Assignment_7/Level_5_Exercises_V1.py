# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 12:22:46 2022

@author: kelse
"""
#======================
#Experiment Structure Exercises
#======================

#=====================
#IMPORT MODULES
#=====================
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event, monitors
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os, random, pprint
from datetime import datetime

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

#=====================
#COLLECT PARTICIPANT INFO
#=====================
# #-create a dialogue box that will collect current participant number, age, gender, handedness
# exp_info = {'subject_nr':0, 
#             'age':0, 
#             'handedness':('right','left','ambi'), 
#             'gender':'',                                                        #2. set to blank
#             'session': 1}

# print("All variables have been created! Now ready to show the dialog box!")

# my_dlg = gui.DlgFromDict(dictionary=exp_info, 
#                           title="Subject info",
#                           fixed=['session'],
#                           order=['session', 'subject_nr', 'age', 'gender', 'handedness'])

# #get date and time
# date = datetime.now()                                                           #what time is it right now?
# exp_info['date'] = str(date.day) + str(date.month) + str(date.year)             #adds 'date' key into the dictionary
# print(exp_info['date'])

# #-create a unique filename for the data
# filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
# print(filename)

#=====================
#IMAGES AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials = range(10)
# for Trial in nTrials
nBlocks = range(2)
# for Block in nBlocks
#-images names (and images extensions, if images) *
img = []
counter = 0
for i in range(10):
    counter = counter + 1
    img.append('face' + str(counter).zfill(2) + '.jpg')                         #.zfill() adds leading zeros to a converted string integer/float

# check if images exist in the directory
# path = image_dir 
# fileList = os.listdir(path)
# missing = [name for name in img if name not in fileList]                        # identifies which image is missing if the fileList and img[] don't match
# if missing == []:                                                               # if missing returns None value == True and fileList and img[] MATCH
#     print('The lists match')
# else:                                                                           # if missing returns ANY value then the fileList and img[] DON'T MATCH
#     print('This image is missing: ' + str(missing) + '. The image lists do not match up!')

    

# #-images properties like size, orientation, location, duration *
# imgHeight = 200
# imgWidth = 200                                                                  # 200 x 200 pixels
# imgOriention = ''                                                               # ???
# imgLocation = ''                                                                # centre screen
# imgDuration = 1                                                                 # 1 sec

# crossDuration = ''                                                              # 1 sec

# screenHeight = ''                                                               # ???
# screenWidth = ''                                                                # ???
# #-start message text *
# msgStart = 'Welcome to the experiment!'
# msgEnd = 'Wait for next image'

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
#-create counterbalanced list of all conditions *
# conditions = list(zip(nTrials, img))                                            # balanced list 
# pprint.pprint(conditions)

# np.random.shuffle(conditions)                                                   # counterbalanced list 
# pprint.pprint(conditions)


#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
# #-create an empty list for participant responses (e.g., "on this trial, response was a 
#     #X") *
# responses = []                                                                  # blank list to collect responses
# for trial in nTrials:
#     print(msgStart)
#     print('Do x ...')                                                           # input instructions
#     response = input()                                                          # participant input
#     responses.append(response)                                                  # function to add responses to list above
#     print(msgEnd)

# #-create an empty list for correct responses (e.g., "on this trial, a response of X is 
#     #correct") *
# correctResponses = []                                                           # blank list to collect: correct, incorrect, error responses   
# for response in responses:                                                      # if, elif, else statements to determine response correct
#     if response == 'x':
#         response = 'correct'
#         correctResponses.append(response)
#     elif response == 'y':
#         response = 'incorrect'
#         correctResponses.append(response)
#     else:
#         response = 'error'
#         correctResponses.append(response)
#  ###### ADD response collection code
 
# #-create an empty list for response accuracy collection (e.g., "was participant 
#     #correct?") *
# accuracy = []                                                                   # blank list to collect response accuracy (yes, no, error)    
# for response in correctResponses:                                               # if, elif, else statements to determine response accuracy
#     if response == 'correct':
#         accurate = 'yes'
#         accuracy.append(accurate)
#     elif response == 'incorrect':
#         accurate = 'no'
#         accuracy.append(accurate)
#     else:
#         accurate = 'error'
#         accuracy.append(accurate)
#  ###### ADD response collection code
# #-create an empty list for response time collection *
# rtData = []
# #-create an empty list for recording the order of images identities *
# imgID = []
# #-create an empty list for recording the order of images properties *
# imgProperties = []

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
# from psychopy import core, gui, visual, event, monitors
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', 
                       width=48.93, 
                       distance=75)                                             #defines name, width, and viewing distance from monitor
mon.setSizePix([1920,1080])                                                     #defines the pixel resolution with (x,y) coordinates

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon)
# win = visual.Window(monitor=mon, 
#                     size=(1600,900),
#                     color=('#ad17a3'),
#                     units='height',
#                     fullscr=None                                                #can be set to 'fullscr=True'; not done to prevent getting stuck in fullscr. 
#                     )

#-define experiment start text unsing psychopy functions
start_msg = "Welcome to my experiment! Wait to begin."
#-define block (start)/end text using psychopy functions
block_msg = "Wait for trial to begin."
end_experiment_msg = "End of trials and the experiment. Thank you."

textStim = visual.TextStim(win)                                                 #create undefined text stimulus 

#-define stimuli using psychopy functions (images, fixation cross)
# stims = img                                                                   #create a list if images to show (uses code lines 69-82 from IMAGES AND TRIAL SETTINGS)                                                                  #create a number of trials for your images
my_image = visual.ImageStim(win, units='pix', size=(200,200))                   #create the stimulus; this script only works with units and size defined.
fixCross = visual.TextStim(win, text='+')                                       #define fixation cross

#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
textStim.text = start_msg                                                       #define the text
textStim.draw()                                                                 #draw start message
win.flip()                                                                      #show the stim
#-allow participant to begin experiment with button press
core.wait(2.0)                                                                  #wait 2 seconds

blockTimer = core.Clock()
trialTimer = core.Clock()
stimTimer = core.Clock()

#=====================
#BLOCK SEQUENCE
#=====================
counter = 0
#-for loop for nBlocks *
for block in nBlocks:
    blockTimer.reset()
    blockStart = blockTimer.getTime()
    
  #  counter = counter + 1
    #-present block start message
    textStim.text = ('Block ' + str(block + 1) + '. ' + block_msg)              #define the text
    textStim.draw()                                                             #draw block message
    win.flip()                                                                  #show the next stim
    core.wait(2.0)                                                              #wait 2 seconds
    # event.waitKeys()                                                         
    #-randomize order of trials here 
    np.random.shuffle(img)                                                      #random, counterbalnced trial order
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trial in nTrials:
        trialTimer.reset()
        trialStart = trialTimer.getTime()
        #-set stimuli and images properties for the current trial
        my_image.image = os.path.join(image_dir, img[trial])
        #-empty keypresses
        #=====================
        #START TRIAL
        #=====================   
        stimTimer.reset()
        while stimTimer.getTime() <= 1:                                         #clock timer
            #-draw fixation
            fixCross.draw()                                                     #draw
            #-flip window
            win.flip()                                                          #show
        #-wait time (stimulus duration)
        # core.wait(.75)                                                        
        stimTimer.reset()
        while stimTimer.getTime() <= .5:                                        #clock timer
            #-draw image
            my_image.draw()                                                     #draw
            #-flip window
            win.flip()                                                          #show
        #-wait time (stimulus duration)
        # core.wait(1)                                                          
        trialEnd = trialTimer.getTime()
    blockEnd = blockTimer.getTime()    
#-draw end trial text
textStim.text = end_experiment_msg                                              #define the text
textStim.draw()                                                                 #draw end of experiment message
#-flip window
win.flip()                                                                      #show
#-wait time (stimulus duration)
core.wait(2.0)                                                                  #wait 2 seconds
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial

#======================
# END OF EXPERIMENT
#======================        
#-write data to a file

#-close window
win.close()                                                                     #close the window after all trials have looped                                    
#-quit experiment