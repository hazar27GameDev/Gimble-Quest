class Enemy():
    def __init__ (self, name, health, attack, defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence

    def takeDamage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def isAlive(self):
        return self.health > 0


    def attackPlayer(self, player):
        damage = self.attack - player.defence
        if damage < 0:
            damage = 0
        player.takeDamage(damage)
        return damage
    
   




