# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 12:24:45 2022

@author: kelse
"""

from psychopy import visual, monitors, event, core
import os

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1280,720])
win = visual.Window(monitor=mon)                                                #define a window

#define directory
# os.chdir('/home/shoarly/Documents/pytutorial/exp')                            
main_dir = os.getcwd()                                                          
image_dir = os.path.join(main_dir,'experiments','exercise_stimulus')            #stuff you only have to define once at the top of your script

#define images and locations
stims = ['face01.jpg','face02.jpg','face03.jpg']                                #create a list if images to show
nTrials=3
waitTimer = core.Clock()
stimTimer = core.Clock()                                                        #create a number of trials for your images
#create the stimulus but don't specify the precise image yet
my_image = visual.ImageStim(win)

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir, stims[trial])
    #reset stimulus presentation timer right before the first stimulus should appear
    stimTimer.reset()
    imgStartTime = waitTimer.getTime()                                          #start timing image presentation
    #-draw stimulus
    while stimTimer.getTime() <=2:                                              #2 seconds
        my_image.draw()                                                         #draw
        win.flip()                                                              #show
    imgEndTime = waitTimer.getTime()                                            #stop timing image presentation     
    print('Image time: {} seconds'.format(imgEndTime - imgStartTime))
win.close()                                                                     #close the window after all trials have looped   