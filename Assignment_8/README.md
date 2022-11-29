### PsychoPy keypress exercises
1. event.getKeys is prone to collect as many responses as you can make in a trial, but often times you only want to collect one response for a trial. 
* Soultion so a single response is recorded from event.getKeys

```
from psychopy import core, gui, visual, event, monitors                         # core for this lesson
# from psychopy import core, gui, visual, event, monitors
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor',
                       width=48.93,
                       distance=75)                                            #defines name, width, and viewing distance from monitor
mon.setSizePix([1920,1080])                                                    #defines the pixel resolution with (x,y) coordinates
win = visual.Window(monitor=mon)                                               #define a window


nTrials=3
my_text=visual.TextStim(win)
fix=visual.TextStim(win, text='+')

for trial in range(nTrials):
    
    keys = event.getKeys(keyList=['1','2'])                                     #define getkeys
    my_text.text = ("Trial " + str(trial) + "...Press keys 1 or 2")                
    
    fix.draw()
    win.flip()
    core.wait(2)
    
    event.clearEvents()                                                         #clear any keys presses just prior to collecting responses
    
    my_text.draw()
    win.flip()
    core.wait(1)
    
    print("The keys pressed were ", keys)                                       #which key did the subject were press?
    
    if keys:
        sub_resp = keys[0]                                                      #if more than one key pressed only take the first response
        print("Only this key press counted: ", sub_resp)    
    
win.close()
```
Indexing used to set the only recorded response to the first one in the collect .getKeys list.

2. Statement placement in your script is very important when collecting responses and refreshing keypresses. What happens if you put event.ClearEvents within the trial loop instead of outside the trial loop? What happens if you unindent the "if keys:" line?

<img width="953" alt="image" src="https://user-images.githubusercontent.com/113373038/204427460-bfebb073-5fd4-4e50-ae1e-b9012f0854a8.png">

Putting the .clearEvents() outside of the loop seems to be preventing response collection in my first trial, but collects inn the subsequent trials.

<img width="941" alt="image" src="https://user-images.githubusercontent.com/113373038/204428399-fbb82586-e7e5-4f27-81a7-095745c2061d.png">

Unindenting the "if keys" only collects the sub_resp from the last trial, instead of after each trial.

### Recording data exercises
1. Instead of collecting key name, subject RT, subject accuracy, and correct responses in lists, create a dictionary containing those variables. Then, during response collection, append the data to the dictionary instead of filling lists.
2. Keep in mind that you can pre-define dictionaries or lists for the whole experiment (in which case you have to use [block][trial] indexing to collect responses) or you can do it block-by-block (in which case you can use [trial] indexing). Create your lists (or dictionary, if you prefer) within the block loop and switch to [trial] indexing.

### Save csv exercises
1. Using csv.DictWriter (use your favorite search engine to find the help page), save your dictionary (that you created above) as a .csv file.
BACK TO TABLE OF CONTENTS

### Save JSON exercises
1. Add JSON filesaving to your experiment script.

### Read JSON exercises
1. Create a short "read and analysis" script that loads a saved JSON file, performs rudimentary analyses on the data, and prints the means.
2. Change your "read and analysis" script so that RTs for inaccurate responses are removed from analysis.
3. Change your "read and analysis" script so that any trials without a response (0 value) are removed from analysis.
