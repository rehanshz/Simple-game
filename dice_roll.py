from random import randint
def diceroll():
    while True:
        print("""
==========DICE ROLL SLOT=============
    ____  _            ____       ____
   / __ \(_)________  / __ \___  / / /
  / / / / / ___/ __ \/ /_/ / _ \/ / / 
 / /_/ / / /__/ /___  _, _/ /_// / /
/_____/_/\___/\____/_/ |_|\___/_/_/   """)

        print("""
Do You Want TO roll a DICE """)
        ch=input("enter your choice (yes/no): ")
        if ch.lower()=="yes":
            print("....rolling🎲......")
            roll=randint(1,6)
            print(f"puffff.......")
            print(f"You have rolled ✨{roll}✨")

        elif ch.lower()=="no":
            print("Thanks for using Dice roll")
            break
        else:
            print("Sorry invalid  input")


    




# another logic i thought of doing with more visual output


#     dice_1 = """
# +-------+
# |       |
# |   o   |
# |       |
# +-------+
# """

# dice_2 = """
# +-------+
# | o     |
# |       |
# |     o |
# +-------+
# """

# dice_3 = """
# +-------+
# | o     |
# |   o   |
# |     o |
# +-------+
# """

# dice_4 = """
# +-------+
# | o   o |
# |       |
# | o   o |
# +-------+
# """

# dice_5 = """
# +-------+
# | o   o |
# |   o   |
# | o   o |
# +-------+
# """

# dice_6 = """
# +-------+
# | o   o |
# | o   o |
# | o   o |
# +-------+
# """
# dice_faces = {
#     1: dice_1,
#     2: dice_2,
#     3: dice_3,
#     4: dice_4,
#     5: dice_5,
#     6: dice_6
# }

# roll = random.randint(1, 6)
# print(dice_faces[roll])