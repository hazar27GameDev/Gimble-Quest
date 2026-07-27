import random
import ToolBox
import Player
import enemy

Bandit = enemy.Bandit("Bandit", 50, 25)

#Main menu
def MainMenu():
    print("Welcome to Epic RPG Game")

    ToolBox.line()
    ToolBox.space()

    print("This is a tuff RPG made by the epic people named Harry, Kobi, and Jacobi")

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
    
        print("A. Fighter - 100HP")
        print("B. Mage - 50HP")
        print("C. Ranger - 75HP")

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

def EnemyAction(EnemyType):
    action = random.randint(1, 3)

    if action == 1:
        print("block")
    else:
        damage = EnemyType.EnemyAttack()
        Character.TakeDamage(damage)

        ToolBox.space()

#interactions
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
        UserChoice = input("Enter option: ")

        while True:
            match UserChoice.upper():
                case "A":
                    EndTurn = True
                    print("You decide to attack")
                    ToolBox.space()

                    print("A. Attack")
                    print("B. Block")

                    Action = input("Enter choice: ")
                    match TypeClass.name:
                        case "Fighter":
                            ToolBox.space()

                            print("A. Slash - 15HP, 10SP")
                            print("B. Double slash - 25HP, 20SP")

                            Attack = input("Enter choice: ")

                            match Attack.upper():
                                case "A":
                                    TypeClass.Slash(enemy)
                                    break
                                case "B":
                                    TypeClass.DoubleSlash(enemy)
                                    break

                        case "Mage":
                            ToolBox.space()

                            print("A. Fire breath - 10HP, 10SP")
                            print("B. Spark bolt - 15HP, 20SP")
                            print("C. FireBall - 30HP, 30SP")

                            Attack = input("Enter choice: ")

                            match Attack.upper():
                                case "A":
                                    TypeClass.FireBreath(enemy)
                                    break

                                case "B":
                                    TypeClass.SparkBolt(enemy)
                                    break

                                case "C":
                                    TypeClass.FireBall(enemy)
                                    break

                        case "Ranger":
                            ToolBox.space()

                            print("A. Arrow - 10HP, 5SP")
                            print("B. Charge shot - 20HP, 15SP")

                            Attack = input("Enter choice: ")

                            match Attack.upper():
                                case "A":
                                    TypeClass.Arrow(enemy)
                                    break
                                case "B":
                                    TypeClass.ChargeShot(enemy)
                                    break

                    break
                case "B":
                    EndTurn = True
                    print("You decide to use a item")
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


#MainMenu call dahhh
MainMenu()

#character creator
info = CharacterCreator()

UserName = info[0]
ClassType = info[2]
health = info[1]
stamina = 100

Character = Player.Player(UserName, health, stamina)
TypeClass = ClassType
Character.PlayerInfo(TypeClass)

ToolBox.space()
ToolBox.line()
input("Click Enter to begin: ")

interaction(Bandit)
