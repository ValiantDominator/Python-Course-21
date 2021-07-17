# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 20:00:39 2021

@author: Daniel Mishler
"""
import thomasUtils
import json
# Practice problem 1a:
# Remember the try-except block we learned in class?
# Take a look at this division function

def ironDivision(a,b):
    if type(a) != int and type(a) != float:
        return None
    elif type(b) != int and type(b) != float:
        return None
    elif b == 0:
        return None
    else:
        quotient= a/b
        return quotient

# Go back into that function and use some if statements to handle the
# following:
    # if b is equal to 0, just return "None"
    # if a is not an integer or float, just return "None"
    # if b is not an integer or float, just return "None"

# Practice problem 1b:
# Let's tackle the same problem in a different way

def lazyDivision(a,b):
    try:
        return a/b
    except:
        return None

# This time, fix all of the above problems, except do it
# WITHOUT if statements and do it in no more than 5 lines!

# Practice problem 2:
# Last week, I was hard on you with monsterFromFile. This week, we're
# going to finish it out now.
# You should already have the AC and name of the creature down pat.

# HP:
    # The HP of the monster is calulated as follows:
        # (number of hit dice) * (hit dice average roll + constitution mod)
    # The number of hit dice and the constitution mod are in the monster Dict!
    # The hit dice type is found in the monster's size. If the monster is:
        # Tiny: d4 (average 2.5)
        # Small: d6 (average 3.5)
        # Medium: d8 (average 4.5)
        # Large: d10 (average 6.5)
        # Huge: d12 (average 10.5)
        # Gargantuan: d20
    # Finally, round up if you found something that ends in 0.5

# Attack Bonus:
    # Take a look at the "actions" key. It might be an array, it might
    # be another dict. Figure out how you're going to handle this!
    # Then, once you have a string that has an attack bonus in it,
    # Find out how to pick out that number.
    # I'd recommend looking into the .find() method for strings
    # and knowing how to splice!

# Damage bonus:
    # Just like you found the attack bonus, hunt down the damage bonus
    # in the same string. It can be found in the open and close parentheses!

# Damage diece:
    # Be cautious with this one: it's found next to the damage bonus,
    # but be sure you parse the NUMBER of dice and the TYPE of die correctly,
    # and be ready to create a utils.Dice() array of all the dice used!
    # If you're having trouble, just start with one die instead, and go
    # from there.
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

def dieParse(dicestr):
    dieNum = int(dicestr.split('d')[0])
    dieMag = int(dicestr.split('d')[1])
    dice = []
    for i in range(dieNum):
        dice.append(thomasUtils.Die(dieMag))
    dDie = thomasUtils.Dice(dice)
    return dDie

def weaponHelper(mdict):
    try:
        # take the first action and make a string of it
        actionstr = mdict['actions'][0]['desc']
        # extract the value that comes before 'to hit'
        aBonus = int(actionstr[:actionstr.find('to hit')].split()[-1]) 
        
        # an attack can either have a bonus or not
        # try case 1: there is a bonus, get the bonus and the dice
        try:
            # 2nd to last should be modifier, we want everything except the last char
            dBonus = int(actionstr[:actionstr.find('damage')].split()[-2][:-1])
            # 4th to last should be dice, ill use a different function to parse it
            dDie = dieParse(actionstr[:actionstr.find('damage')].split()[-4][1:])
        # except case 2: there is no bonus, get the dice and leave
        except:
            dBonus = 0
            dDie = dieParse(actionstr[:actionstr.find('damage')].split()[-2][1:-1])
        return [dDie, dBonus, aBonus]
    except:
        return "No action found"
    

def monsterFromFile(filename):
    workfile = open(filename,"r")
    worktext = workfile.read()
    monsterDict = json.loads(worktext)
    #print(monsterDict)
    workfile.close()
    HP = HPHelper(monsterDict['hitDice'],monsterDict['conPoints'],monsterDict['size'])
    tval = weaponHelper(monsterDict)
    dDie = tval[0]
    dBonus = tval[1]
    aBonus = tval[2]
    dex = statMod(monsterDict['dexPoints'])
    armorDesc = monsterDict['otherArmorDesc'].split()
    AC = int(armorDesc[0])
    nameM = monsterDict['name']
    return thomasUtils.rollingMonster(HP,dDie,dBonus,aBonus,AC,dexmod=dex,name=nameM)


# Practice problem 3:
# We're going to bring it all home:
# write a function called "fightFinal" that will:
    # Have a group of monsters fight a second group of monsters.
        # Turn order goes as the following:
            # First alive group A monster attacks first alive group B monster
            # First alive group B monster attacks first alive group A monster
            # Second alive group A monster attacks first alive group B monster
            # Second alive group B monster attacks first alive group A monster
            # Third alive group A monster attacks first alive group B monster
            # Third alive group B monster attacks first alive group B monster
            # ...
            # And so on. If a monster group only has 3 versus 7, then the
            # group with more monsters gets to all act before the next round
            # starts. So a fighting order with [A1,A2,A3] vs. [B1,B2,B3...B8]
            # might look like:
                # A1 -> B1
                # B1 -> A1
                # A2 -> B1 (kills it)
                # B2 -> A1
                # A3 -> B2
                # B3 -> A1
                # B4 -> A1 (kills it)
                # B5 -> A2
                # B6 -> A2
                # B7 -> A2
                # B8 -> A2
    # The monsters are all rolling monsters, of course.
    # Also: still print the results of the fight like last assignment,
    # now accounting for the groups.
# You should be able to properly read
    # Zombie
    # Skeleton
    # Acolyte
    
## Returns true if a least 1 member of the group is alive
def aliveCheck(group1):
    g1 = False
    for i in group1:
        if i.alive:
            g1 = True
    if g1:
        return True
    else:
        return False

## Returns an index for a target in the group
def targetPick(group):
    monsterIndex = 0
    for i in group:
        if i.alive:
            return monsterIndex
        monsterIndex += 1
    return 0

def initiative(group1,group2):
    #puts two groups into an initiative order, returns a list that contains 2 lists
    #a list of monsters, and a list on integers
    mlist = []
    for i in range(len(group1)):
        mlist.append({'monster': group1[i], 'team': 1, 'initiative': group1[i].initiative()})
    for i in range(len(group2)):
        mlist.append({'monster': group2[i], 'team': 2, 'initiative': group2[i].initiative()})
    srt = lambda m : m['initiative']
    mlist.sort(reverse=True, key=srt)
    return mlist

def attack(attacker,defender):
    if attacker.attack() >= defender.AC and attacker.alive:
        defender.damage(attacker.hit())

def printGroup(group):
    if len(group) == 1:
        groupstr = group[0].name
    elif len(group) == 2:
        groupstr = group[0].name + " and " + group[1].name 
    else: 
        i = 0
        groupstr = ""
        for monster in group:
            i+=1
            if i == len(group):
                groupstr += "and "+monster.name
            else:
                groupstr += monster.name+", "
    return groupstr

def dictExtract(l,term):
    nl=[]
    for m in l:
        nl.append(m[term])
    return nl

def fightFinal(group1,group2,suspense = False,printing = True,refresh=True):
    ## initialize fight
    ## initiative order
    attackOrder = initiative(group1,group2)
    iorder = dictExtract(attackOrder,'monster')
    teamlist = dictExtract(attackOrder,'team')
    initroll = dictExtract(attackOrder,'initiative')
    
    if printing == True:
        print(printGroup(group1))
        print("vs")
        print(printGroup(group2))
        print()
        i = 0
        for monster in iorder:
            print("Team " + str(teamlist[i]))
            print("Initiative Roll " + str(initroll[i]))
            i += 1
            monster.show()
            print()
    if suspense == True:
        thomasUtils.time.sleep(3)
    ## while loop of fighting
    ## break after a group dies
    r = 0
    while aliveCheck(group1) and aliveCheck(group2):
        if printing == True:
            i = 0
            print()
            print("-----Start of Round " + str(r+1) + "-----\n")
            for monster in iorder:
                print("Team " + str(teamlist[i]))
                i += 1
                monster.show()
                print()
            print("-----End of Round " + str(r+1) + "-----")
        for i in range(len(iorder)):
            if suspense == True:
                thomasUtils.time.sleep(2)
            if teamlist[i] == 1:
                attack(iorder[i],group2[targetPick(group2)])
            else:
                attack(iorder[i],group1[targetPick(group1)])
        r += 1
    if aliveCheck(group1):
        winningTeam = group1
        winnum = 1
    else:
        winningTeam = group2
        winnum = 2
    ## post fight printing
    if printing == True:
        print()
        print("The winners are team "+str(winnum))
        print(printGroup(winningTeam))
        i = 0
        print()
        print("-----End of Fight-----\n")
        for monster in iorder:
            print("Team " + str(teamlist[i]))
            i += 1
            monster.show()
            print()
        print("-----End of Fight-----\n")
        logfile = open("battleLog.txt","a")
        logfile.write("A fight has just occured \n"+
                  printGroup(winningTeam) + " won \n"+
                  "The fight was a "+str(len(group2))+" v "+ str(len(group2))+"\n"+
                  printGroup(group1) + " fought against "+ printGroup(group2)+"\n"+
                  "\n\n")
        logfile.close()
        print("Documentation successful")
    
    if refresh:
        for mon in group1:
            mon.refresh()
        for mon in group2:
            mon.refresh()
    return winnum
    
# Practice problem 4a:
# Have 3 zombies and 3 skeletons fight 6 skeletons.
def buildTeam(listofstr):
    #Builds a list of monsters from a list of strings
    team = []
    for name in listofstr:
        filename = name+".monster"
        team.append(monsterFromFile(filename))
    return team

team1 = buildTeam(["zombie","zombie","zombie","skeleton","skeleton","skeleton"])
team2 = buildTeam(["skeleton","skeleton","skeleton","skeleton","skeleton","skeleton"])
team3 = buildTeam(["skeleton","skeleton","skeleton","zombie","zombie","zombie"])
team4 = buildTeam(["acolyte","acolyte"])
team5 = buildTeam(['skeleton'])
team6 = buildTeam(['bugbear','bugbear'])
        
team1wins = 0
for i in range(1000):
    victor = fightFinal(team1,team2,suspense=False,printing=False)
    for nigga in team1:
        nigga.refresh()
    for nigga in team2:
        nigga.refresh()
    if victor == 1:
        team1wins += 1

# Empirically show who wins if the zombies and skeletons array is
# organized so that the zombies act and are hit first.
# A mathematical argument is not good enough. Use python to prove it.
# (one fight is not enough)

# 4b: do the same for if the skeletons act and are hit first.

team3wins = 0
for i in range(1000):
    victor = fightFinal(team3,team2,suspense=False,printing=False)
    for nigga in team3:
        nigga.refresh()
    for nigga in team2:
        nigga.refresh()
    if victor == 1:
        team3wins += 1

team4wins = 0
for i in range(1000):
    victor = fightFinal(team4,team5,suspense=False,printing=False)
    for nigga in team4:
        nigga.refresh()
    for nigga in team5:
        nigga.refresh()
    if victor == 1:
        team4wins += 1

## Before Initiative
## Arrangement 1 wins about 53% of the time
## Arrangement 2 wins about 34% of the time

## After Initiative
## Arrangement 1 wins about 55% of the time
## Arrangement 2 wins about 30% of the time

# Practice problem 5:
"""
Make an extension to our code to include something we don't have yet!
"""
# Suggestion:
# Note that the "Troll" is a class that exists sort of outside the
# normal generic monster class. That's because the troll is special:
# our code infrastructure isn't really designed to handle all these
# special abilities in a generic rolling monster.
# However, we made the troll regenerate before it attacks
# so that it fits into our fight function.
# (shoot, actually there's a bug where it does it before it hits,
# why don't you go ahead and fix that?)
# Pick any monster that has a special ability like the troll.
# (Hell, even the Zombie's undead fortitude is good enough)
# And make a monster class for it.

# Suggestion:
# Add an initiative system for the monsters

# Suggestion:
# Implement a mechanic of ranged attacks versus melee attacks

# Suggestion:
# Implement ciritical attacks (roll 20 = autohit and double dice)
# alongisde critical fails (roll 1 = miss your attack)

# Or anything else that you wish!
# Submit any relevant changes to known files to me as well.
# For this assignment, it is okay if you change utils.py