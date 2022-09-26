# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 16:45:33 2022

@author: kelse
"""
# Operation exercises
# 1. Divide 5/2 (integer format) and 5.0/2.0 (float format). 

print(5/2)          #Integer

print(5.0/2.0)      #Float

# Does python output the same values for these? 
    # No.
# (Might get a different answer depending on the version of python you are in). 
# If you got a different answer for the two operations, explain why.
    # N/A; But if they did it maybe would have to do with rounding?
    
# 2.  What does the modulo operator (**) do? 
# Try it out with a few numbers in this format: "x % y" to get an idea.

print(10 % 5)
print(7 % 2)
print(8 % 3)
print(5 % 10)
print(14 % 142)

# "x % y" is the modulo operator and is giving the remainder (R) of "x/y"
# in the cases where x is smaller than y, the value given is simply x 
# source: https://bit.ly/3Bnxpwf

# 3 What do these operators do: ** and //? 
# Try them out with a few numbers in this format: "x // y" to get an idea.

print(1 ** 10)
print(2 ** 4)
print(10 ** 2)
   
# this is calculating exponents: x "to the power of" y
print(1 // 1)
print(4 // 3)
print(24 // 7)
 
# this is calculating the first part of the "x / y"
# However, this is not producing the remainder (R) from the "x % y"
# it is only returning the frequency of y into x (i.e., Floor Division)
# Source: https://www.educative.io/answers/floor-division

# 4. Does python follow order of operations? 
# Try it out with a few numbers in this format: "a + b + c * d / e"
print(0 + 0 + 1 * 20 / 2)
print(1 + 1 + 1 * 20 / 2)
# YES, it is following order of operations. If not, the second answer = 30.
# add in order of operations brackets
print(1 + 1 + (1 * (20 / 2)))
print(1 + 1 + 1 * 20 / 2)
print((((1 + 1) + 1) * 20 )/ 2)

#Boolean exercises
#1. 
print(1 == 1.0)
#2.
print(5 == (3+2)) 
#3. 
print(1 == 1.0 and not "1" == "1.0" and 5 == (3+2))
print(1 == 1.0 and not "1" == "1.0" or 5 == (3+2))
print(1 == 1.0 or "1" == "1.0" and 5 == (3+2))
print(1 == 1.0 or "1" == "1.0" and not 5 == (3+2))
print(1 == 1.0 and "1" == "1.0" or 5 == (3+2))

#List exercises
#1.
oddlist = [1, 3, 5, 7, 9]
#2. 
print(oddlist)
#3. 
len(oddlist)
#4.
type(oddlist)
#5.
intlist = list(range(1, 100))   #to get integers btw 0-100 start at 1.
#6.
print(intlist)

#Dictionary exercises
#1.
about_me = {'Name': "Kelsey Brick", 
            'Age': 40.0, 
            'Year of Study': 8, 
            'Favorite foods': ['tacos', 'grilled cheese', 'sushi']
            }
#double click the entry in variable explorer to check entry types.
#2.
print(about_me)
type(about_me)
#3.
len(about_me)
#using "text labels" to determine length

# Array exercises
#1. 
import numpy as np
mixnums = np.array([1.0, 2.0, 3.0, 4, 5, 6])
print(mixnums)
#2. 
mixtypes = np.array([1.0, 2.0, 3, 4, "rad", "sauce"])
print(mixtypes)
#3.
oddarray = np.arange(1, 100, 2)
print(oddarray)
#4. 
logarray = np.logspace(1.0, 5.0, 16)
print(logarray)
#Step one: import "matplotlib.pyplot as plt"
import matplotlib.pyplot as plt      
#Step two: use plt.plot() function with the array
plt.plot(logarray)
#Step three: use plt.show() function
plt.show()
# Output appears in the "Plots" pane on the right.
