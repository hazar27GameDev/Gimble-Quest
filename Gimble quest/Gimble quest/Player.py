class Player:

    def __init__(self, name, ClassType, health, stamina):
        self.name = name
        self.ClassType = ClassType
        self.health = health
        self.stamina = stamina

    def PlayerInfo(self):

        print("Player Info: ")
        print(f"Name: {self.name}")
        print(f"Class: {self.ClassType}")
        print(f"Health: {self.health}")
        print(f"Stamina: {self.stamina}")
