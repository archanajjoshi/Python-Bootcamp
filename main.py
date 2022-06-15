print(
    """
*******************************************************************************
      _,-""-._
        ,"        ".
       /    ,-,  ,"\
      "    /   \ | o|
      \    `-o-"  `-',
       `,   _.--'`'--`
         `--`---'                    |   _)
           ,' '      _  /  _ \  ` \   _ \ |  -_)
         ./ ,  `,    ___|\___/_|_|_|_.__/_|\___|
         / /     \
        (_)))_ _,"
           _))))_,
  --------(_,-._)))-------------------------------
*******************************************************************************
"""
)
print("Welcome to Zombie Land.")
print("Your mission is to stay alive.")

choice = input("Make a choice, left or right? ")
choice.lower()

if choice != "left":
    print(
        "Bad choice, now get rekt! Zombie has killed you by twisting your skull and pulling out your tongue. Game Over Loser!"
    )
else:
    choice2 = input("Do you wanna swim or wait? ")
    choice2.lower()
    if choice2 != "wait":
        print(
            "Woohoo!!! You have chosen BRUTAL DEATH!!! Zombie kills you by eating you alive piece by piece!! Yum! Game Over Nerrrrd!"
        )
    else:
        choice3 = input(
            "You approach 3 doors, red, blue and yellow. Which one will you choose? "
        )
        choice3.lower()
        if choice3 != "yellow":
            print(
                "Amazing choice! Congratulations!!! The door opens to a gang of zombies waiting to fuck you over and guess what... they DO fuck you over! Goodbye!"
            )
            print("Game Over Motherfucker!!!")
        else:
            print(
                "Congratulations! After making wise choices, you go back to your mundane life, sucker!"
            )
