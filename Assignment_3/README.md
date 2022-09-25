### Variable operation exercises
1. Create three variables: "sub_code", "subnr_int", and "subnr_str". The sub_code should be "sub". Assign the integer 2 to subnr_int, and assign the string "2" to subnr_str. Which form of subnr (int or str) can be added to sub_code to create the output "sub2"? Why don't both work?

2. Use operations to create the following outputs with your variables:
"sub 2"
"sub 222"
"sub2sub2sub2"
"subsubsub222"

### List operations exercises
1. Create a list of numbers [1,2,3] called "numlist". Multiply the list by 
2. Create a numpy array of numbers [1,2,3] called "numarr". Multiply the array by 2. What is the difference between multiplying lists and multiplying arrays?
3. Create a list of strings ['do','re','mi','fa'] called "strlist". Use operations to create the following outputs with your variable:
['dodo','rere','mimi','fafa']
['do','re','mi','fa','do','re','mi','fa']
['do','do','re','re','mi','mi','fa','fa']
[['do','do'],['re','re'],['mi','mi'],['fa','fa']]

### Zipping exercises
You are designing a memory experiment in which 1 face and 1 house are presented on each trial, one after the other, followed by a post-cue that tells the participant which of the two images to remember. You want to present all combinations of stimuli an equal number of times, with a random trial order for each participant. The order of image presentations (face first or house first) should also be counterbalanced ahead of time.

Specifically, you have:

2 categories of images (faces, houses)
5 images from each category
2 post-cues (1,2)
Create a script that outputs a counterbalanced list with every face paired with every house, repeated with each possible post-cue. Then, randomize the order of the list. The final output should look something like this:

[(face1.png, house2.png, cue1),
(house5.png, face1.png, cue2)...]

### Indexing Exercises
1. Create a list of strings called "colors", containing the following colors in this order: red, orange, yellow, green, blue, purple
2. Using indexing, print the penultimate color.
3. Using indexing, print the 3rd and 4th characters of the penultimate color.
4. Using indexing, remove the color "purple" and add "indigo" and "violet" to the list instead.

### Slicing exercises
1. Create a list of numbers 0-100 called "list100".
2. Using slicing, print the first 10 numbers in the list.
3. Using slicing, print all the odd numbers in the list backwards.
4. Using slicing, print the last four numbers in the list backwards.
5. Are the 40th-44th numbers in the list equal to integers 39-43? Show the Boolean operation you would use to determine the truth value.
