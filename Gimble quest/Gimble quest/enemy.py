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

    def __init__ (self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        #self.defence = defence


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
        ToolBox.space()

        print("Enemy Info: ")

        ToolBox.line()

        print(f"Type: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        #print(f"Defence: {self.defence})



class Bandit(Enemy):

    """
    Represents a Bandit Inherited from Enemy.
    Author: Kobi Nichols
    Date: 22/06/2026
    Parameters: none
    Returns: Enemy object
    """

    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def attack(self, attack):
        self.attack = attack
        print(f"{self.name} attacks with {self.attack} damage")




class Slime(Enemy):

    """
    Represents a Slime Inherited from Enemy.
    Author: Kobi Nichols
    Date: 25/06/2026
    Parameters: none
    Returns: Enemy object
    """

    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)


class Dragon(Enemy):
    """
    Represents a Dragon Inherited from Enemy.
    Author: Kobi Nichols
    Date: 25/06/2026
    Parameters: none
    Returns: Enemy object
    """

    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)





