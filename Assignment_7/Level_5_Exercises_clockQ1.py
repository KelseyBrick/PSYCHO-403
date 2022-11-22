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
wait_timer = core.Clock()
                                                                       #create a number of trials for your images
#create the stimulus but don't specify the precise image yet
my_image = visual.ImageStim(win)

for trial in range(nTrials):                                                    #loop through trials
    #point to a different filename for each image
    my_image.image = os.path.join(image_dir,stims[trial])
    my_image.draw()                                                             #draw
    win.flip()                                                                  #show
    imgStartTime = wait_timer.getTime()                                         #start timing image presentation
    core.wait(2)                                                                #wait 2 seconds
    imgEndTime = wait_timer.getTime()                                           #stop timing image presentation
    
    print('Image time: {} seconds'.format(imgEndTime - imgStartTime))
    
win.close()                                                                     #close the window after all trials have looped   