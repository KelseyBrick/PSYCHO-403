# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:27:01 2022

@author: kelse
"""
#=====================
#IMPORT SETTINGS
#=====================

from psychopy import visual, event, core, gui
import numpy as np
import os, sys
import pandas as pd
from datetime import datetime

#=====================
#PATH SETTINGS
#=====================
mainDir = os.getcwd()                                                          
dataDir = os.path.join(mainDir,'experimentData')                              
imageDir = os.path.join(mainDir, 'images') 
if not os.path.exists(dataDir):                                                 # raise Error: if the folder does not exist... 
    os.makedirs(dataDir)                                                        # create one                                

#=====================
#OPEN DATA SETTINGS
#=====================
locationsFile = ('waldoLocations.csv')                                          # filename variable from identfyWaldo script
fullAddress = os.path.join(dataDir, locationsFile)                              # save full file path location as variable

df = pd.read_csv(fullAddress, engine = 'python')                                # use pandas to open the .csv as a dataframe

#=====================
#COLLECT INFO
#=====================
today = datetime.today()                                                        # date/time variable

gui = gui.Dlg(title="Find Waldo Experiment")

gui.addField("Subject ID:")                                                     # fields of collected per subject info
gui.addField("Cond. num.:", choices=["1", "2", "3"])
gui.addFixedField("Date:", today)
gui.addField("Name:")
gui.addField('Age:')

ok_data = gui.show()                                                            # show dialog and wait for OK or Cancel
if gui.OK:                                                                      # or if ok_data is not None
    print(ok_data)
else:
    print('user cancelled')

subjID = gui.data[0]
condNum = gui.data[1]
date = gui.data[2]                                              

filename = (str(condNum) + '_' + str(subjID) + '_outputFile.csv')               # filename variable that creates unique filename 

#=====================
#IMAGES AND TRIAL SETTINGS
#=====================
#///WALDO IMAGES AND LOCATIONS\\\#
img = np.array([])                                                              # create numpy array to collect image names from waldoLocations
img = np.append(img, df["Image_Name"])                                          # get image name from df and append to array
img = img.tolist()                                                              # convert array to list for easier indexing

waldoLoc_x = np.array([])                                                       # create numpy array to collect image names from waldoLocations
waldoLoc_x = np.append(waldoLoc_x, df["waldoLoc_x"])                            # get x-coordinates from df and append to array
waldoLoc_x = waldoLoc_x.tolist() 

waldoLoc_y = np.array([])                                                       # create numpy array to collect image names from waldoLocations
waldoLoc_y = np.append(waldoLoc_y, df["waldoLoc_y"])                            # get y-coordinates from df and append to array
waldoLoc_y = waldoLoc_y.tolist() 

#///TRIALS AND CONDITIONS\\\#
nTrials = 6

trials = list(zip(img, waldoLoc_x, waldoLoc_y))                                 # zipped, ordered, tuple list of all posible trial conditions
    
if condNum == "1":
    trials = trials[:6]
    np.random.shuffle(trials)
elif condNum == "2":
    trials = trials[6:12]
    np.random.shuffle(trials)
elif condNum == "3":
    trials = trials[12:18]
    np.random.shuffle(trials)
else:
    sys.exit("Unknown condition number")                                        # exit experiment in participant info cannot be found

#///DATA COLLECTION LISTS\\\#
trialNumbers = []
clickNum = []                                                    
clickTimes = []
allClickLocs = []
accuracy = []
trialNumber = [] 
imgName = []

#=====================
#WINDOW AND MONITOR SETTINGS
#=====================
win = visual.Window(units='norm', fullscr=True)                                 # units normalized to scale image across various window sizes = fullscreen
                                                                         
#=====================
#STIMULUS SETTINGS
#=====================
#///TIME AND KEYPRESSES\\\#
clickTimer = core.Clock()
mouse = event.Mouse()

#///GRAPHICS\\\#
waldoExemplar = visual.ImageStim(win, pos=(-.50, 0),
                            image= os.path.join(imageDir, 'wheres-waldo.png'))
waldoImage = visual.ImageStim(win, size= 2, interpolate=True)                   # define image variable; script only works with size=2 fills window.
x = visual.TextStim(win, text='x', color='black')
clickLoc = visual.Circle(win, units='norm',                                     # circle positions will be updated to trial image's waldoLoc 
                          radius=(16/450,16/263), 
                          fillColor=None)
clickLocDummy = visual.Circle(win, units='norm', lineWidth=2,
                              radius=(14/450,14/263),                           # normalized units: (circle radius in px)/(position x or y in px) 
                              fillColor=None) 

#///TEXT\\\#
instructions = visual.TextBox2(win, color='black', letterHeight=0.06, 
                               alignment='center', size=[1, 1.85], 
                               fillColor='#8DDBD7', borderColor='black',     
text="""Hello! \n
You are about to see a series of images that contain a hidden person named Waldo.
You can see what he looks like on the left of this screen. \n
Your task is to FIND WALDO. \n
If you think you have spotted him, CLICK ON THE SCREEN.
If you are correct, you will move on.
If it was not Waldo, you can try again. 
But...you will only get three guesses. \n
Be QUICK, but ACCURATE. \n
Good luck. Press any key to begin."""
                                )                                               # keep text aligned like or misaligns in textbox    

goodbye = visual.TextBox2(win, color='black', letterHeight=0.07,  
                               alignment='center', size=[.85, 1], 
                               fillColor='#8DDBD7', borderColor='black',     
text="""Nice work during your searches to find Waldo! \n
Thanks for your participation. \n
Good Bye! \n
Press any key to exit the experiment."""
                                )  

waldoFound = visual.TextBox2(win, color='black', opacity=(.85), 
                             alignment='center', size=[.65, .35], 
                             fillColor='#92DB8D', borderColor='black',
                             letterHeight=0.06,
text="""Way to go!
You found Waldo.
On to the next hunt!"""
                                )

waldoMiss = visual.TextBox2(win, color='black', opacity=(.85), 
                            alignment='center', size=[.65, .35],
                            fillColor='#8DC5DB', borderColor='black',
                            letterHeight=0.06,
text="""Oops! 
That's not Waldo.
Try again!"""
                                )  
                      
waldoEscapes = visual.TextBox2(win, color='black', opacity=(.85), 
                               alignment='center', size=[.65, .35], 
                               fillColor='#DB8D8D', borderColor='black',
                               letterHeight=0.06,
text="""Good try, but you did not find Waldo! 
Sneaky guy got away this time.
On to the next hunt!"""
                                )                                               

#=====================
#TRIALS SETTINGS
#===================== 
instructions.pos = (0.3, 0)
instructions.draw()
waldoExemplar.draw()
win.flip()
event.waitKeys()

for itrial in range(nTrials):
    trial = itrial + 1
    
    waldoImage.image = os.path.join(imageDir, trials[itrial][0])                # defines image from 'trials' tuples          
    waldoImage.draw()
    win.flip()
    
    #\\\RESESTS///#
    clickTimer.reset()
    mouse.setPos(newPos=(0,0))
    clickCount = 0
    clickIndex = -1
    clickList = []                                                              # reset trial clicks
    mouseDetected = False                                                       # tracker for mouse-click depression/release 
    found = False
    
    while True:
        
        if mouse.getPressed()[0]:
            
            if not mouseDetected:
                mouseDetected = True                                            # tracks first mouse-click only
                
                loc = mouse.getPos()                                            # click location coordinates
                clickList.append(loc)
                clickIndex = clickIndex + 1                                     # indexes click location in clickList
                
                clickTime = clickTimer.getTime()                                # click times
                clickTimes.append(clickTime) 
                
                clickCount = clickCount + 1                                     # counts click frequency within a trial
                clickNum.append(clickCount)

                print('Trial:' + str(itrial+1), 'Click:' + str(clickCount), 
                      'Location:' + str(loc))

                clickLoc.pos = (trials[itrial][1], trials[itrial][2])           # defines circle position from 'trials' tuples 
                clickLocDummy.pos = (trials[itrial][1], trials[itrial][2])      # defines circle position from 'trials' tuples          
                
                waldoImage.draw()  
                clickLoc.draw()
                
                if mouse.isPressedIn(clickLoc):                                 # Waldo Found (hit)
                    found = True
                    trueClick = 1
                    accuracy.append(trueClick)
                    clickLocDummy.lineColor = 'green'
                    
                    clickLocDummy.draw()                                        # circle Waldo
                    waldoFound.draw()
                    win.flip()

                    core.wait(2.25)
                    break                                                       # break out of while loop
                    
                elif not mouse.isPressedIn(clickLoc):                           # Not Waldo (miss)
                    found = False
                    x.pos = clickList[clickIndex]
                    missClick = 0
                    accuracy.append(missClick)
                    
                    x.draw()                                                    # 'x' at wrong click location and 'Miss' text
                    waldoMiss.draw()
                    win.flip()
                    
                    core.wait(.8)
                    clickTimer.reset()                                          # reset click timer
                    
                    waldoImage.draw()                                           # clear the 'x' and 'Miss' text
                    win.flip()
                    
                    if clickCount >= 3:                                         # adjusts permitted clicks per trial
                        waldoImage.draw()    
                        waldoEscapes.draw()
                        win.flip()
                        core.wait(2.25)
                        break                                                   # break out of while loop
        else: 
            mouseDetected = False                                               # mouse button not pressed

    for thisIndex in range(len(clickList)):                                     # adds click locations by trial to master list (sub-list cleared each trial)
        allClickLocs.append(clickList[thisIndex])
        trialNumbers.append(trial) 
        imgName.append(trials[itrial][0])

#=====================
#SAVE DATA SETTINGS
#=====================

df = pd.DataFrame(data={                                                        #use pandas module to save a dataframe of collected trial data 
  "Trial_Number": trialNumbers,                                                  
  "Image_Name": imgName,
  "Click_Count": clickNum, 
  "Time_to_Click": clickTimes, 
  "Click_Coordinates": allClickLocs,
  "Find_Accuracy": accuracy

})
df.to_csv(os.path.join(dataDir, filename), sep=',', index=False)                # save the dataframe as .csv file using parameters

#=====================
#END EXPERIMENT SESSION
#=====================
goodbye.pos = (0.3, 0)    
goodbye.draw()
waldoExemplar.draw()
win.flip()
event.waitKeys()

win.close()

