import ToolBox
import Player

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
                class_type = "Fighter"
                health = 100
                break
            case "B":
                picked = True
                print("You picked Mage")
                class_type = "Mage"
                health = 50
                break
            case "C":
                picked = True
                print("You picked Ranger")
                class_type = "Ranger"
                health = 75
                break
        if picked == True:
            break
    return UserName, health, class_type

#MainMenu call dahhh
MainMenu()

#character creator
info = CharacterCreator()

UserName = info[0]
ClassType = info[2]
health = info[1]
stamina = 100

Character = Player.Player(UserName, health, stamina)
TypeClass = Player.ClassType(ClassType)
Character.PlayerInfo(TypeClass)