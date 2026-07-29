import ToolBox # Use of tools like lines making the prosess of creating code faster and efficent
from Player import *

class item:
    def __init__(self, name, ItemAmount, heal):
        self.name = name
        self.ItemAmount = ItemAmount
        self.heal = heal

    def AddHeal(self, ItemAmount, HealAmount):
        Player.health += HealAmount
        self.ItemAmount -= 1
        print(f"You decide to drink a {self.name}")

#small pot yes
class SmallHealthPotion(item):
    def __init__(self):
        super().__init__("Small Health Potion", 5, 25)

#huge pot yes but yes
class HugeHealthPotion(item):
    def __init__(self):
        super().__init__("Huge Health Potion", 2, 50)
    