### Eighteen images in the experiment:
[Waldo Images](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/tree/main/Experiment/Images)

[Original images links](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Experiment/Images/imageCitation.md)


### This is set to identify Waldo's locations:
[Identify Waldo script](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Experiment/identifyWaldo.py)

This script was created as an experiment helper. This experiment will only work with identifying a click location of a target. 
* Allows the experimenter to set a list of target coordinates that are then imported into the actual experiment.
* Script is designed to mark the target and pause to ensure the location choice is accurate.
* A click count could be added if an average or range of click locations was desired. 
* Any images containing a target could be used in place of Waldo photos.

Waldo Answers used: 
* [Waldo01](https://www.deviantart.com/where-is-waldo-wally/art/Where-s-Waldo-Book-1-Scene-2-789863105)
* [Waldo02](https://www.deviantart.com/where-is-waldo-wally/art/Where-s-Waldo-Book-1-Scene-3-789863397)
* [Waldo03](https://www.deviantart.com/where-is-waldo-wally/art/Where-s-Waldo-Book-1-Scene-7-789864742)
* [Waldo04](https://www.deviantart.com/where-is-waldo-wally/art/Where-s-Waldo-In-Hollywood-Book-4-Scene-11-462458877)
* [Waldo05](https://www.deviantart.com/where-is-waldo-wally/art/Where-s-Waldo-Now-Book-2-Scene-12-462401664)
* [Waldo06](https://www.deviantart.com/where-is-waldo-wally/art/Where-s-Waldo-The-Wonder-Book-Book-5-S2-464390635)

### To try this experiment and skip the first script with this file:
[WaldoAnswers CSV](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Experiment/experimentData/waldoLocations.csv)

### This is the Waldo's experiment:
[Waldo experiment script](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Experiment/waldoExp.py)

### *Question: Does visual noise affect participant search time and accuracy?*
* Visual noise is defined by the number of contents contained within the image. One hundred percent would be a full-size image. Reductions in visual noise will crop the original image, thus limiting content that needs to be searched.

Design: between-subject; currently, this experiment is set to three conditions:
  * Full-sized images (3000 x 1899 px)
  * 10% cropped images (2700 x 1709 px)
  * 25% cropped images (2250 x 1424.25 px)

The script will run the desired image size based on the condition number set by the GUI collecting subject information.
* Participants will view 6 Waldo images.
* They are instructed to click where they have found Waldo.
* If the guess is correct, they move on to the following image.
 * Waldo's location is set by a clickLoc using coordinates defined in the identifyWaldo.py script and a CircleStim whose radius sets the accuracy tolerance.
* If the guess is wrong, the participant can try again, up to three tries, before moving on to the following image.
 * not coded, but possible to add a time limit instead of click count as the criterion to move on.

This experiment collects and saves the following info:
* "Trial_Number", "Image_Name", "Click_Count", "Time_to_Click", "Click_Coordinates", and "Find_Accuracy"

[Example output](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Experiment/experimentData/2_1_outputFile.csv)
* Filenames are coded by condition number first, so they auto-sort while saving.

One issue with this script is that visual noise is currently confounded with a zooming effect when the image is displayed. Because each image is cropped and then normalized to a fullscreen mode, smaller images zoom in. That is, not only is there less content to search in the image, the size of the content becomes bigger because a smaller image has more room to expand into a full-sized screen. As a result, the change in search speed could be due to less or easier-to-see content.

A possible solution is not to display images in fullscreen mode or normalize units. However, this allows the images to be viewed on anyone's screen. Another possible solution would be to create a method to hold zoom constant. This is currently out of this project's scope, but I wanted to acknowledge the experimental confound.





