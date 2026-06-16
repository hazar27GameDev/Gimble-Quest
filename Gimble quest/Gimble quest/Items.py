class item:
    def __init__(self, items, damage, heal, armor):
        self.items = items
        self.damage = damage
        self.heal = heal
        self.armor = armor

    def AddHeal(self):
        self.heal = 10

    def AddArmor(self):
        self.armor = 5

    def AddDamage(self):
        self.damage = 2
