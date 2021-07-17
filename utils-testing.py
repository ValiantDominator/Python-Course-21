# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:14:30 2021

@author: Daniel Mishler
"""

import utils

zombies = []

for i in range(12):
    zombies.append(
        utils.rollingMonster(22, #HP
                             utils.Die(6),              # Damage Die
                             1,                         # Damage bonus
                             3,                         # Attack bonus
                             8,                         # Armor Class
                             "zombie {}".format(i+1)    # Name
        )
    )
# for zombie in zombies:
#     zombie.show()



troll = utils.rollingTroll()

# utils.fightManyRoll(troll,zombies,suspense=False,printing=True)
# troll.refresh()
# for zombie in zombies:
#     zombie.refresh()

trollWins = 0
for i in range(1000):
    victor = utils.fightManyRoll(troll,zombies,suspense=False,printing=False)
    troll.refresh()
    for zombie in zombies:
        zombie.refresh()
    if victor == "Troll":
        trollWins += 1

print("the troll is expected to win", trollWins, "out of 1000")