### Variable operation exercises
1. The fuction print(sub_code + subnr_str) creates the output "sub2."
Print(sub_code + subnr_int) does not work because you cannot concatenate an integer to a string.
```
print(sub_code + subnr_int)
print(sub_code + subnr_str)
```
  TypeError: can only concatenate str (not "int") to str <br>
  sub2

2. See the following code outputs:
```
print(sub_code + "" + subnr_str)
print(sub_code + " " + subnr_str + subnr_str + subnr_str)
print((sub_code + subnr_str)*3)
print(sub_code + sub_code + sub_code + subnr_str + subnr_str + subnr_str)
```
  sub 2 <br>
  sub 222 <br>
  sub2sub2sub2 <br>
  subsubsub222 

### List operations exercises
1. See code:
```
numlist = [1, 2, 3]*2
print(numlist)
```
[1, 2, 3, 1, 2, 3]

2. See code:
```
import numpy as np
numarr = np.array([1, 2, 3])*2
print(numarr)
```
[2 4 6]

Multiplying a list by 2 duplicates the list by 2, whereas multiplying the array by 2 multiplies each value in the array by 2. 2, in this example, could be substituted for any value x. For example:
```
numlist2 = [1, 2, 3]*4
print(numlist2)
```
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

3. See code:
```
strlist = ['do','re','mi','fa']
print([strlist[0]*2, strlist[1]*2, strlist[2]*2, strlist[3]*2])
```
['dodo', 'rere', 'mimi', 'fafa']
```
print(strlist *2)
```
['do', 're', 'mi', 'fa', 'do', 're', 'mi', 'fa']
```
print([ strlist[0], strlist[0], 
        strlist[1], strlist[1], 
        strlist[2], strlist[2], 
        strlist[3], strlist[3]
      ])
```
['do', 'do', 're', 're', 'mi', 'mi', 'fa', 'fa']
```
print([ [strlist[0], strlist[0]], 
        [strlist[1], strlist[1]], 
        [strlist[2], strlist[2]], 
        [strlist[3], strlist[3]]
      ])
```
[['do', 'do'], ['re', 're'], ['mi', 'mi'], ['fa', 'fa']]

### Zipping exercises
See file: (here)[] 

####Variable Explorer comparison: balanced vs. counterbalnced of master list post np.random.shuffle() application.
<img width="529" alt="image" src="https://user-images.githubusercontent.com/113373038/193157832-7a143f6d-3edf-44d7-927b-8763d194798c.png">


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
