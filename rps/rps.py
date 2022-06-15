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
import random

element_matrix = ["rock", "paper", "scissors"]

user_choice = str(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if user_choice == "0":
  user_choice = element_matrix[0]
  print(rock)
elif user_choice == "1":
  user_choice = element_matrix[1]
  print(paper)
elif user_choice == "2":
  user_choice = element_matrix[2]
  print(scissors)

computer_choice = str(random.randint(0, 2))
print("Computer chooses: " + computer_choice)

if computer_choice == "0":
  computer_choice = element_matrix[0]
  print(rock)
elif computer_choice == "1":
  computer_choice = element_matrix[1]
  print(paper)
elif computer_choice == "2":
  computer_choice = element_matrix[2]
  print(scissors)

#final_choice = [user_choice, computer_choice]
#print(final_choice)

if(user_choice == computer_choice):
  print("It is a tie")
elif((user_choice == "rock" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "scissors") or user_choice == "scissors" and computer_choice == "rock"):
  print("You lose.")
elif((user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or user_choice == "scissors" and computer_choice == "paper"):
  print("You win.")