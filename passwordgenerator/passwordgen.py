#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
'''password_letters = " "
for letter in range(0, nr_letters):
    current_letter = random.choice(letters)
    password_letters += current_letter


password_symbols = " "
for symbol in range(0, nr_symbols):
    current_symbol = random.choice(symbols)
    password_symbols += current_symbol

password_numbers = " "
for number in range(0, nr_numbers):
    current_number = str(random.choice(numbers))
    password_numbers += current_number

print("Generated password is" + " " + password_letters.strip(" ") + password_numbers.strip(" ") + password_symbols.lstrip(" "))'''

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_letters = []
for letter in range(0, nr_letters):
    current_letter = random.choice(letters)
    password_letters.append(current_letter)
#random_password.append(password_letters)

password_symbols = []
for symbol in range(0, nr_symbols):
    current_symbol = random.choice(symbols)
    password_symbols.append(current_symbol)
#random_password.append(password_symbols)

password_numbers = []
for number in range(0, nr_numbers):
    current_number = random.choice(numbers)
    password_numbers.append(current_number)
#random_password.append(password_numbers)

random_password = password_letters + password_symbols + password_numbers

generated_password = " "
total_characters = nr_numbers + nr_symbols + nr_letters
for i in range(0, total_characters):
    generated_password += random.choice(random_password)

print("Generated password is" + " " + generated_password)










