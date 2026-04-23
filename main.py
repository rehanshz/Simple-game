
from dice_roll import diceroll
from rock_paper_scissor import rockpaperscissor

while True:
    print("""
=====WELCOME TO GAME STATION=====
MAIN MENU :
      1. DICE ROLL 
      2. ROCK PAPER SCISSOR
      3. EXIT

""")
    ch =int(input("Which Game would You like to play : "))
    if ch==1:
        diceroll()
    elif ch==2:
        rockpaperscissor()
    elif ch==3:
        print("Thanks for using gamestation ")
        break
    else:
        print("sorry invalid input")


