import ToolBox # Use of tools like lines making the prosess of creating code faster and efficent
from Player import *

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

    # Attacks the player and returns the damage dealt
    #def attackPlayer(self, player):
        #damage = self.attack - player.defence
        #if damage < 0:
            #damage = 0
        #player.takeDamage(damage)
        #return damage

    # Displays the enemy's information
    def enemyInfo(self):
        ToolBox.space()

        print("Enemy Info: ")

        ToolBox.line()

        print(f"Type: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack power: {self.attack}")
        #print(f"Defence: {self.defence})



class Bandit(Enemy):

    """
    Represents a Bandit Inherited from Enemy.
    Author: Kobi Nichols
    Date: 22/06/2026
    Parameters: none
    Returns: Enemy object
    """
    
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    # The banits specific attack
    def LightAttack(self):
        ToolBox.space()
        ToolBox.line()

        print(f"The Bandit throws a knife towards you -{15} health")
        return 15
        
    def HeavyAttack(self):
        ToolBox.space()
        ToolBox.line()

        print(f"The Bandit slash towards you -{25} health")
        return 25


class Slime(Enemy):

    """
    Represents a Bandit Inherited from Enemy.
    Author: Kobi Nichols
    Date: 22/06/2026
    Parameters: none
    Returns: Enemy object
    """
    
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    # The slime specific attack
    def LightAttack(self):
        ToolBox.space()
        ToolBox.line()

        print(f"The Slime shoot sludge at you -{10} health")
        return 10
        
    def HeavyAttack(self):
        ToolBox.space()
        ToolBox.line()

        print(f"The Slime lunges at you -{20} health")
        return 20


class Dragon(Enemy):

    """
    Represents a Dragon Inherited from Enemy.
    Author: Harry Imre
    Date: 28/07/2026
    Parameters: none
    Returns: Enemy object
    """
    
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    # The dragon specific attack
    def LightAttack(self):
        ToolBox.space()
        ToolBox.line()

        print(f"The Dragon slashes towards you -{20} health")
        return 20
        
    def HeavyAttack(self):
        ToolBox.space()
        ToolBox.line()

        print(f"The Dragon thrust down with a double‑claw slash -{35} health")
        print("The attack creates a crater around you")
        print("\nThe dragon looks stunned")
        return 35

    def TailCleaver(self):
        ToolBox.space()
        ToolBox.line()

        print(f"The Dragon swips its tail towards you -{15} health")
        return 15

    def FireBreath(self):
        ToolBox.space()
        ToolBox.line()

        print(f"The Dragon blows fire towards you -{35} health")
        print("The fire engulfs all around you")
        print("In doing that the dragon is stunned")
        return 35

    def FireHeal(self):
        ToolBox.space()
        ToolBox.line()
        
        if self.health <= 250:
            self.health += 50
        print(f"The dragon engulfs itself in flames +50 health")
        print(f"The dragon now has {self.health} health")
        print("In doing that the dragon is stunned")

    def FireBall(self):
        ToolBox.space()
        ToolBox.line()

        print("The dragon charges a huge ball of fire before")
        print(f"Sudenly exploding -{45} health")
        print("Strands of fire falls down to the earth")
        print("\n The attack leaves the dragon stunned")
        return 45




