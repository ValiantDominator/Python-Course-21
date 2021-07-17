# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 18:02:21 2021

@author: neeb-meister
"""

# Practice problem 1:

# properly import the "utils.py" library. You can do it however you want.
# Run this code and make sure that "utils loaded successfully" prints.
import utils
import json

# Note: you are absolutely allowed to change things in the utils.py file,
# But (like any professional coding environment), you should ensure that
# any code you write will still run and work with the default utils.py!


# Practice problem 2:
# (this one is review for for loops)
# What is the average result of a D20 rolled with advantage?
# Write whatever code you need to determine this answer below.
d20 = utils.Die(20)
total = 0
for i in range(1000):
    total += max(d20.roll(),d20.roll())
print(total/1000)



# Answer in a comment here:
"""
13.8
"""
# No, googling the answer is not good enough
    # (but you can use that to check your work!)



# Practice problem 3:
# Go ahead and download and run that "Utils testing" file and fiddle
# around for a bit.
    # How many zombies are needed so that they have a 1% chance to win?
#10 or 11
    # How many zombies are needed so that they have a 66% chance to win?
#13 or 14
    # How many zombies are needed so that they have a 99% chance to win?
#15
# There's another file I made on the website called "fightSimulation.txt"
# That file is the result of a huge number of fights from the demo code!
# How many times did the troll win total?
"""
660
"""
# What was his victory percentage?
"""
66%
"""
# How many zombies did I have fighting the troll?
"""
12
"""

# Yes, you'll probably need to write some file parsing here.
fightFile = open("fightSimulation.txt","r")
fightText = fightFile.read()
fightList = fightText.split()
trollWins = 0
zombieWins = 0
for winner in fightList:
    if winner == "Troll":
        trollWins += 1
    else:
        zombieWins += 1
fightFile.close()
totalFights = trollWins + zombieWins
trollWinrate = trollWins/totalFights


# Practice problem 4:
# Write a function called "monsterFromFile"
# That takes the name of a file as an argument.
# This function will find out the monster's armor class, attack bonus,
# damage dice, damage bonus, and even name. It will return a monster
# With all of this information properly allocated. This way you can
# define monsters much more easily! You just have to say something like
# skeleton = monsterFromFile('skeleton.monster')
# And that's all you need! So much simpler.
def statMod(score):
    modif = (score-10)//2
    return modif

def HPHelper(hitDice,conPoints,size):
    if size == 'tiny':
        dieSize = 4
    elif size == 'small':
        dieSize = 6
    elif size == 'medium':
        dieSize = 8
    elif size == 'large':
        dieSize = 10
    elif size == 'huge':
        dieSize = 12
    elif size == 'gargantuan':
        dieSize = 20
    HP = statMod(conPoints)*hitDice + hitDice*(dieSize+1)//2
    return HP

def monsterFromFile(filename):
    workfile = open(filename,"r")
    worktext = workfile.read()
    monsterDict = json.loads(worktext)
    #print(monsterDict)
    workfile.close()
    HP = HPHelper(monsterDict['hitDice'],monsterDict['conPoints'],monsterDict['size'])
    dDie = utils.Die(6)
    dBonus = 2
    aBonus = 1
    armorDesc = monsterDict['otherArmorDesc'].split()
    AC = int(armorDesc[0])
    nameM = monsterDict['name']
    return utils.rollingMonster(HP,dDie,dBonus,aBonus,AC,name=nameM)


# Once you've written the function, finish it out by downloading
# the acolyte and skeleton files from the website





# Practice problem 5:
# Copy the "fightManyRoll" function from utils.py here.
# Change the name to "fightManyRollPrint"
# At the end of each fight, this function will append to a file
# (call the file whatever you want) the following information:
# - A fight has just occurred
# - The winner
# - how many monsters fought on each side
# - The names of all the monsters involved
# - The total remaining current HP of the winning side
def fightManyRollPrint(soloMonster,group,suspense = False,printing = True):
    if not soloMonster.alive:
        print("You forgot to refresh")
        return
    for monster in group:
        if not monster.alive:
            print("you forgot to resfresh")
            monster.show()
            return
    while True:
        if suspense:
            time.sleep(2)
        if printing:
            print(soloMonster.name, "vs", "monster group")
            soloMonster.show()
            for monster in group:
                monster.show()
        # First, the big monster tries to hit one in the group
        for monster in group:
            if monster.alive:
                target = monster
                break
        if soloMonster.attack() >= target.AC:
            target.damage(soloMonster.hit())
        # Then, each living monster gets a chance to attack
        for monster in group:
            if monster.alive:
                if monster.attack() >= soloMonster.AC:
                    soloMonster.damage(monster.hit())
        if not group[-1].alive or not soloMonster.alive:
            break
    if soloMonster.alive:
        if printing:
            print("the victor is", soloMonster.name)
            soloMonster.show()
        winner = soloMonster.name
        HPpool = soloMonster.curHP
    else:
        if printing:
            print("the victor is", "the monster group")
            for monster in group:
                monster.show()
        i = 0
        winner = ""
        for monster in group:
            i+=1
            if i == len(group):
                winner += "and "+monster.name
            else:
                winner += monster.name+", "
        HPpool = 0
        for monster in group:
            HPpool += monster.curHP
    i = 0
    groupstr = ""
    for monster in group:
        i+=1
        if i == len(group):
            groupstr += "and "+monster.name
        else:
            groupstr += monster.name+", "
    logfile = open("battleLog.txt","a")
    logfile.write("A fight has just occured \n"+
                  winner + " won \n"+
                  "The fight was a 1 v "+ str(len(group))+"\n"+
                  soloMonster.name + " fought against "+ groupstr+"\n"+
                  "The total remaining HP of the winning side is "+str(HPpool)+
                  "\n\n")
    logfile.close()
    print("Documentation successful")
    if soloMonster.alive:
        return soloMonster.name
    else:
        return "group"
skele = monsterFromFile('skeleton.monster')
acol1 = monsterFromFile('acolyte.monster')
acol2 = monsterFromFile('acolyte.monster')
fightManyRollPrint(skele,[acol1,acol2])
# Now, have one skeleton fight two acolytes
# a couple times in this new function.

