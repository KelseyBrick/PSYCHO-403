### Experiment structure exercises

see [Level_3_Exercises_v2.py](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment_5/Level_3_Exercises_v2.py).

**Note**: this code may change based on subsequent exercises used to complete this experiment's code.
- Lines 54-66: these include possible properities required in this experiment. Some may be added, deleted, or modified based on final code.
- Lines 123, 125, 127: no for loops or .append() methods have been added. This code will be required in future to direct the program to add certain information to the lists.
- Line 157: has alternate code option
- Line 164: the *for loop* has not been expanded past the initial execution. Additionally, if the randomized conditions list from line 156 is used the variables in this loop may need to be chnaged (i.e., looping through the counterbalanced conditions list vs. nTrials.

### Import exercises

```
#=====================
#IMPORT MODULES
#=====================
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os, random, pprint
```
**Note**: more moldules may require importing in future edits of this program's code.

### Directory exercises

```
#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()                                                          # C:\Users\kelse\Google Drive\00 University of Alberta\2022- Fall\PSYCH 403
#-define the directory where you will save your data
data_dir = os.path.join(main_dir, 'experiments','exercise_data')                # C:\Users\kelse\Google Drive\00 University of Alberta\2022- Fall\PSYCH 403\experiments\exercise_data
#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'experiments','exercise_stimulus')            # C:\Users\kelse\Google Drive\00 University of Alberta\2022- Fall\PSYCH 403\experiments\exercise_stimulus
#-check that these directories exist >>> SEE BELOW (Lines 57-63)
```

Check matching of list and directory contents (Lines 57-63):
```
# check if images exist in the directory
path = image_dir 
fileList = os.listdir(path)
missing = [name for name in img if name not in fileList]                        # identifies which image is missing if the fileList and img[] don't match
if missing == []:                                                               # if missing returns None value == True and fileList and img[] MATCH
    print('The lists match')
else:                                                                           # if missing returns ANY value then the fileList and img[] DON'T MATCH
    print('This image is missing: ' + str(missing) + '. The image lists do not match up!')
```
Output test: 
<br> MATCHING: 
<br> The lists match
<br> DIFFERENT: 
<br> This image is missing: ['face01.jpg']. The image lists do not match up!
