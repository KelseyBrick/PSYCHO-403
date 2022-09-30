# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 12:54:04 2022

@author: kelse
"""

#variable operations
#1
sub_code = "sub"
subnr_int = 2
subnr_str = "2"

#print(sub_code + subnr_int) # can't concatonate integer to string
print(sub_code + subnr_str)

#2
#sub 2
print(sub_code + " " + subnr_str)
#sub 222
print(sub_code + " " + subnr_str + subnr_str + subnr_str)
#sub2sub2sub2
print((sub_code + subnr_str)*3)
#subsubsub222
print(sub_code + sub_code + sub_code + subnr_str + subnr_str + subnr_str)

#list operations
#1
numlist = [1, 2, 3]*2
print(numlist)
# numlist = [1, 2, 3]
# print(numlist * 2) # give the same outputs

#2
import numpy as np
numarr = np.array([1, 2, 3])*2
print(numarr)
numlist2 = [1, 2, 3]*4
print(numlist2)

#3
strlist = ['do','re','mi','fa']
# ['dodo','rere','mimi','fafa']
print([strlist[0]*2,strlist[1]*2,strlist[2]*2,strlist[3]*2])
# ['do','re','mi','fa','do','re','mi','fa']
print(strlist *2)
# ['do','do','re','re','mi','mi','fa','fa']
print([ strlist[0], strlist[0], 
        strlist[1], strlist[1], 
        strlist[2], strlist[2], 
        strlist[3], strlist[3]
      ])
# [['do','do'],['re','re'],['mi','mi'],['fa','fa']]
print([ [strlist[0], strlist[0]], 
        [strlist[1], strlist[1]], 
        [strlist[2], strlist[2]], 
        [strlist[3], strlist[3]]
      ])

#Zipping exercises

# create cues
cue1 = ["cue1"] * 25
cue2 = ["cue2"] * 25
print(cue1)
print(len(cue1))                #check for 25 
print(cue2)
print(len(cue2)) 

#create 50 (face, house) pairings
imgs_F1 = (['face1.png'] + ['face2.png'] + ['face3.png'] + ['face4.png'] + ['face5.png'])*5 #keep code on one line.
print(imgs_F1)
imgs_H2 = ["house1.png"]*5 + ["house2.png"]*5 + ["house3.png"]*5 + ["house4.png"]*5 + ["house5.png"]*5 #keep code on one line.
print(imgs_H2)

#create 25 (face, house, cue1) pairings
P1C1 = list(zip(imgs_F1, imgs_H2, cue1))
#create 25 (face, house, cue2) pairings
P1C2 = list(zip(imgs_F1, imgs_H2, cue2))

print(P1C1)
print(P1C2)
print(len(P1C1))                #check for 25 
print(len(P1C2))                #check for 25 
#pair1 = list(zip(imgs_F1, imgs_H2))
#print(pair1)
#print(len(pair1))               #check for 25 pairs

#create 50 (house, face) pairings
imgs_H1 = (["house1.png"] + ["house2.png"] + ["house3.png"] + ["house4.png"] + ["house5.png"])*5 #keep code on one line.
print(imgs_H1)
imgs_F2 = ['face1.png']*5 + ['face2.png']*5 + ['face3.png']*5 + ['face4.png']*5 + ['face5.png']*5  #keep code on one line.
print(imgs_F2)

P2C1 = list(zip(imgs_H1, imgs_F2, cue1))
P2C2 = list(zip(imgs_H1, imgs_F2, cue2))
#pair2 = list(zip(imgs_H1, imgs_F2))
#print(pair2)
#print(len(pair2))               #check for 25 pairs

print(P2C1)
print(P2C2)
print(len(P2C1))                #check for 25 
print(len(P2C2))                #check for 25 

#add cues to pairs >> this created lists with tuples with 2 vs. 3 values because they were paired
#P1C1 = list(zip(pair1, cue1))
#P1C2 = list(zip(pair1, cue2))
#P2C1 = list(zip(pair2, cue1))
#P2C2 = list(zip(pair2, cue2))

#print(P1C1)
#print(P1C2)
#print(P2C1)
#print(P2C2)

#print(len(P1C1))                #check for 25 
#print(len(P1C2))                #check for 25 
#print(len(P2C1))                #check for 25 
#print(len(P2C2))                #check for 25 

#create master list by adding the zipped lists together
master = P1C1 + P1C1 + P2C1 + P2C2
print(master)
print(len(master))            #check for 100

#counterbalance the list using np functions
import numpy as np
np.random.shuffle(master)
print(master)

#Indexing exercises
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
print(colours)
#print the penultimate color.
print(colours[-2])
#print the 3rd and 4th characters of the penultimate color.
print(colours[-2][2])
print(colours[-2][3])
#remove the color "purple" and add "indigo" and "violet" to the list instead.
colours.remove("purple")
print(colours)
colours.insert(5,"indigo")
colours.insert(6,"violet")
print(colours)

#Slicing exercises
#create a list 0-100
list100 = range(101)
print(list(list100))
#Using slicing, print the first 10 numbers in the list.
print(list(list100[:10]))                                           # [START:STOP]
#Using slicing, print all the odd numbers in the list backwards.
print(list(list100[99::-2]))                                        # [START:STOP:STEP]
#Using slicing, print the last four numbers in the list backwards.
print(list(list100[100:96:-1])) 
#Are the 40th-44th numbers in the list equal to integers 39-43? 
#Show the Boolean operation you would use to determine the truth value.
print(list(list100[39:44])) 
#print(list100[39:44] == [39, 40, 41, 42, 43])                      This returns a FALSE output; use syntax below for TRUE
print(list(list100[39:44]) == [39, 40, 41, 42, 43])