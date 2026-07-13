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

    def attack(damage, stamina):
        print(f"You did {damage} damage")
        print(f"-{stamina} stamina")

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
    Parameters: Fighter
    Returns: Player object
    """
    def __init__(self, name):
        self.name = name

    def Slash(self, enemy):
        ToolBox.space()
        ToolBox.line()
        print("You slash towards the enemy")
        Player.attack(15, 10)
        enemy.takeDamage(15)

    def DoubleSlash(self, enemy):
        ToolBox.space()
        ToolBox.line()
        print("You slash towards the enemy twice")
        Player.attack(25, 20)
        enemy.takeDamage(25)

class Mage:
    """
    Represents Class type.
    Author: Harry Imre
    Date: 26/06/2026
    Parameters: Mage
    Returns: Player object
    """
    def __init__(self, name):
        self.name = name

    def FireBreath(self, enemy):
        ToolBox.space()
        ToolBox.line()
        print("You blow fire towards the enemy")
        Player.attack(10, 10)
        enemy.takeDamage(10)

    def SparkBolt(self, enemy):
        ToolBox.space()
        ToolBox.line()
        print("You shoot a lightning projectile towards the enemy")
        Player.attack(15, 20)
        enemy.takeDamage(15)

    def FireBall(self, enemy):
        ToolBox.space()
        ToolBox.line()
        print("You shoot a fire ball towards the enemy")
        Player.attack(30, 30)
        enemy.takeDamage(30)

class Ranger:
    """
    Represents Class type.
    Author: Harry Imre
    Date: 26/06/2026
    Parameters: Ranger
    Returns: Player object
    """
    def __init__(self, name):
        self.name = name

    def Arrow(self, enemy):
        ToolBox.space()
        ToolBox.line()
        print("You shoot a arrow towards the enemy")
        Player.attack(10, 5)
        enemy.takeDamage(10)

    def ChargeShot(self, enemy):
        ToolBox.space()
        ToolBox.line()
        print("You shoot a charged arrow towards the enemy")
        Player.attack(20, 15)
        enemy.takeDamage(20)
