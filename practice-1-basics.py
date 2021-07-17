# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:54:30 2021

@author: Daniel Mishler
"""

# Practice problem 1:
# What is the data type of "Object"?
# Be specific! If it is
  # something that contains other things, what are those things?

Object = [1,2,3,"four"]

'''
list of [int,int,int,string]
'''

# Practice problem 2:
# Write a function that takes in a number as an argument.
# Your function will *print* to the user what group the number belongs to.
# These groups could be natural numbers, whole numbers, integers, and
# Real Numbers. Don't worry about rational numbers for this problem.
def numberType(number):
    if type(number) == int and number > 0:
        print("natural")
    elif type(number) == int and number >= 0:
        print("whole")
    elif type(number) == int:
        print("integer")
    else:
        print("real")
            

# Practice problem 3:
# This function returns the mean of all elements in a list or array
# of real numbers.
def myMean(yourList):
    listSum = 0
    error = 0
    for i in yourList:
        if type(i) == int or type(i) == float:
            listSum += i
        else:
            print("Error: List contains non-number")
            error = 1
    listMean = listSum/len(yourList)
    if error == 1:
        return None
    else:
        return listMean
# But note that a program will crash if you pass the function something
# that is not a list or array, or a list that contains something that
# isn't a real number.
# Fix this oversight by adding in type checking! You can return None
# If an error is given.

# Your function should be able to handle the following:
# print(myMean([1,3,4]))
# print(myMean("xd"))
# print(myMean([1,3,"four"]))


# Practice problem 4:
# Write a function that takes a whole number that is between
# [20-99] (inclusive), and will *print* the spelling of such a
# number to the screen.
# Note that you don't have to check that the argument is, indeed,
# a whole number in this range. In general for homework problems,
# error check is good practice but not necessary.

# For example, if I passed 21, you should print "twenty-one".
# If you need any help, consult the following link
# https://www.tools4noobs.com/online_tools/number_spell_words/
def spellOnes(number):
    if number == 1:
        return "one" 
    elif number == 2:
        return "two"
    elif number == 3:
        return "three"
    elif number == 4:
        return "four"
    elif number == 5:
        return "five"
    elif number == 6:
        return "six"
    elif number == 7:
        return "seven"
    elif number == 8:
        return "eight"
    elif number == 9:
        return "nine"

def spellTens(number):
    if number == 1:
        return "reeeeeeeeeeeee" 
    elif number == 2:
        return "twenty"
    elif number == 3:
        return "thirty"
    elif number == 4:
        return "fourty"
    elif number == 5:
        return "fifty"
    elif number == 6:
        return "sixty"
    elif number == 7:
        return "seventy"
    elif number == 8:
        return "eighty"
    elif number == 9:
        return "ninety"

def spell(number):
    if number >= 20 and number <= 99:
        listNumber = [int(a) for a in str(number)]
        ones = spellOnes(listNumber[1])
        tens = spellTens(listNumber[0])
        print(tens + "-" + ones)
    else:
        print("Error: put a number between 20 and 99 cockass")



# Practice problem 5:
# The distance between two ordered pairs of points (a,b) and (c,d)
# is ((a-c)^2 + (b-d)^2)^(1/2) (shoutout to Pythagorus). Write a
# function that takes a tuple (a,b) and a tuple (c,d) and returns
# The distance between them.


