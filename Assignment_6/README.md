
### Dialog box exercises

1. Edit dictionary "exp_info" to include a session variable set to 1.
```
exp_info = {'subject_nr':0, 
            'age':0, 
            'handedness':('right','left','ambi'), 
            'gender':('male','female','other','prefer not to say'),
            'session': 1}
```
2. Add a blank space for participants to type gender
```
exp_info = {'subject_nr':0, 
            'age':0, 
            'handedness':('right','left','ambi'), 
            'gender':'',                                    #2. set to blank
            'session': 1}
```
3. Using DlgFromDict:

a) Customize my_dlg so that you have a title for your dialog box: "subject info"
```
my_dlg = gui.DlgFromDict(dictionary=exp_info,
                         title="subject info")
```
b) Set the variable "session" as fixed. What happens?
```

my_dlg = gui.DlgFromDict(dictionary=exp_info, 
                         title="Subject info",
                         fixed=['session'])
```
When the parameter 'session' is set to 'fixed' it cannot be edited by whomever is entering information into the subject info box.

c) Set the order of the variables as session, subject_nr, age, gender, handedness.
```
my_dlg = gui.DlgFromDict(dictionary=exp_info, 
                         title="Subject info",
                         fixed=['session'],
                         order=['session', 'subject_nr', 'age', 'gender', 'handedness'])
```
d) Don't show "my_dlg" right away. Tell your experiment to print "All variables have been created! Now ready to show the dialog box!". Then, show the dialog box.
```
exp_info = {'subject_nr':0, 
            'age':0, 
            'handedness':('right','left','ambi'), 
            'gender':'',                                    #2. set to blank
            'session': 1}

print("All variables have been created! Now ready to show the dialog box!")

my_dlg = gui.DlgFromDict(dictionary=exp_info, 
                         title="Subject info",
                         fixed=['session'],
                         order=['session', 'subject_nr', 'age', 'gender', 'handedness'])
```
A print() funtion has been added between the dictionary and the dialog box code.

e) Edit the psuedo code in the experiment document (see [Level_4_Exercises_v3.py](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment_6/Level_4_Exercises_v3.py): lines 38-58)
```
#-create a dialogue box that will collect current participant number, age, gender, handedness
exp_info = {'subject_nr':0, 
            'age':0, 
            'handedness':('right','left','ambi'), 
            'gender':'',                                                        #2. set to blank
            'session': 1}

print("All variables have been created! Now ready to show the dialog box!")

my_dlg = gui.DlgFromDict(dictionary=exp_info, 
                         title="Subject info",
                         fixed=['session'],
                         order=['session', 'subject_nr', 'age', 'gender', 'handedness'])

#get date and time
date = datetime.now()                                                           #what time is it right now?
exp_info['date'] = str(date.day) + str(date.month) + str(date.year)             #adds 'date' key into the dictionary
print(exp_info['date'])

#-create a unique filename for the data
filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
print(filename)
```

### Window and monitor exercises
1. How does changing "units" affect how you define your window size?

References: https://psychopy.org/general/units.html#units and https://psychopy.org/api/visual/window.html#psychopy.visual.Window

The 'units' parameter determines how stimuli is drawn in the window based on monitor settings provided. Psychopy uses these settings to calculate an appropriate pixel size of the stimulus. It has the following values that can be defined:
* None: default; stimulus presentation ONLY based on monitor settings provided.
* ‘height’ (of the window): scales stimuli relative to participant screen; no monitor info required.
* ‘norm’ (normalised): maintains aspect ratio of the screen; no monitor info required. 
* ‘deg’: sets stimuli based on degrees of the visual angle;  requires screen width, veiwing distance and pixel info.
* ‘cm’: sets stimuli size and location in centimeters; requires screen width and pixel info.
* ‘pix’: sets stimuli based on pixels; requires screen pixel info.

2. How does changing colorSpace affect how you define the color of your window? 

Different colourspaces use different methods to define colours. See below.

