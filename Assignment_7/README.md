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
See: DOCUMENT lines xxx-xxx for full functionality within the experiment

### Clock exercises
1. Create a "wait_timer" to find out exactly how long core.wait(2) presents each image. Make sure this is not counting the time of the whole trial, but only the duration of each image. How precise is core.wait?
See: FILE XXX

On test, using the core.wait function, the outputs were:
![image](https://user-images.githubusercontent.com/113373038/203156124-68434afe-442d-4b65-903c-8a31d82a408c.png)
These numbers are relatively precise.

2. Create a "clock_wait_timer" to find out exactly how long each image is presented when you use a clock + while loops. How precise is this?
See: FILE XXX

On test, using clock + while loops, the outputs were:

4. Create a "countdown_timer" to find out exactly how long each image is presented when you use a CountdownTimer + while loops. How precise is this?
See: FILE XXX

On test, using CountdownTimer + while loops, the outputs were:

6. Edit your main experiment script so that the trials loop according to a clock timer. Also create and implement a block_timer and a trial_timer.

### Frame-based timing exercises
1. Adjust your experiment so that it follows frame-based timing rather than clock timing (comment out the clock-based timing code in case you want to use it again) using for loops and if statements.
2. Add a "dropped frame" detector to your script to find out whether your experiment is dropping frames. How many total frames are dropped in the experiment? If 20 or fewer frames are dropped in the whole experiment (1 frame per trial), keep frame-based timing in your experiment. Otherwise, switch back to the CountdownTimer.
