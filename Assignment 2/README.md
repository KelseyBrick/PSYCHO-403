### Print Exercises
1. See: [KelseyBrick.py](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment%202/KelseyBrick.py)
2. No variables appeared in the variable explorer.

### Operation exercises
1. Yes, it outputs the same values.
 ```
  print(5/2)          #Integer
  print(5.0/2.0)      #Float
  
  2.5
  2.5
 ```
2. The modulo operator is giving the remainder (R) of "x/y."

   *Note: in the cases where x is smaller than y, the value given is simply x*
 ```
  print(10 % 5)
  print(7 % 2)
  print(8 % 3)
  print(5 % 10)
  print(14 % 142)
  0
  1
  2
  5
  14
 ```
3. The operator "**" is calculating exponents: x "to the power of" y
 ```
  print(1 ** 10)
  print(2 ** 4)
  print(10 ** 2)
  1
  16
  100
 ```
   The operator "//" is calculating floor division. That is, the frequancy of y into x in "x/y"
 ```
  print(1 // 1)
  print(4 // 3)
  print(24 // 7)
  1
  1
  3
 ```
4. Yes, python follows order of operations. 

  *Note: The last line of code is set to ignore order of operations and instead follow order of numbers producing a different value.*
 ```
  print(1 + 1 + (1 * (20 / 2)))
  print(1 + 1 + 1 * 20 / 2)
  print((((1 + 1) + 1) * 20 )/ 2)
  12.0
  12.0
  30.0
```

### Variable Exercises
1. See: [KelseyBrick_2.py](https://github.com/KelseyBrick/PSYCHO-403-Fall-2022/blob/main/Assignment%202/KelseyBrick_2.py)
2. Yes, the variables show up in the editor as strings (Type = str)
3. N/A (there are repeated letters in my name, go to question 4).
4. No, python is outputting the same letter multiple times.
5. No, changing the value of "letterX" did not change the value of the other variables when reprinted.
6. No, "letterX" was still equal to the previously assigned value of "letter1." 
   This indicates that python variable assignment is based on the order of commands.
   <br>
   Example: <br>
     First, "LetterX" = "Letter1"; this set the varable = "K". <br>
     Then, "Letter1" = "Z". <br>
     However, "LetterX" remained equal to "K" because this command came first.

### Boolean Exercises
1. Yes, in python boolean code returns "print(1 == 1.0)" as TRUE.
2. Yes, in python boolean code returns "print(5 == (3+2))" as TRUE.
3. The following code all produced "True" outputs in python:
```
print(1 == 1.0 and not "1" == "1.0" and 5 == (3+2))
print(1 == 1.0 and not "1" == "1.0" or 5 == (3+2))
print(1 == 1.0 or "1" == "1.0" and 5 == (3+2))
print(1 == 1.0 or "1" == "1.0" and not 5 == (3+2))
print(1 == 1.0 and "1" == "1.0" or 5 == (3+2))
```

### List Exercises
1. Yes, it became a variable (Type = "list")
```
 oddlist = [1, 3, 5, 7, 9]
```
2. No error.
```
 print(oddlist)
 [1, 3, 5, 7, 9]
```
3. The len() function says "oddlist" is 5 values.
4. The type() function says "oddlist" is a list.
5. All integers BETWEEN 0-100 would include values 1-99:
```
 intlist = list(range(1, 100))
```
6. print(intlist) returns:
```
 list(range(1, 100))
 print(intlist)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
```