Colours can be defined by (reference: https://www.psychopy.org/general/colours.html):
* RGB: psychopy defaults to tri-values between -1 to 1 to indicate saturation of red, green, and blues. It can be told to use rgb255.
* DKL: Requires the monitor to be calibrated and uses 3D spherical space to define colours. Psychopy also uses tri-values between 1 to -1 in defining the degrees of elevation, azimuth, and a float.
* LMS: Requires the monitor to be calibrated and permits colour definition for independent cones.
* HEX: hexidecimal number that can be found in an online chart (ex., #B8860B); https://htmlcolorcodes.com/color-picker/
* HSV: uses a tri-value hue, saturation, and 'value' to define a colour.
* Or by name: uses web/X11 colour names (ex., DarkGoldenRod); not case sensitive, but no spaces used.           

Can you define colors by name? 

**Yes**, see above.

3. Fill in the following pseudocode with the real code you have learned so far. ((see [Level_4_Exercises_v3.py](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment_6/Level_4_Exercises_v3.py): see lines 167-179)
```
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', 
                       width=48.93, 
                       distance=75)                                             #defines name, width, and viewing distance from monitor
mon.setSizePix([1920,1080])                                                     #defines the pixel resolution with (x,y) coordinates

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon)
win = visual.Window(monitor=mon, 
                    size=(1600,900),
                    color=('#ad17a3'),
                    units='height',
                    fullscr=None                                                #can be set to 'fullscr=True'; not done to prevent getting stuck in fullscr. 
                    )
```
Example of silly window colour used in the code above:
![image](https://user-images.githubusercontent.com/113373038/201568503-75515738-7447-4453-ab4e-09c9c7484523.png)

### Stimulus exercises

References: psychopy.org/api/visual/imagestim.html; https://psychopy.org/api/visual/textstim.html

1. Write a short script that shows different face images from the image directory at 400x400 pixels in size. What does this do to the images? How can you keep the proper image dimensions and still change the size?

See script here: [Level_4_Exercises_stimQ1](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment_6/Level_4_Exercises_stimQ1.py)

Changing these settings squished the image. This required units to be set to pixels and the size specified.
* To keep dimensions and change inmage size, use a scalar value in the size property of visual.ImageStim class.
```
my_image = visual.ImageStim(win)                                               #default
my_image = visual.ImageStim(win, units='pix', size=(400,400))                  #create the stimulus 400x400 pixels
my_image = visual.ImageStim(win, size=0.5)                                     #scalar- change image size, but keep dimensions
```

Default, without 400x400: 
![image](https://user-images.githubusercontent.com/113373038/201770769-7523bb97-c82c-4013-ae20-da0deaff0f5b.png)

With 400x400 settings:
![image](https://user-images.githubusercontent.com/113373038/201770965-725a1cac-3397-4042-a546-850d86c6891b.png)

With scalar value of 50%:
![image](https://user-images.githubusercontent.com/113373038/201776515-3ceae306-0c26-4dbd-8e4e-b727e70bee85.png)

2. Write a short script that makes one image appear at a time, each in a different quadrant of your screen (put the window in fullscreen mode). Think about how you can calculate window locations without using a trial-and-error method.

See script here: [Level_4_Exercises_stimQ2](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment_6/Level_4_Exercises_stimQ2.py)

3. Create a fixation cross stimulus (hint:text stimulus).

See script here: [Level_4_Exercises_stimQ3](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment_6/Level_4_Exercises_stimQ3.py)

4. Fill in the following pseudocode with the real code you have learned so far: (see [Level_4_Exercises_v3.py](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment_6/Level_4_Exercises_v3.py)

Code example:
```
#-define experiment start text unsing psychopy functions
start_msg = "Welcome to my experiment! Press any key to begin."
#-define block (start)/end text using psychopy functions

block_msg = "Press any key to continue to the first trial."
    
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
        
        #-draw image
        my_image.draw()                                                         #draw
        #-flip window
        win.flip()                                                              #show
        #-wait time (stimulus duration)
        event.waitKeys()                                                        #wait for keypress
        
#-draw end trial text
textStim.text = end_experiment_msg                                              #define the text
textStim.draw()                                                                 #draw end of experiment message
#-flip window
win.flip()                                                                      #show
#-wait time (stimulus duration)
event.waitKeys()                                                                #wait for keypress
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial

#======================
# END OF EXPERIMENT
#======================        
#-write data to a file

#-close window
win.close()                                                                 #close the window after all trials have looped                                    
#-quit experiment
```
