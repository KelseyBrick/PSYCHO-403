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
[Zip exercises file](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment_3/zip_exercise.py)

**Variable Explorer comparison: balanced vs. counterbalnced of master list post np.random.shuffle() application.**
<img width="529" alt="image" src="https://user-images.githubusercontent.com/113373038/193157832-7a143f6d-3edf-44d7-927b-8763d194798c.png">


### Indexing Exercises
1. Create a list of strings called "colors", containing the following colors in this order: red, orange, yellow, green, blue, purple. See code:
```
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
print(colours)
```
['red', 'orange', 'yellow', 'green', 'blue', 'purple']

2. Using indexing, print the penultimate color. See code:
```
print(colours[-2])
```
blue

3. Using indexing, print the 3rd and 4th characters of the penultimate color. See code:
```
print(colours[-2][2])
print(colours[-2][3])
```
u
e

4. Using indexing, remove the color "purple" and add "indigo" and "violet" to the list instead. See code:
```
colours.remove("purple")
print(colours)
colours.insert(5,"indigo")
colours.insert(6,"violet")
print(colours)
```
['red', 'orange', 'yellow', 'green', 'blue'] <br>
['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

### Slicing exercises
1. Create a list of numbers 0-100 called "list100".
```
list100 = range(101)
print(list(list100))
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, <br>
20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, <br>
40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, <br>
60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, <br>
80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

2. Using slicing, print the first 10 numbers in the list.
```
print(list(list100[:10])) 
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

3. Using slicing, print all the odd numbers in the list backwards.
```
print(list(list100[99::-2]))   
```
[99, 97, 95, 93, 91, 89, 87, 85, 83, 81, 79, 77, 75, 73, 71, 69, 67, 65, 63, 61, <br>
59, 57, 55, 53, 51, 49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, <br>
19, 17, 15, 13, 11, 9, 7, 5, 3, 1]

4. Using slicing, print the last four numbers in the list backwards.
```
print(list(list100[100:96:-1])) 
```
[100, 99, 98, 97]

5. Are the 40th-44th numbers in the list equal to integers 39-43? Show the Boolean operation you would use to determine the truth value.
```
print(list(list100[39:44])) 
#print(list100[39:44] == [39, 40, 41, 42, 43])                      This returns a FALSE output; use syntax below for TRUE
print(list(list100[39:44]) == [39, 40, 41, 42, 43])
```
[39, 40, 41, 42, 43] <br>
True
