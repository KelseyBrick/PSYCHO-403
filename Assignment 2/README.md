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
1. 
