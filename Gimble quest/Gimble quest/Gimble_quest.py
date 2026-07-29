import random
import ToolBox
import Player
import enemy
import InventoryClass

EnemyStunTurn = 0

Bandit = enemy.Bandit("Bandit", 50, 20)
Slime = enemy.Slime("Slime", 30, 15)
Goblin = enemy.Goblin("Goblin", 50, 25)
Ogre = enemy.Ogre("Ogre", 100, 35)

Dragon = enemy.Dragon("Dragon", 500, 100)

EnemyPool = [Bandit, Slime, Goblin, Ogre]

SmallPotion = InventoryClass.Potion("Small health potion", 25)
BigPotion = InventoryClass.Potion("Big health potion", 50)

ItemPool = [SmallPotion, BigPotion]

#Main menu
def MainMenu():
    print("Welcome to Gimble Quest")

    ToolBox.line()
    ToolBox.space()

    print("This is a tuff RPG made by the epic people named Harry, Kobi, and Jacobi - here in spirit")

    ToolBox.line()
    ToolBox.space()

#creats the character 
def CharacterCreator():
    print("Character Creator: ")

    ToolBox.space()

    UserName = input("Enter you name: ")
    class_type = ""
    health = 100


    ToolBox.space()

    while True:
        print("Choice your class: ")
        ToolBox.line()
    
        print("A. Fighter - 100MAX HP")
        print("B. Mage - 50MAX HP")
        print("C. Ranger - 75MAX HP")

        ToolBox.space()
        UserChoice = input("Enter option: ")

        picked = False
        match UserChoice.upper():
            case "A":
                picked = True
                print("You picked Fighter")
                class_type = Player.Fighter("Fighter")
                health = 100
                break
            case "B":
                picked = True
                print("You picked Mage")
                class_type = Player.Mage("Mage")
                health = 50
                break
            case "C":
                picked = True
                print("You picked Ranger")
                class_type = Player.Ranger("Ranger")
                health = 75
                break
            case _:
                print("Invalid option: Please try again")
        if picked == True:
            break
    return UserName, health, class_type

#allows the enemy to make actions
def EnemyAction(EnemyType):
    global EnemyStunTurn
    if EnemyStunTurn <= 0:
        if EnemyType.name != "Dragon":
            if EnemyType.attack >= 25:
                action = random.randint(1, 3)
            elif EnemyType.attack <= 50:
                action = random.randint(1, 4)
            else:
                action = random.randint(1, 5)

            if action == 1:
                ToolBox.space()
                ToolBox.line()
                print(f"{EnemyType.name} moves back too rest")
            elif action == 2:
                damage = EnemyType.LightAttack()
                Character.TakeDamage(damage)

                ToolBox.space()
            elif action == 3:
                damage = EnemyType.HeavyAttack()
                Character.TakeDamage(damage)
            elif action == 4:
                damage = EnemyType.StunAttack()
                Character.TakeDamage(damage)
                EnemyStunTurn = 1
            elif action == 5:
                damage = EnemyType.BigStunAttack()
                Character.TakeDamage(damage)
                EnemyStunTurn = 1

                ToolBox.space()
        elif EnemyType.name == "Dragon":
            if EnemyType.health >= 250:
                action = random.randint(1, 4)
            else:
                action = random.randint(1, 7)

            if action == 1:
                ToolBox.space()
                ToolBox.line()
                print(f"The {EnemyType.name} flys back too rest")
            elif action == 2:
                damage = EnemyType.LightAttack()
                Character.TakeDamage(damage)

                ToolBox.space()
            elif action == 3:
                damage = EnemyType.TailCleaver()
                Character.TakeDamage(damage)

                ToolBox.space()
            elif action == 4:
                damage = EnemyType.HeavyAttack()
                Character.TakeDamage(damage)
                EnemyStunTurn = 1

                ToolBox.space()
            elif action == 5:
                damage = EnemyType.FireBreath()
                Character.TakeDamage(damage)
                EnemyStunTurn = 1

                ToolBox.space()
            elif action == 6:
                damage = EnemyType.FireHeal()
                EnemyStunTurn = 2

                ToolBox.space()
            elif action == 7:
                damage = EnemyType.FireBall()
                Character.TakeDamage(damage)
                EnemyStunTurn = 2

                ToolBox.space()
    else:
        EnemyStunTurn = EnemyStunTurn - 1
        print(f"The {EnemyType.name} is stunned (stuned for {EnemyStunTurn} turns left)")

