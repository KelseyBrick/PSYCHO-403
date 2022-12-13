# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:17:52 2022

@author: kelse
"""

#figuring out how to define a mouse click location in an image object
#=====================
#IMPORT SETTINGS
#=====================

from psychopy import visual, event, core, data, gui, monitors, misc             # as written as 'import psychopy.visual', etc.
import numpy as np
import os, csv, random, sys

#=====================
#PATH SETTINGS
#=====================
main_dir = os.getcwd()                                                          # C:\Users\kelse\Google Drive\00 University of Alberta\2022- Fall\PSYCH 403\Experiment project
data_dir = os.path.join(main_dir,'experimentData')                              # C:\Users\kelse\Google Drive\00 University of Alberta\2022- Fall\PSYCH 403\Experiment project\experimentData
image_dir = os.path.join(main_dir, 'images')                                    # C:\Users\kelse\Google Drive\00 University of Alberta\2022- Fall\PSYCH 403\Experiment project\images

#=====================
#WINDOW AND MONITOR SETTINGS
#=====================
# mon = monitors.Monitor('myMonitor', 
#                         width=35.56, 
#                         distance=75)                                            #defines name, width, and viewing distance from monitor

# mon.setSizePix([1920,1080])                                                     #defines the pixel resolution with (x,y) coordinates
#monitor=mon, 
win = visual.Window(units='norm', size= [1000,642], fullscr=None)  #-defines window (size, color, units, fullscreen mode, etc.) 
                                                                                # normalized units: window has a total height of 1:-1 = 2
#=====================
#STIMULUS SETTINGS
#=====================
waldoImage = visual.ImageStim(win, size=2, interpolate=True)                    #define image variable; script only works with size=2 fills window.
waldoImage.image = os.path.join(image_dir, 'wallpaperflare.com_wallpaper (2).jpg') #original size = 1920 x 1233 px 

mouse = event.Mouse()

x = visual.TextStim(win, text='x', color='black')
findWaldo = np.array([])                                                        #Waldo locations

waldoImage.draw()
win.flip()
if mouse.getPressed(waldoImage):
# if mouse.isPressedIn(waldoImage):
    loc = mouse.getPos()                                                        #setting location equal to mouse starting point where starts in the window, not where it is moved and clicked
    findWaldo = np.append(findWaldo, loc)
event.waitKeys()

# test click location 
waldoImage.draw()
x.pos = findWaldo
x.draw()
win.flip()    
event.waitKeys()
win.close()

print(findWaldo)