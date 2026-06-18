import ToolBox

class Player:

    def __init__(self, name, health, stamina):
        self.name = name
        self.health = health
        self.stamina = stamina

    def attack():
        print("Your attacking")

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
        print(f"Class: {TypeClass.ClassType}")
        print(f"Health: {self.health}")
        print(f"Stamina: {self.stamina}")


class ClassType:
    def __init__(self, ClassType):
        self.ClassType = ClassType
