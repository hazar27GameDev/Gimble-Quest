import ToolBox # Use of tools like lines making the prosess of creating code faster and efficent
from Player import *

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.name} to inventory.")

    def use_item(self, item_name, player):
        for item in self.items:
            if item.name == item_name:
                print(f"You decide to use a {item.name}")
                item.use(player)
                self.items.remove(item)
                return
            print("Potion not found in inventory!")

class Potion:

  def __init__(self, name, healing_amount):
    self.name = name
    self.healing_amount = healing_amount

  def use(self, player):
      math = min(player.health + self.healing_amount, player.MaxHealth) - player.health
      player.health = min(player.health + self.healing_amount, player.MaxHealth)
      print(f"+{math} Health")
    