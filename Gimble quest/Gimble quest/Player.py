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

    def attack(self, damage, StaminaLoss):
        self.stamina -= StaminaLoss
        print(f"You did {damage} damage")
        print(f"-{StaminaLoss} stamina")

    def QuickRest(self):
        if self.stamina < 100:
            StaminaGain = 100 - self.stamina
            self.stamina = StaminaGain
            return StaminaGain
        if self.stamina > 100:
            self.stamina = 100

    def TakeDamage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0

            ToolBox.space()
            ToolBox.line()
            print(f"{self.name} has fallen")

    def PlayerInfo(self, TypeClass):
        ToolBox.space()

        print("Player Info: ")

        ToolBox.line()

        print(f"Name: {self.name}")
        print(f"Class: {TypeClass.name}")
        print(f"Health: {self.health}")
        print(f"Stamina: {self.stamina}")

#fighter SubClass with all abilitys
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

    def Slash(self, enemy, character):
        if character.stamina >= 25:
            ToolBox.space()
            ToolBox.line()
            print("You slash towards the enemy")
            character.attack(15, 25)
            enemy.takeDamage(15)
        else:
            print("You go to slash the enemy but fail due to lack of stamina")

    def DoubleSlash(self, enemy, character):
        if character.stamina >= 35:
            ToolBox.space()
            ToolBox.line()
            print("You slash towards the enemy twice")
            character.attack(25, 35)
            enemy.takeDamage(25)
        else:
            print("You go for a double slash but fail due to lack of stamina")
#mage SubClass with all abilitys
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

    def FireBreath(self, enemy, character):
        if character.stamina >= 20:
            ToolBox.space()
            ToolBox.line()
            print("You blow fire towards the enemy")
            character.attack(15, 20)
            enemy.takeDamage(15)
        else:
            print("You take a deep breath before coughing due to lack of stamina")

    def SparkBolt(self, enemy, character):
        if character.stamina >= 30:
            ToolBox.space()
            ToolBox.line()
            print("You shoot a lightning projectile towards the enemy")
            character.attack(25, 30)
            enemy.takeDamage(25)
        else:
            print("You ready your attack but nothing happens due to lack of stamina")

    def FireBall(self, enemy, character):
        if character.stamina >= 50:
            ToolBox.space()
            ToolBox.line()
            print("You shoot a fire ball towards the enemy")
            character.attack(40, 50)
            enemy.takeDamage(40)
        else:
            print("You ready your attack but nothing happens due to lack of stamina")
#ranger SubClass with all abilitys
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

    def Arrow(self, enemy, character):
        if character.stamina >= 15:
            ToolBox.space()
            ToolBox.line()
            print("You shoot a arrow towards the enemy")
            character.attack(10, 15)
            enemy.takeDamage(10)
        else:
            print("You try to shoot your bow but fail due to lack of stamina")

    def ChargeShot(self, enemy, character):
        if character.stamina >= 30:
            ToolBox.space()
            ToolBox.line()
            print("You shoot a charged arrow towards the enemy")
            character.attack(20, 30)
            enemy.takeDamage(20)
        else:
            print("You try to shoot your bow but fail due to lack of stamina")
