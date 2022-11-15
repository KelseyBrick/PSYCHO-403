# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 13:02:05 2022

@author: kelse
"""

#Stimulus Exercises- Question 1

#========================
#IMPORT MODULES
#========================

from psychopy import visual, monitors, event
import os

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()                                                          # C:\Users\kelse\Google Drive\00 University of Alberta\2022- Fall\PSYCH 403
#-define the directory with image locations
image_dir = os.path.join(main_dir,'experiments','exercise_stimulus')            # C:\Users\kelse\Google Drive\00 University of Alberta\2022- Fall\PSYCH 403\experiments\exercise_stimulus

#=====================
#CREATION OF MONITOR AND WINDOW 
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', 
                       width=48.93, 
                       distance=75)                                             #defines name, width, and viewing distance from monitor
mon.setSizePix([1920,1080])                                                     #defines the pixel resolution with (x,y) coordinates                                                    #sets vertical position

win = visual.Window(monitor=mon)   

#=====================
#DISPLAY IMAGE STIMULI
#=====================

stims = ['face01.jpg','face02.jpg','face03.jpg', 'face04.jpg']                  #create a list if images to show
nTrials=4                                                                       #create a number of trials for your images
my_image = visual.ImageStim(win, units='pix', size=(200,200))                   #define image
fixCross = visual.TextStim(win, text='+')                                       #define fixation cross
#fixCross.setSize(200)

for trial in range(nTrials):                                                    #loop through trials 
    my_image.image = os.path.join(image_dir,stims[trial])                       #point to a different filename for each image
    
    my_image.draw()                                                             #draw
    fixCross.draw()
    win.flip()                                                                  #show
    event.waitKeys()                                                            #wait for keypress
    
win.close()                                                                     #close the window after all trials have looped    