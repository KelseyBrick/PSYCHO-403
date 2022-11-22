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
start_msg = "Welcome to my experiment! Press any key to begin."
#-define block (start)/end text using psychopy functions

block_msg = "Press any key to continue to the trial."
    
end_experiment_msg = "End of trials and the experiment. Press any key to exit."

textStim = visual.TextStim(win)                                                 #create undefined text stimulus 

#-define stimuli using psychopy functions (images, fixation cross)
# stims = img                                                                     #create a list if images to show (uses code lines 69-82 from IMAGES AND TRIAL SETTINGS)                                                                  #create a number of trials for your images
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
event.waitKeys()                                                                #wait for keypress

#=====================
#BLOCK SEQUENCE
#=====================
counter = 0
#-for loop for nBlocks *
for block in nBlocks:
    counter = counter + 1
    #-present block start message
    textStim.text = ('Block ' + str(counter) + '. ' + block_msg)                #define the text
    textStim.draw()                                                             #draw block message
    win.flip()                                                                  #show the next stim
    event.waitKeys()                                                            #wait for keypress
    #-randomize order of trials here 
    np.random.shuffle(img)                                                      #random, counterbalnced trial order
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trial in nTrials:
        #-set stimuli and images properties for the current trial
        my_image.image = os.path.join(image_dir, img[trial])
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw fixation
        fixCross.draw()                                                         #draw
        #-flip window
        win.flip()                                                              #show
        #-wait time (stimulus duration)
        core.wait(.75)                                                          #wait 0.75 seconds, then:
        
        #-draw image
        my_image.draw()                                                         #draw
        #-flip window
        win.flip()                                                              #show
        #-wait time (stimulus duration)
        core.wait(1)                                                            #wait 1 seconds, then:
        
#-draw end trial text
textStim.text = end_experiment_msg                                              #define the text
textStim.draw()                                                                 #draw end of experiment message
#-flip window
win.flip()                                                                      #show
#-wait time (stimulus duration)
core.wait(3.0)                                                                  #wait 3 seconds
        
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