# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 11:14:29 2021

@author: neeb-meister
"""

import random
import time

class Die:
    def __init__(self,dieMax):
        self.max = dieMax
        self.name = "d"+str(self.max)
        return
    def roll(self): # Always use "self" as first argument!
        return random.randint(1,self.max)
    def loudRoll(self):
        result = random.randint(1,self.max)
        print(self.name,"rolls",result)
        return result
    

class Dice:
    def __init__(self,dieList):
        self.dice = dieList
        self.name = ""
        for die in dieList:
            self.name = die.name
        return
    def rollCall(self):
        for i in self.dice: # For each die
            print(i.name)
    def roll(self):
        result = 0
        for i in self.dice:
            result += i.roll()
        return result
    def loudRoll(self):
        result = 0
        for i in self.dice:
            result += i.loudRoll()
        print("group total:",result)
        return result

class Troll:
    # any monster with HP, a damage die, and damage bonus
    def __init__(self):
        self.maxHP = 84
        self.curHP = 84
        self.damageDie = Dice([Die(6),Die(6),Die(6),Die(6)])
        self.damageBonus = 10
        self.alive = True
        self.name = "Troll"
        self.regenDie = Die(20)
        return # You don't have to put the return here
    def show(self):
        print()
        print(self.name, "stats")
        print(self.curHP,"/",self.maxHP)
        print(self.damageBonus,"+",self.damageDie.name)
    def regen(self):
        if self.alive:
            self.curHP += self.regenDie.roll()
            if self.curHP > self.maxHP:
                self.curHP = self.maxHP
    def hit(self): # dealing damage
        damage = self.damageBonus + self.damageDie.roll()
        self.regen() # This is exclusively so it fits in our fight function.
        return damage
    def damage(self,damage): # taking damage
        self.curHP -= damage
        if self.curHP <= 0:
            self.curHP = 0
            self.alive = False
        return
    def refresh(self):
        self.curHP = self.maxHP
        self.alive = True

troll = Troll()
# Practice set 3: advanced classes

# Practice problem 1:
# Go ahead and copy the code for the generic monster class that we made in class.
class genericMonster:
    # any monster with HP, a damage die, and damage bonus
    def __init__(self,HP,damageDie,damageBonus,name="generic monster"):
        self.maxHP = HP
        self.curHP = HP
        self.damageDie = damageDie
        self.damageBonus = damageBonus
        self.alive = True
        self.name = name
        return # You don't have to put the return here
    def show(self):
        print()
        print(self.name, "stats")
        print(self.curHP,"/",self.maxHP)
        print(self.damageBonus,"+",self.damageDie.name)
    def hit(self): # dealing damage
        damage = self.damageBonus + self.damageDie.roll()
        return damage
    def damage(self,damage): # taking damage
        self.curHP -= damage
        if self.curHP <= 0:
            self.curHP = 0
            self.alive = False
        return
    def refresh(self):
        self.curHP = self.maxHP
        self.alive = True



# Now initialize three zombies (health 22, damage 1+1d6)
# (Pst... if you can't run the code after just copying the zombie init code,
          # think about what class you might be missing in this file still)
zombie1 = genericMonster(22,Die(6),1,"zombie")
zombie2 = genericMonster(22,Die(6),1,"zombie")
zombie3 = genericMonster(22,Die(6),1,"zombie")
zombie4 = genericMonster(22,Die(6),1,"zombie")
zombie5 = genericMonster(22,Die(6),1,"zombie")
zombie6 = genericMonster(22,Die(6),1,"zombie")
zombie7 = genericMonster(22,Die(6),1,"zombie")
zombie8 = genericMonster(22,Die(6),1,"zombie")



# Now create an list called zombies that contains the three zombies you made.
horde1 = [zombie1,zombie2,zombie3]
horde2 = [zombie1,zombie2,zombie3,zombie4,zombie5,zombie6,zombie7,zombie8]
# Now use a for loop to iterate through the list
    # and print the stats of each zombie.
for i in horde1:
    i.show()
    print()


# Practice problem 2:
# Remember that "fight" function that we made earlier?
# We're going to make a similar function called "fightMany"
# It takes in two arguments:
    # The first is a single strong monster
    # The second is a list of many other monsters teaming up against it
# Remember that in order to make this function you'll have to have *all*
# of the other creatures act and do their damage each round.
# Write your function here:
def fightMany(monster1,listofmonster,suspense = False):
    if not monster1.alive:
        print("You forgot to refresh")
        return
    for monstie in listofmonster:
        if not monstie.alive:
            print("You forgot to refresh")
            return
    while True:
        if suspense:
            time.sleep(1)
        print(monster1.name,end=" ")
        print("vs",end=" ")
        i=0
        for monstie in listofmonster:
            i+=1
            if i == len(listofmonster):
                print("and "+monstie.name,end="")
            else:
                print(monstie.name+", ",end="")
        print()
        monster1.show()
        for monstie in listofmonster:
            monstie.show()
        for monstie in listofmonster:
            if monstie.alive:
                monster1.damage(monstie.hit())
        if not monster1.alive:
            break
        ready = True
        for monstie in listofmonster:
            if monstie.alive and ready:
                monstie.damage(monster1.hit())
                ready = False
        i=0
        for monstie in listofmonster:
            if not monstie.alive:
                i+=1
        if i == len(listofmonster):
            break
                
    print()
    if monster1.alive:
        print("the victor is", monster1.name)
        monster1.show()
        return monster1.name
    else:
        print("the victor is ",end="")
        i=0
        for monstie in listofmonster:
            i+=1
            if i == len(listofmonster):
                print("and "+monstie.name,end="")
            else:
                print(monstie.name+", ",end="")
            return monstie.name




def fight(monster1,monster2,suspense = False):
    if not monster1.alive or not monster2.alive:
        print("You forgot to refresh")
        return
    while True:
        if suspense:
            time.sleep(2)
        print(monster1.name,"vs",monster2.name)
        monster1.show()
        monster2.show()
        monster2.damage(monster1.hit())
        if not monster2.alive:
            break
        monster1.damage(monster2.hit())
        if not monster1.alive:
            break
    print()
    if monster1.alive:
        print("the victor is", monster1.name)
        monster1.show()
        return monster1.name
    else:
        print("the victor is", monster2.name)
        monster2.show()
        return monster2.name
# Do some experimentation now & run the code as needed to check:
    # How many zombies does it take to beat a troll?
        # Trolls have 84 HP and do 28 damage.
    # (yes, there is some randomness, but 3 is not enough.)


# Practice problem 3:
# Go back up to the generic monster class. Copy and paste it here.
# Change the class name to "rollingMonster".
# We need to add two data values:
    # Attack bonus (name it whatever you want)
    # Armor class (name it watever you want)
# Both of these data values will need to be passed as
        # arguments to the class in __init__()

# You should *also* make a new method called "attack."
# This method will simply roll a d20 and add the monster's attack bonus.
# Write the class here
class rollingMonster:
    # any monster with HP, a damage die, and damage bonus
    def __init__(self,HP,damageDie,damageBonus,attackBonus,AC,name="rolling monster"):
        self.maxHP = HP
        self.curHP = HP
        self.damageDie = damageDie
        self.damageBonus = damageBonus
        self.alive = True
        self.name = name
        self.AC = AC
        self.attackBonus = attackBonus
        return # You don't have to put the return here
    def show(self):
        print()
        print(self.name, "stats")
        print(self.curHP,"/",self.maxHP)
        print(self.damageBonus,"+",self.damageDie.name)
    def hit(self): # dealing damage
        damage = self.damageBonus + self.damageDie.roll()
        return damage
    def damage(self,damage): # taking damage
        self.curHP -= damage
        if self.curHP <= 0:
            self.curHP = 0
            self.alive = False
        return
    def attack(self): # rolling to hit
        attackRoll = self.attackBonus + Die(20).roll()
        return attackRoll
    def refresh(self):
        self.curHP = self.maxHP
        self.alive = True


# Also, go ahead and initialize a rolling zombie:
    # HP 22
    # Damage 1+1d6
    # Attack bonus +3
    # Armor class 8
# And a rolling skelton:
    # HP 15
    # Damage 2+1d6
    # Attack bonus +4
    # Armor class 13
rollzombie1 = rollingMonster(22,Die(6),1,3,8,name="zombie")
rollskeleton = rollingMonster(15,Die(6),2,4,13,name="skeleton")
rollzombie2 = rollzombie1
rollzombie3 = rollzombie1
rollzombie4 = rollzombie1
rollzombie5 = rollzombie1
rollzombie6 = rollzombie1
rollzombie7 = rollzombie1
rollzombie8 = rollzombie1
horderoll = [rollzombie1,rollzombie2,rollzombie3,rollzombie4,rollzombie5,rollzombie6,rollzombie7]


# Practice problem 4:
# Remember that "fight" function that we made in class?
# We're going to make yet another similar function called "fightRoll"
# It takes the same structure of arguments that the one in class takes,
# Except these monsters must both be rolling monsters.
# This function will add the iconic step of D&D combat into the mix:
    # A monster will first roll.
    # If the monster's attack score is >= the opponent's Armor Class:
        # Then do damage
    # Otherwise
        # No damage is dealt.
    # Action passes to the other monster
    # Repeat until we have a winner
# Write that function here
def fightRoll(monster1,monster2,suspense = False):
    if not monster1.alive or not monster2.alive:
        print("You forgot to refresh")
        return
    while True:
        if suspense:
            time.sleep(2)
        print(monster1.name,"vs",monster2.name)
        monster1.show()
        monster2.show()
        if monster1.attack() >= monster2.AC:
            monster2.damage(monster1.hit())
        if not monster2.alive:
            break
        if monster2.attack() >= monster1.AC:
            monster1.damage(monster2.hit())
        if not monster1.alive:
               break
    print()
    if monster1.alive:
        print("the victor is", monster1.name)
        monster1.show()
        return monster1.name
    else:
        print("the victor is", monster2.name)
        monster2.show()
        return monster2.name


# Go ahead and fight a zombie and a skeleton again.
# Let the skeleton go first. Is it still a zombie win every time?
# naw the skele wins sometimes

# Practice problem 5:
# Let's bring it all together: make a function called "fightManyRoll"
# That allows a single rolling monster to fight many rolling monsters.
# Go ahead and make a "rollingTroll" monster too (AC of 15, +7 to hit)
# write it here and set a troll up in a fight with a bunch of zombies.
# How many zombies does it take to win now?
def fightManyRoll(monster1,listofmonster,suspense = False):
    if not monster1.alive:
        print("You forgot to refresh")
        return
    for monstie in listofmonster:
        if not monstie.alive:
            print("You forgot to refresh")
            return
    while True:
        if suspense:
            time.sleep(1)
        print(monster1.name,end=" ")
        print("vs",end=" ")
        i=0
        for monstie in listofmonster:
            i+=1
            if i == len(listofmonster):
                print("and "+monstie.name,end="")
            else:
                print(monstie.name+", ",end="")
        print()
        monster1.show()
        for monstie in listofmonster:
            monstie.show()
        for monstie in listofmonster:
            if monstie.alive:
                if monstie.attack() >= monster1.AC:
                    monster1.damage(monstie.hit())
        if not monster1.alive:
            break
        ready = True
        for monstie in listofmonster:
            if monstie.alive and ready:
                if monster1.attack() >= monstie.AC:
                    monstie.damage(monster1.hit())
                    ready = False
        i=0
        for monstie in listofmonster:
            if not monstie.alive:
                i+=1
        if i == len(listofmonster):
            break
                
    print()
    if monster1.alive:
        print("the victor is", monster1.name)
        monster1.show()
        return monster1.name
    else:
        print("the victor is ",end="")
        i=0
        for monstie in listofmonster:
            i+=1
            if i == len(listofmonster):
                print("and "+monstie.name,end="")
            else:
                print(monstie.name+", ",end="")
            return monstie.name
        
class trollRoll:
    # any monster with HP, a damage die, and damage bonus
    def __init__(self):
        self.maxHP = 84
        self.curHP = 84
        self.damageDie = Dice([Die(6),Die(6),Die(6),Die(6)])
        self.damageBonus = 10
        self.alive = True
        self.name = "Troll"
        self.regenDie = Die(20)
        self.AC = 15
        self.attackBonus = 7
        return 
    def show(self):
        print()
        print(self.name, "stats")
        print(self.curHP,"/",self.maxHP)
        print(self.damageBonus,"+",self.damageDie.name)
    def regen(self):
        if self.alive:
            self.curHP += self.regenDie.roll()
            if self.curHP > self.maxHP:
                self.curHP = self.maxHP
    def hit(self): # dealing damage
        damage = self.damageBonus + self.damageDie.roll()
        self.regen() # This is exclusively so it fits in our fight function.
        return damage
    def damage(self,damage): # taking damage
        self.curHP -= damage
        if self.curHP <= 0:
            self.curHP = 0
            self.alive = False
        return
    def refresh(self):
        self.curHP = self.maxHP
        self.alive = True
    def attack(self): # rolling to hit
        attackRoll = self.attackBonus + Die(20).roll()
        return attackRoll
trolol = trollRoll()