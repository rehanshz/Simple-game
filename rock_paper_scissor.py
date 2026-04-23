from random import randint
def rockpaperscissor():
    while True:

        print("""
    ____             __       ____                       
   / __ \____  _____/ /__    / __ \____ _____  ___  _____
  / /_/ / __ \/ ___/ //_/   / /_/ / __ `/ __ \/ _ \/ ___/
 / _, _/ /_/ / /__/ ,<     / ____/ /_/ / /_/ /  __/ /    
/_/ |_|\____/\___/_/|_|   /_/    \__,_/ .___/\___/_/     
   _____      _                      /_/                 
  / ___/_____(_)_____________  __________                
  \__ \/ ___/ / ___/ ___/ __ \/ ___/ ___/                
 ___/ / /__/ (__  |__  ) /_/ / /  (__  )                 
/____/\___/_/____/____/\____/_/  /____/                  """)
        w=input("would you like to continue (y/n)")
        if w.lower()=="n":
            break
        else:
            pass
            ch = input("choose Rock Paper Scissors: ")
            lib={1:"rock",2:"paper",3:"scissor"}
            b=randint(1,3)

            you=0
            bot=0
            
            print(f"you choose : {ch}\nbot choose:{lib[b]}")

            if ch.lower()=="rock":
                if lib[b]=="rock":
                    print("Its a Draw ....")
                elif lib[b]=="paper":
                    print("You Lost... Bot Wins")
                    bot+=1
                elif lib[b]=="scissor":
                    print("yayy.. You Win..")
                    you+=1
                else:
                    print("something went wrong")
                print(f"Score \nyou={you}\nbot={bot}")
            if ch.lower()=="paper":
                if lib[b]=="rock":
                    print("yayy.. You Win..")
                    you+=1
                elif lib[b]=="paper":
                    print("Its a Draw ....")
                elif lib[b]=="scissor":
                    print("You Lost... Bot Wins")
                    bot+=1
                else:
                    print("something went wrong")
                print(f"Score \nyou={you}\nbot={bot}")
            if ch.lower()=="scissor":
                if lib[b]=="rock":
                    print("You Lost... Bot Wins")
                    bot+=1
                elif lib[b]=="paper":
                    print("yayy.. You Win..")
                    you+=1
                elif lib[b]=="scissor":
                    print("Its a Draw ....")
                else:
                    print("something went wrong")
                print(f"Score \nyou={you}\nbot={bot}")
        
        