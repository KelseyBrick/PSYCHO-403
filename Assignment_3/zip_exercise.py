# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:11:49 2022

@author: kelse
"""

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

#create 50 (house, face) pairings
imgs_H1 = (["house1.png"] + ["house2.png"] + ["house3.png"] + ["house4.png"] + ["house5.png"])*5 #keep code on one line.
print(imgs_H1)
imgs_F2 = ['face1.png']*5 + ['face2.png']*5 + ['face3.png']*5 + ['face4.png']*5 + ['face5.png']*5  #keep code on one line.
print(imgs_F2)

P2C1 = list(zip(imgs_H1, imgs_F2, cue1))
P2C2 = list(zip(imgs_H1, imgs_F2, cue2))

print(P2C1)
print(P2C2)
print(len(P2C1))                #check for 25 
print(len(P2C2))                #check for 25 

#create master list by adding the zipped lists together
master = P1C1 + P1C1 + P2C1 + P2C2
print(master)
print(len(master))            #check for 100

#counterbalance the list using np functions
import numpy as np
np.random.shuffle(master)
print(master)