#player choice 
def interaction(enemy):
    ToolBox.space()

    print(f"A {enemy.name} approaches you")

    ToolBox.line()

    print("What do you do")
    
    enemy.enemyInfo()

    while True:
        EndTurn = False

        ToolBox.line()
    
        print("A. Action")
        print("B. Use item")
        print("C. Display player info")

        ToolBox.space()
        while True:
            UserChoice = input("Enter option: ")

            match UserChoice.upper():
                case "A":
                    EndTurn = True
                    print("You decide to take an action")
                    ToolBox.space()

                    print("A. Attack")
                    print("B. Rest")

                    Action = input("Enter choice: ")
                    match Action.upper():
                        case "A":
                            match TypeClass.name:
                                case "Fighter":
                                    ToolBox.space()

                                    print("A. Slash - 15HP, 25SP")
                                    print("B. Double slash - 25HP, 35SP")

                                    Attack = input("Enter choice: ")

                                    match Attack.upper():
                                        case "A":
                                            TypeClass.Slash(enemy, Character)
                                            break
                                        case "B":
                                            TypeClass.DoubleSlash(enemy, Character)
                                            break

                                case "Mage":
                                    ToolBox.space()

                                    print("A. Fire breath - 15HP, 20SP")
                                    print("B. Spark bolt - 25HP, 30SP")
                                    print("C. FireBall - 50HP, 50SP")

                                    Attack = input("Enter choice: ")

                                    match Attack.upper():
                                        case "A":
                                            TypeClass.FireBreath(enemy, Character)
                                            break

                                        case "B":
                                            TypeClass.SparkBolt(enemy, Character)
                                            break

                                        case "C":
                                            TypeClass.FireBall(enemy, Character)
                                            break

                                case "Ranger":
                                    ToolBox.space()

                                    print("A. Arrow - 10HP, 15SP")
                                    print("B. Charge shot - 20HP, 30SP")

                                    Attack = input("Enter choice: ")

                                    match Attack.upper():
                                        case "A":
                                            TypeClass.Arrow(enemy, Character)
                                            break
                                        case "B":
                                            TypeClass.ChargeShot(enemy, Character)
                                            break

                            break
                        case "B":
                            print(f"You stand still and rest")
                            
                            break
                        case _:
                            print("Invalid option: Please try again")
                case "B":
                    EndTurn = False
                    print("You decide to use a item")

                    ToolBox.space()

                    counts = {"Small health potion": 0, "Big health potion": 0}

                    for item in Bag.items:
                        counts[item.name] += 1


                    small = counts["Small health potion"]
                    big = counts["Big health potion"]

                    print(f"A. Small Health Potion +25HP {small} left")
                    print(f"B. Big Health Potion +50HP {big} left")


                    Action = input("Enter choice: ")
                    match Action.upper():
                        case "A":
                            pass
                            Bag.use_item("Small health potion", Character)
                        case "B":
                            pass
                            Bag.use_item("Big health potion", Character)
                        case _:
                            print("Invalid option: Please try again")

                    break
                case "C":
                    print("You decide to check your states")
                    Character.PlayerInfo(TypeClass)
                    break
                case _:
                    print("Invalid option: Please try again")
        if EndTurn == True:
            enemy.enemyInfo()
            if enemy.health < 1:
                ToolBox.space()
                ToolBox.line()

                print(f"You defeated the {enemy.name}")

                break
            else:
                EnemyAction(enemy)
                if Character.health <= 0:
                    break


#MainMenu call dahhh
MainMenu()

#character creator
info = CharacterCreator()

UserName = info[0]
ClassType = info[2]
health = info[1]
MaxHealth = info[1]
stamina = 100

Character = Player.Player(UserName, health, MaxHealth, stamina)
TypeClass = ClassType
Bag = InventoryClass.Inventory()

Bag.add_item(SmallPotion)

#Bag.use_item("Small health potion", Character)

Character.PlayerInfo(TypeClass)

ToolBox.space()
ToolBox.line()
input("Click Enter to begin: ")

for i in range(4):
    enemy = random.choice(EnemyPool)
    EnemyPool.remove(enemy)

    interaction(enemy)

    ToolBox.space()
    ToolBox.line()

    print("You founded an item!")
    Bag.add_item(random.choice(ItemPool))

interaction(Dragon)
