# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:27:25 2022

@author: kelse
"""
#=====================
#IMPORT SETTINGS
#=====================
from psychopy import visual, event
import numpy as np
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
nTrials = 6

img = []                                                                        # list images names and extensions
counter = 0
for i in range(6):
    counter = counter + 1
    img.append('waldo' + str(counter).zfill(2) + '.jpg')                        # .zfill() adds leading zeros to integer/float

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
    
    click_count = 0
    
    while True:
        if mouse.getPressed()[0]:                                               # indexes 'left' mouse-click
            if not mouseDetected:                                               # initial mouse-click detection 
                loc = mouse.getPos()
                click_list.append(loc)
                img_list.append(img[trial])
                click_count = click_count + 1
                print(img[trial], click_count, loc)
                mouseDetected = True                                            # mouse press (depression) 
                for thisLoc in click_list:                                      # accuracy check: draw click-locations
                    waldoImage.draw()    
                    x.pos = thisLoc                                             # update 'x' position = click location 
                    x.draw()
                    win.flip() 
        else:
            mouseDetected = False                                               # mouse press (released) 
        if click_count >= 2:
            break #break out of while loop

#=====================
#SAVE DATA SETTINGS
#=====================
# print(click_list[0][0])                                                         #TEST: indexs list index=0, array value = x
# print(click_list[0][1])                                                         #TEST: indexs list index=0, array value = y
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
