# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:27:25 2022

@author: kelse
"""
#=====================
#IMPORT SETTINGS
#=====================
from psychopy import visual, event, core
import os
import pandas as pd

#=====================
#PATH SETTINGS
#=====================
main_dir = os.getcwd()                                                          
data_dir = os.path.join(main_dir,'experimentData')                              
image_dir = os.path.join(main_dir, 'images') 
if not os.path.exists(data_dir):                                                # raise Error: if the folder does not exist... 
   os.makedirs(data_dir)                                                        # create one
#=====================
#IMAGES AND TRIAL SETTINGS
#=====================
nTrials = 18

img = []                                                                        # list images names and extensions
counter = 0
for i in range(6):
    counter = counter + 1
    img.append('waldo' + str(counter).zfill(2) + '.jpg')                        # Condition: full size images
counter = 0
for i in range(6):
    counter = counter + 1
    img.append('waldo' + '10' + str(counter) + '.jpg')                          # Condition: 10% reduced images
counter = 0
for i in range(6):
    counter = counter + 1
    img.append('waldo' + '25' + str(counter) + '.jpg')                          # Condition: 25% reduced images

#=====================
#COLLECT INFO
#=====================
click_list = []
img_list = []
filename = ('waldoLocations.csv')                                               # filename variable 

#=====================
#STIMULUS SETTINGS
#=====================
win = visual.Window(units='norm', fullscr=True)                                 # units normalized to scale image across various window sizes = fullscreen
waldoImage = visual.ImageStim(win, size=2, interpolate=True)                    # interpolate >> helping with blurry image??
mouse = event.Mouse()
x = visual.TextStim(win, text='x', color='black')

mouseDetected = False                                                           # tracker for mouse-click depression/release 
                                                                                # (otherwise mouse.getPressed() = True, i.e. always depressed)

for trial in range(nTrials):
    waldoImage.image = os.path.join(image_dir, img[trial]) 

    waldoImage.draw()
    win.flip()
    
    while True:
        if mouse.getPressed()[0]:                                               # indexes 'left' mouse-click
            if not mouseDetected:                                               # initial mouse-click detection 
                loc = mouse.getPos()
                click_list.append(loc)
                img_list.append(img[trial])
                mouseDetected = True                                            # mouse press (depression) 
                waldoImage.draw()    
                x.pos = loc                                                     # save Waldo's location for experiment
                x.draw()                                                        # draw an 'X' and wait to verify accurate click
                win.flip()
                core.wait(.3)
                break
        else:
            mouseDetected = False                                               # mouse press (released) 

#=====================
#SAVE DATA SETTINGS
#=====================
waldoLoc_x = []                                                                 # index and save x-coordinates
for x in range(len(click_list)):
    waldoLoc_x.append(click_list[x][0])
waldoLoc_y = []                                                                 # index and save y-coordinates
for y in range(len(click_list)):
    waldoLoc_y.append(click_list[y][1])


df = pd.DataFrame(data={                                                        # use pandas to save a dataframe of waldo locations
  "Image_Name": img_list,                                                       # define column headers/lists 
  "waldoLoc_x": waldoLoc_x,
  "waldoLoc_y": waldoLoc_y                                                        
})
df.to_csv(os.path.join(data_dir, filename), sep=',', index=False)               # save the dataframe as .csv file using parameters            

#=====================
#END EXPERIMENT SESSION
#=====================
win.close()
