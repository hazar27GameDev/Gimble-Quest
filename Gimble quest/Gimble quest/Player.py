from calendar import c
import ToolBox

"""
Module: Player.py
Author: Harry Imre
Date: 16/06/2026
Purpose: Stores the Player class.
Parameters: None
Returns: None
"""

class Player:

    """
    Represents an Player.
    Author: Harry Imre
    Date: 16/06/2026
    Parameters: none
    Returns: Player object
    """

    def __init__(self, name, health, stamina):
        self.name = name
        self.health = health
        self.stamina = stamina

    def attack(damage):
        print(f"You did {damage} damage")

    def TakeDamage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
            print(f"{self.name} has fallen")

    def PlayerInfo(self, TypeClass):
        ToolBox.space()

        print("Player Info: ")

        ToolBox.line()

        print(f"Name: {self.name}")
        print(f"Class: {TypeClass.name}")
        print(f"Health: {self.health}")
        print(f"Stamina: {self.stamina}")


class Fighter:
    """
    Represents Class type.
    Author: Harry Imre
    Date: 26/06/2026
    Parameters: none
    Returns: Player object
    """
    def __init__(self, name):
        self.name = name

    def slash(self):
        ToolBox.space()
        ToolBox.line()
        print("You slash towards the enemy")
        Player.attack(15)

class Mage:
    """
    Represents Class type.
    Author: Harry Imre
    Date: 26/06/2026
    Parameters: none
    Returns: Player object
    """
    def __init__(self, name):
        self.name = name

    def FireBall(self):
        ToolBox.space()
        ToolBox.line()
        print("You shoot a fire ball towards the enemy")
        Player.attack(20)

class Ranger:
    """
    Represents Class type.
    Author: Harry Imre
    Date: 26/06/2026
    Parameters: none
    Returns: Player object
    """
    def __init__(self, name):
        self.name = name

    def Arrow(self):
        ToolBox.space()
        ToolBox.line()
        print("You shoot a arrow towards the enemy")
        Player.attack(10)

