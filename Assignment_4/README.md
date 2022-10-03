### Conditional exercises
1. You want to tell your experiment to record participant responses. If the response is "1" or "2", print OK. If the response is "NaN" (empty), print a "subject did not respond" message. If the response is anything else, print "subject pressed the wrong key".
```
response = ''
if response == '1' or response == '2':
    print('OK')
elif response == 'NaN':
    print('empty')
else: print("subject pressed the wrong key")
```
2. Create a nested "if" statement in the above exercise. If the response is "1", print "Correct!". If the response is "2", print "Incorrect!"
```
response = ''
if response == '1' or response == '2':
    if response == '1':
        print("correct")
    if response == '2':
        print("incorrect")
elif response == 'NaN':
    print('empty')
else: print("subject pressed the wrong key")
```
3. Test out your script with various responses. Does it do what you expect it to?

Yes, I tested all responses and the code works. Below are some examples.
```
# Version 1 

response = '1'
if response == '1' or response == '2':
    print('OK')
elif response == 'NaN':
    print('empty')
else: print("subject pressed the wrong key")
```
OK
```
# Version 2

response = '1'
if response == '1' or response == '2':
    if response == '1':
        print("correct")
    if response == '2':
        print("incorrect")
elif response == 'NaN':
    print('empty')
else: print("subject pressed the wrong key")

response = 'hello'
if response == '1' or response == '2':
    if response == '1':
        print("correct")
    if response == '2':
        print("incorrect")
elif response == 'NaN':
    print('empty')
else: print("subject pressed the wrong key")
```
Correct <br>
subject pressed the wrong key

### For loop exercises
1. Remember the exercise where you printed each letter of your name? Create a for loop that prints each letter without writing out all of the print statements manually.
```
name = ['K', 'E', 'L', 'S', 'E', 'Y']           # name as list

for letter in name:
    image = letter
    print(image)

myName = "Kelsey"                               # name as string
   
for letter in myName:
    print(letter)
```
K <br>
E <br>
L <br>
S <br>
E <br>
Y <br>
K <br>
e <br>
l <br>
s <br>
e <br>
y <br>

2. Add an index counter and modify your loop to print the index number after each letter
```
name = ['K', 'E', 'L', 'S', 'E', 'Y']           # name as list
count = -1

for letter in name:
    count = count + 1
    image = letter
    print("Index # %s" %count)      #make sure to add %s argument and %count argument
    print(image)

myName = "Kelsey"                               # name as string
count = -1

for letter in myName:
    count = count + 1
    image = letter
    print("Index # %s" %count)      #make sure to add %s argument and %count argument
    print(image)
    
```
Index # 0 <br>
K <br>
Index # 1 <br>
E <br>
Index # 2 <br>
L <br> 
Index # 3 <br>
S <br>
Index # 4 <br>
E <br>
Index # 5 <br>
Y <br>
Index # 0 <br>
K <br>
Index # 1 <br>
e <br>
Index # 2 <br>
l <br>
Index # 3 <br>
s <br>
Index # 4 <br>
e <br>
Index # 5 <br>
y <br>

3. Create a list of names "Amy","Rory", and "River". Create a nested for loop to loop through each letter of each name.
```
group = ["Amy","Rory","River"]
#Create a nested for loop to loop through each letter of each name.
for name in group:
    print(name)
    for letters in name:    #calls the values (i.e. letters) from the variable name (assigned in previous line)
        print(letters)
```
Amy <br>
A <br>
m <br>
y <br>
Rory <br>
R <br>
o <br>
r <br>
y <br>
River <br>
R <br>
i <br>
v <br>
e <br>
r <br>

4. Add an index counter that gives the index of each letter for each name. The counter should start over at 0 for each name in the list.

### While loop exercises
1. Create a while loop of 20 iterations that prints "image1.png" for the first 10 iterations, and "image2.png" for the next 10 iterations.

2. Create a while loop that shows an image until the participant makes a response of 1 or 2. Run it a few times to make sure it works the way you expect.

3. Create a failsafe that terminates the previous while loop after 5 iterations if one of the valid responses (1,2) have not been made in that time.
