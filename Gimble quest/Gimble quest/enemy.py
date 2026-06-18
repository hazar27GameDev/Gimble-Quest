import ToolBox # Use of tools like lines making the prosess of creating code faster and efficent

"""
Module: Enemy.py
Author: Kobi Nichols
Date: 16/06/2026
Purpose: Stores the Enemy class.
Parameters: None
Returns: None
"""

class Enemy():

    """
    Represents an enemy.
    Author: Kobi Nichols
    Date: 16/06/2026
    Parameters: none
    Returns: Enemy object
    """

    def __init__ (self, name, health, attack, defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence


    # If the enemy takes damage, this function will be called to reduce the health of the enemy
    def takeDamage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    # Checks if the enemy is still alive 
    def isAlive(self):
        return self.health > 0

    # Attacks the player and returns the damage dealt
    def attackPlayer(self, player):
        damage = self.attack - player.defence
        if damage < 0:
            damage = 0
        player.takeDamage(damage)
        return damage

    # Displays the enemy's information
    def enemyInfo(self):
        print("Enemy " + self.name + " Info")

        ToolBox.line

        print("Health: " + str(self.health))
        print("Attack: " + str(self.attack))
        print("Defence: " + str(self.defence))



