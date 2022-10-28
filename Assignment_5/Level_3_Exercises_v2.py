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
from psychopy import core, gui, visual, event
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os, random, pprint

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
#-create a dialogue box that will collect current participant number, age, gender, 
    #handedness
#get date and time
#-create a unique filename for the data

#=====================
#images AND TRIAL SETTINGS
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
path = image_dir 
fileList = os.listdir(path)
missing = [name for name in img if name not in fileList]                        # identifies which image is missing if the fileList and img[] don't match
if missing == []:                                                               # if missing returns None value == True and fileList and img[] MATCH
    print('The lists match')
else:                                                                           # if missing returns ANY value then the fileList and img[] DON'T MATCH
    print('This image is missing: ' + str(missing) + '. The image lists do not match up!')

    

#-images properties like size, orientation, location, duration *
imgHeight = 200
imgWidth = 200                                                                  # 200 x 200 pixels
imgOriention = ''                                                               # ???
imgLocation = ''                                                                # centre screen
imgDuration = 1                                                                 # 1 sec

crossDuration = ''                                                              # 1 sec

screenHeight = ''                                                               # ???
screenWidth = ''                                                                # ???
#-start message text *
msgStart = 'Welcome to the experiment!'
msgEnd = 'Wait for next image'

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
#-create counterbalanced list of all conditions *
conditions = list(zip(nTrials, img))                                            # balanced list 
pprint.pprint(conditions)

np.random.shuffle(conditions)                                                   # counterbalanced list 
pprint.pprint(conditions)


#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for participant responses (e.g., "on this trial, response was a 
    #X") *
responses = []                                                                  # blank list to collect responses
for trial in nTrials:
    print(msgStart)
    print('Do x ...')                                                           # input instructions
    response = input()                                                          # participant input
    responses.append(response)                                                  # function to add responses to list above
    print(msgEnd)

#-create an empty list for correct responses (e.g., "on this trial, a response of X is 
    #correct") *
correctResponses = []                                                           # blank list to collect: correct, incorrect, error responses   
for response in responses:                                                      # if, elif, else statements to determine response correct
    if response == 'x':
        response = 'correct'
        correctResponses.append(response)
    elif response == 'y':
        response = 'incorrect'
        correctResponses.append(response)
    else:
        response = 'error'
        correctResponses.append(response)
 ###### ADD response collection code
 
#-create an empty list for response accuracy collection (e.g., "was participant 
    #correct?") *
accuracy = []                                                                   # blank list to collect response accuracy (yes, no, error)    
for response in correctResponses:                                               # if, elif, else statements to determine response accuracy
    if response == 'correct':
        accurate = 'yes'
        accuracy.append(accurate)
    elif response == 'incorrect':
        accurate = 'no'
        accuracy.append(accurate)
    else:
        accurate = 'error'
        accuracy.append(accurate)
 ###### ADD response collection code
#-create an empty list for response time collection *
rtData = []
#-create an empty list for recording the order of images identities *
imgID = []
#-create an empty list for recording the order of images properties *
imgProperties = []

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
counter = 0
for block in nBlocks:
    counter = counter + 1
    #-present block start message
    print('Welcome to Block ' + str(counter))
    #-randomize order of trials here *
    np.random.shuffle(conditions)                                               # random, counterbalnced trial order
####np.random.shuffle(nTrial)                                                   # alternate code to shuffle trial order
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trial in nTrials:
        #-set stimuli and images properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw images
        #-flip window
        #-wait time (images duration)
        #-draw images
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment