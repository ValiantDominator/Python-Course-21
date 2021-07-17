# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:04:20 2021

@author: Daniel Mishler
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
    def advantage(self):
        result = max(self.roll(),self.roll())
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

class rollingMonster:
    # any monster with HP, a damage die, and damage bonus
    def __init__(self,HP,damageDie,damageBonus,attackBonus,AC,dexmod=0,name="generic monster"):
        self.maxHP = HP
        self.curHP = HP
        self.damageDie = damageDie
        self.damageBonus = damageBonus
        self.alive = True
        self.attackBonus = attackBonus
        self.AC = AC
        self.name = name
        self.D20 = Die(20)
        self.dexmod = dexmod
        return # You don't have to put the return here
    def show(self):
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
    def attack(self):
        attackRoll = self.D20.roll() + self.attackBonus
        return attackRoll
    def refresh(self):
        self.curHP = self.maxHP
        self.alive = True
    def initiative(self):
        return self.D20.roll() + self.dexmod


class Troll:
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

class rollingTroll:
    def __init__(self):
        self.maxHP = 84
        self.curHP = 84
        self.damageDie = Dice([Die(6),Die(6),Die(6),Die(6)])
        self.damageBonus = 10
        self.alive = True
        self.AC = 15
        self.attackBonus = 7
        self.name = "Troll"
        self.regenDie = Die(20)
        self.D20 = Die(20)
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
    def attack(self):
        attackRoll = self.D20.roll() + self.attackBonus
        return attackRoll
    def damage(self,damage): # taking damage
        self.curHP -= damage
        if self.curHP <= 0:
            self.curHP = 0
            self.alive = False
        return
    def refresh(self):
        self.curHP = self.maxHP
        self.alive = True


def fight(monster1,monster2,suspense = False,printing = True):
    if not monster1.alive or not monster2.alive:
        print("You forgot to refresh")
        return
    while True:
        if suspense:
            time.sleep(2)
        if printing:
            print(monster1.name,"vs",monster2.name)
            monster1.show()
            monster2.show()
        monster2.damage(monster1.hit())
        if not monster2.alive:
            break
        monster1.damage(monster2.hit())
        if not monster1.alive:
            break
    if printing:
        print()
    if monster1.alive:
        if printing:
            print("the victor is", monster1.name)
            monster1.show()
        return monster1.name
    else:
        if printing:
            print("the victor is", monster2.name)
            monster2.show()
        return monster2.name

def fightManyRoll(soloMonster,group,suspense = False,printing = True):
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
        return soloMonster.name
    else:
        if printing:
            print("the victor is", "the monster group")
            for monster in group:
                monster.show()
        return "group"


print("utils loaded successfully!")