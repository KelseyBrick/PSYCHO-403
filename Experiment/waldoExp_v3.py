# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:27:01 2022

@author: kelse
"""



# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:17:52 2022

@author: kelse
"""

#figuring out how to define a mouse click location in an image object
#=====================
#IMPORT SETTINGS
#=====================

from psychopy import visual, event, core
import numpy as np
import os
import pandas as pd
import pprint

#=====================
#PATH SETTINGS
#=====================
main_dir = os.getcwd()                                                          
data_dir = os.path.join(main_dir,'experimentData')                              
image_dir = os.path.join(main_dir, 'images') 
if not os.path.exists(data_dir):                                                # raise Error: if the folder does not exist... 
   os.makedirs(data_dir)                                                        # create one                                

#=====================
#OPEN DATA SETTINGS
#=====================
filename = ('waldoLocations.csv')                                               # filename variable from identfyWaldo script
fullAddress = os.path.join(data_dir, filename)                                  # save full file path location as variable

df = pd.read_csv(fullAddress, engine = 'python')                                # use pandas to open the .csv as a dataframe
# print(df) #TEST
# print(df.dtypes) #TEST
#=====================
#IMAGES AND TRIAL SETTINGS
#=====================
nTrials = 6

img = np.array([])                                                              # create numpy array to collect image names from waldoLocations
img = np.append(img, df["Image_Name"])                                          # get image name from df and append to array
img = img.tolist()                                                              # convert array to list for easier indexing
# print(img) #TEST
waldoLoc_x = np.array([])                                                              # create numpy array to collect image names from waldoLocations
waldoLoc_x = np.append(waldoLoc_x, df["waldoLoc_x"])                                          # get image name from df and append to array
waldoLoc_x = waldoLoc_x.tolist() 
# print(waldoLoc_x) #TEST
waldoLoc_y = np.array([])                                                              # create numpy array to collect image names from waldoLocations
waldoLoc_y = np.append(waldoLoc_y, df["waldoLoc_y"])                                          # get image name from df and append to array
waldoLoc_y = waldoLoc_y.tolist() 
# print(waldoLoc_y) #TEST

trials = list(zip(img, waldoLoc_x, waldoLoc_y))                                       #zipped, ordered, tuple list of all posible trial conditions:
# print(df) #TEST ALIGNED
# pprint.pprint(trials) #TEST ALIGNED
trialNumbers = [0]*nTrials                                                      # blank list (6 values): trial number
click_list = []
click_times = []
trial_time = []
# click_list = np.array([])                                                       # participant guesses; use np.array, so (x,y) can be extracted
#=====================
#WINDOW AND MONITOR SETTINGS
#=====================
win = visual.Window(units='norm', fullscr=True)                                 # units normalized to scale image across various window sizes = fullscreen


                                                                                
#=====================
#STIMULUS SETTINGS
#=====================
waldoImage = visual.ImageStim(win, size= 2, interpolate=True)                    #define image variable; script only works with size=2 fills window.

mouse = event.Mouse()

x = visual.TextStim(win, text='x', color='black')
waldoFound = visual.TextStim(win, color='black', wrapWidth=2, alignText='center', pos=(-0.2,0), #defines text stimulus to a variable; to parameters: display in window and text to be used (Lines 90-93)
                        text="""
                        Way to go!
                        You found Waldo.\n
                        Press any key to continue to the next hunt!""")
waldoMiss = visual.TextStim(win, color='black', wrapWidth=2, alignText='center', pos=(-0.2,0), #defines text stimulus to a variable; to parameters: display in window and text to be used (Lines 90-93)
                        text="""
                        Oops!
                        That is not Waldo.\n
                        Try again!""")                        
waldoEscapes = visual.TextStim(win, color='black', wrapWidth=2, alignText='center', pos=(-0.2,0), #defines text stimulus to a variable; to parameters: display in window and text to be used (Lines 90-93)
                        text="""
                        So many tries and still no Waldo!
                        Sneaky guy got away this time.\n
                        On to the next hunt! Press any key.""")

clickLoc = visual.Circle(win, units='norm',                                     #circle positions will be updated to trial image's waldoLoc 
                          radius=(14/450,14/263), 
                          fillColor=None)
clickLocDummy = visual.Circle(win, units='norm', 
                              radius=(14/450,14/263), #(circle radius in px)/(position x or y in px) 
                              fillColor=None, 
                              lineColor='black') 

trial_timer = core.Clock()  

for itrial in range(nTrials):
    # overallTrial = nTrials+trial                                                #creates trial counter used to iterate through conditions list
    # blockNumbers[overallTrial] = iblock+1                                     #defines block number list using overallTrial counter as list index and iblock as list value
    # trialNumbers[overallTrial] = trial+1                                        #defines trial number list using overallTrial counter as list index and itrial as list value
    # colours[overallTrial] = trials[overallTrial][2] 
    trialNumbers[itrial] = itrial+1                                        #defines trial number list using overallTrial counter as list index and itrial as list value
    waldoImage.image = os.path.join(image_dir, img[itrial]) 
    waldoImage.draw()
    # clickLoc.draw()
    # clickLocDummy.draw()
    
    win.flip()
    
    trial_timer.reset()
    
    mouse.setPos(newPos=(0,0))
    click_count = 0
    mouseDetected = False
    found = False
    
    while True:
        if mouse.getPressed()[0]:
            if not mouseDetected:
                loc = mouse.getPos()
                click_list.append(loc)
                click_time = trial_timer.getTime()
                click_times.append(click_time)
                click_count = click_count + 1
                print('Trial:' + str(itrial+1), 'Click:' + str(click_count), 'Location:' + str(loc))
                mouseDetected = True #keep track of mouse presses so only first is use
                clickLoc.pos = (trials[itrial][1], trials[itrial][2])          #defines circle position from the randomized 'trial' tuples list: trial = list index; [0] = 1st tuple value (x-coordinate); [1] = 2nd tuple value (y-coordinate)
                clickLocDummy.pos = (trials[itrial][1], trials[itrial][2])     #defines circle position from the randomized 'trials' tuples list: overallTrial = list index; [0] = 1st tuple value (x-coordinate); [1] = 2nd tuple value (y-coordinate)          
                for thisLoc in click_list: #keep this list of click and draw all of them
                    waldoImage.draw()  
                    clickLoc.draw()
                    if mouse.isPressedIn(clickLoc):
                        found = True
                        clickLocDummy.lineColor = 'red'
                        clickLocDummy.draw()
                        waldoFound.draw()
                        win.flip()
                        event.waitKeys()
                        break
                    else: #adjusts number of available clicks
                        found = False    
                        x.pos = thisLoc
                        x.draw()
                        waldoMiss.draw()
                        win.flip()    
        else:
            mouseDetected = False
        if found == True:
            break
        elif click_count >= 2: #adjusts number of available clicks
            waldoImage.draw()    
            waldoEscapes.draw()
            win.flip()
            event.waitKeys()
            break #break out of while loop
    

win.close()

