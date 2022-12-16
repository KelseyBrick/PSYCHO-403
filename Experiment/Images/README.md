
These are all the images used in this experiment.

There are:
* Full-sized images (3000 x 1899 px)
* 10% cropped images (2700 x 1709 px)
* 25% cropped images (2250 x 1424.25 px)

Image cropping was completed using photoshop clipping masks set to condition crop dimensions (above).
* Photoshop horizontal and vertical guides were set to create a (0,0) centre point in the full-size image
* All clipping masks were centred on the (0,0) original centre point
* Original normalized units of Waldo's location were converted to Waldo's pixel location in cropped image relative to centre.
  *  This produced +/- values which indicate Waldo's location right/left or up/down of centre.   
  *  This holds Waldo's coordinate location within the new image constant.
* To accurately shift Waldo to his new location in the cropped image, horzontal and vertical guides were set to new location.
  *  x-values were added to 1500 (center point of x-axis of original image)
  *  y-values were reversed (i.e. switch +/-) and then added to 949.5 (center point of y-axis of original image)
  *  Waldo was then dragged to this new point and the image was saved.

[Calculations example](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Experiment/experimentData/waldoLocationsCalcs.csv)
