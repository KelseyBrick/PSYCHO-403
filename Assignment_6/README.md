
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
            'gender':'',                #2. set to blank
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
            'gender':'',                #2. set to blank
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
            'gender':'',                #2. set to blank
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
