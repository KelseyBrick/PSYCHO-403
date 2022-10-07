# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:53:32 2022

@author: kelse
"""
#Conditional exercises

#tell your experiment to record participant responses. 
#If the response is "1" or "2", print OK. 
response = ''
if response == '1' or response == '2':
    print('OK')
#If the response is "NaN" (empty), print a "subject did not respond" message. 
elif response == 'NaN':             #NaN = 'not a number'
    print('empty')
#If the response is anything else, print "subject pressed the wrong key".
else: print("subject pressed the wrong key")

#Create a nested "if" statement in the above exercise. 
#If the response is "1", print "Correct!". 
response = '1'
if response == '1' or response == '2':
    if response == '1':
        print("correct")
    if response == '2':
        print("incorrect")
#If the response is "2", print "Incorrect!"
response = '2'
if response == '1' or response == '2':
    if response == '1':
        print("correct")
    if response == '2':
        print("incorrect")

#Test out your script with various responses. Does it do what you expect it to?

#version one:

response = '1'
#If the response is "1" or "2", print OK. 
if response == '1' or response == '2':
    print('OK')
#If the response is "NaN" (empty), print a "subject did not respond" message. 
elif response == 'NaN':
    print('empty')
#If the response is anything else, print "subject pressed the wrong key".
else: print("subject pressed the wrong key")

response = 'NaN'
#If the response is "1" or "2", print OK. 
if response == '1' or response == '2':
    print('OK')
#If the response is "NaN" (empty), print a "subject did not respond" message. 
elif response == 'NaN':
    print('empty')
#If the response is anything else, print "subject pressed the wrong key".
else: print("subject pressed the wrong key")

response = 'hello'
#If the response is "1" or "2", print OK. 
if response == '1' or response == '2':
    print('OK')
#If the response is "NaN" (empty), print a "subject did not respond" message. 
elif response == 'NaN':
    print('empty')
#If the response is anything else, print "subject pressed the wrong key".
else: print("subject pressed the wrong key")

#version two (nested):

response = '1'
#If the response is "1" or "2", print OK. 
if response == '1' or response == '2':
    if response == '1':
        print("correct")
    if response == '2':
        print("incorrect")
#If the response is "NaN" (empty), print a "subject did not respond" message. 
elif response == 'NaN':
    print('empty')
#If the response is anything else, print "subject pressed the wrong key".
else: print("subject pressed the wrong key")

response = '2'
#If the response is "1" or "2", print OK. 
if response == '1' or response == '2':
    if response == '1':
        print("correct")
    if response == '2':
        print("incorrect")
#If the response is "NaN" (empty), print a "subject did not respond" message. 
elif response == 'NaN':
    print('empty')
#If the response is anything else, print "subject pressed the wrong key".
else: print("subject pressed the wrong key")



#looping exercises

#Create a for loop that prints each letter of your name without writing out all of the print statements manually.
name = ['K', 'E', 'L', 'S', 'E', 'Y']           # name as list

for letter in name:
    image = letter
    print(image)

myName = "Kelsey"                               # name as string
   
for letter in myName:
    print(letter)

#Add an index counter and modify your loop to print the index number after each letter
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
    
#Create a list of names "Amy","Rory", and "River". 
group = ["Amy","Rory","River"]
#Create a nested for loop to loop through each letter of each name.
for name in group:
    print(name)
    for letters in name:    #calls the values (i.e. letters) from the variable name (assigned in previous line)
        print(letters)


#Add an index counter that gives the index of each letter for each name. 
#The counter should start over at 0 for each name in the list.
for name in group:
    print(name)
    letterCounter = -1
    for letters in name:    #calls the values (i.e. letters) from the variable name (assigned in previous line)
        letterCounter = letterCounter + 1
        print("Letter index # %i" %letterCounter)
        print(letters)


#Create a 'while' loop of 20 iterations that prints "image1.png" for the first 10 iterations, and "image2.png" for the next 10 iterations.
iterations = 0                                 #begin counting from 0

while iterations <= 21:                         #arguement for 20 iterations (note: -1, so 20 = 19)    
    iterations = iterations + 1                 
    if iterations <= 10:                       #first 10 do this (<=10 necessary to get include 10th; otherwise < 11)
    #if iterations < 11:
        print('%i image1.png' %iterations)
    elif iterations <= 20:                     #next 10 do that (<=20 necessary to get include 20th; otherwise < 21)
    #elif iterations < 21:
        print('%i image2.png' %iterations)

#Create a 'while' loop that shows an image until the participant makes a response of 1 or 2. Run it a few times to make sure it works the way you expect.
import random
image = True

while image:
    response = random.randint(0, 10)
       
    if response == 1 or response == 2:              #have this conditional first otherwise while loops indefinetly
        image = False
        print("Response %i made." %response)
        
    elif response != 1 or response != 2:
        print('Response #%i: IMAGE' %response)
        
#    if response != 1 or response != 2:             this code created nopn-stop looping.
#        print('Response #%i: IMAGE' %response)

#    elif response == 1 or response == 2:              
#        image = False
#        print("Response %i made." %response)

#Create a failsafe that terminates the previous while loop after 5 iterations if one of the valid responses (1,2) have not been made in that time.
import random
image = True
failSafe = -1                                       #terminate if no response after 5 iterations
while image:
    response = random.randint(0, 10)
    failSafe = failSafe + 1
    
    if failSafe == 5:
        print("Too many attempts. Trial stopped.")
        break
        
    if response == 1 or response == 2:              #have this conditional first otherwise while loops indefinetly
        image = False
        print("Response %i made." %response)
        
    elif response != 1 or response != 2:
        print('Response #%i: IMAGE' %response)
        



