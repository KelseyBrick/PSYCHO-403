### Wait exercises

```
        #=====================
        #START TRIAL
        #=====================   
        #-draw fixation
        fixCross.draw()                                                         #draw
        #-flip window
        win.flip()                                                              #show
        #-wait time (stimulus duration)
        core.wait(.75)                                                          #wait 0.75 seconds, then:
        
        #-draw image
        my_image.draw()                                                         #draw
        #-flip window
        win.flip()                                                              #show
        #-wait time (stimulus duration)
        core.wait(1)                                                            #wait 1 seconds, then:
        
#-draw end trial text
textStim.text = end_experiment_msg                                              #define the text
textStim.draw()                                                                 #draw end of experiment message
#-flip window
win.flip()                                                                      #show
#-wait time (stimulus duration)
core.wait(3.0)                                                                  #wait 3 seconds
```
See: [Wait code](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment_7/Level_5_Exercises_waitQ1.py)

### Clock exercises
**See precision comments below Q3**
1. Create a "wait_timer" to find out exactly how long core.wait(2) presents each image. Make sure this is not counting the time of the whole trial, but only the duration of each image. How precise is core.wait?

See: [ClockQ1](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment_7/Level_5_Exercises_clockQ1.py)

2. Create a "clock_wait_timer" to find out exactly how long each image is presented when you use a clock + while loops. How precise is this?

See: [ClockQ2](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment_7/Level_5_Exercises_clockQ2.py)

3. Create a "countdown_timer" to find out exactly how long each image is presented when you use a CountdownTimer + while loops. How precise is this?

See: [ClockQ3](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment_7/Level_5_Exercises_clockQ3.py)

Summary of time differences between Clocks Q1-Q3:

![image](https://user-images.githubusercontent.com/113373038/203163460-9180d17f-5212-4bf3-aa84-0e1e9b0dc6cf.png)

The differences between these three methods was nominal on my computer (Decending outputs: Q1, Q2, Q3).

4. Edit your main experiment script so that the trials loop according to a clock timer. Also create and implement a block_timer and a trial_timer.

See: [Code V1](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment_7/Level_5_Exercises_V1.py)

Of interest: lines 207 forward.

### Frame-based timing exercises
1. Adjust your experiment so that it follows frame-based timing rather than clock timing (comment out the clock-based timing code in case you want to use it again) using for loops and if statements.
2. Add a "dropped frame" detector to your script to find out whether your experiment is dropping frames. How many total frames are dropped in the experiment? If 20 or fewer frames are dropped in the whole experiment (1 frame per trial), keep frame-based timing in your experiment. Otherwise, switch back to the CountdownTimer.

Q1 & Q2: [Code V2](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment_7/Level_5_Exercises_V2.py)

Of interest: Q1 (lines 198 forward); Q2 (lines 212-220; 291)

Dropped frame check in console:

![image](https://user-images.githubusercontent.com/113373038/203185662-32b1b40b-519b-4954-9987-45e05ff2be4a.png)

**NOTE: not sure why I have so many drop frames. I still need to experiment with this a bit, but my guess is that I have a mix of clocks and frame-based timing. I need to integrate frame-based timing into meta and block level experiment timing. But overall an interesting output.
