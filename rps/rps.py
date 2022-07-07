rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
from random import choice

choices = ["rock", "paper", "scissors"]

user_choice = str(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

match user_choice:
    case "0":
        user_choice = choices[0]
        print(rock)
    case "1":
        user_choice = choices[1]
        print(paper)
    case "2":
        user_choice = choices[2]
        print(scissors)
    case _:
        print("Wrong choice, loser!")
        quit()

computer_choice_index = choice(range(len(choices)))
computer_choice = choices[computer_choice_index]

print(f"Computer chooses: {computer_choice}")

match computer_choice_index:
    case 0:
        print(rock)
    case 1:
        print(paper)
    case 2:
        print(scissors)

if user_choice == computer_choice:
    print("It is a tie")
elif (user_choice == "rock" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "rock"):
    print("You lose.")
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    print("You win.")
