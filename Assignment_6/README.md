
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

e) Edit the psuedo code in the experiment document (see lines 44-68, **here**)
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
date = datetime.now() #what time is it right now?
exp_info['date'] = str(date.day) + str(date.month) + str(date.year)             #adds 'date' key into the dictionary
print(exp_info['date'])

#-create a unique filename for the data
filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
print(filename)

#create a subject info directory to save subject info
sub_dir = os.path.join(main_dir,'experiments','subject_dir',filename) 
```

### Window and monitor exercises
1. How does changing "units" affect how you define your window size?

Every monitor must be defined because their units (ex., width, viewing distance, and pixel resolution) affect how the default window is displayed.
* the default window display is 800x600 pixels, centred, and white
```
win = visual.Window(monitor=mon)                            #default
```
![image](https://user-images.githubusercontent.com/113373038/201561613-ea2a3897-0eae-4e08-a434-938b28347576.png)

* changing the pixel ratio in the 'size' parameter will change the window display size. 
```
win = visual.Window(monitor=mon, 
                    size=(1600,900))                       #adjusted units
```
![image](https://user-images.githubusercontent.com/113373038/201561454-2c3ef104-cfbd-4134-a2cb-057c3ac0c7d5.png)

2. How does changing colorSpace affect how you define the color of your window? 

Different colourspaces use different methods to define colours. See below.

Colours can be defined by (source: https://www.psychopy.org/general/colours.html):
* RGB: psychopy defaults to tri-values between -1 to 1 to indicate saturation of red, green, and blues. It can be told to use rgb255.
* DKL: Requires the monitor to be calibrated and uses 3D spherical space to define colours. Psychopy also uses tri-values between 1 to -1 in defining the degrees of elevation, azimuth, and a float.
* LMS: Requires the monitor to be calibrated and permits colour definition for independent cones.
* HEX: hexidecimal number that can be found in an online chart (ex., #B8860B); https://htmlcolorcodes.com/color-picker/
* HSV: uses a tri-value hue, saturation, and 'value' to define a colour.
* Or by name: uses web/X11 colour names (ex., DarkGoldenRod); not case sensitive, but no spaces used.           

Can you define colors by name? 

**Yes**, see above.

3. Fill in the following pseudocode with the real code you have learned so far:
