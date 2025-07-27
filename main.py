"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kristýna Růžičková  
email: krist.ruzickova@gmail.com
"""

TEXTS = [
'''Situated about 10 miles west of Kemmerer,
 Fossil Butte is a ruggedly impressive
 topographic feature that rises sharply
 some 1000 feet above Twin Creek Valley
 to an elevation of more than 7500 feet
 above sea level. The butte is located just
 north of US 30 and the Union Pacific Railroad,
 which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


#login
users = {"bob" : "123", "ann" : "pass123", "mike" : "password 123", "liz" : "pass 123"}
username = input("Please enter: \nUsername: " )
password = input("Password: ")
print("-" * 38)
if username in users and users[username] == password:
    print (f"Welcome to the app {username}.\nWe have 3 texts to be analyzed.")
else:
    print ("You are not registered or you filled in wrong details. Terminating the program.")
    exit()
print("-" * 38)


#text choice
text = input("Enter a number btw. 1 and 3 to select: ") 
if text.isdigit():
    choice = int(text)
    if choice not in range(len(TEXTS) + 1):
        print("This is not a valid option. Terminating the program.")
        exit()
    else:
        chosen_text = TEXTS[choice - 1]     
else:
    print("This is not a number. Terminating the program.")
    exit()

print("-" * 38)

#text edit
for character in chosen_text:
    if not (character.isdigit() or character.isalpha() or character.isspace()):
        chosen_text = chosen_text.replace(character, "")
chosen_text_slova = chosen_text.split()

#statistics
sum_words = len(chosen_text_slova)

title_letters = 0
upper_letters = 0
lower_letters = 0
for character in chosen_text_slova:
    if character.istitle():
        title_letters += 1
    if character.isupper():
        upper_letters += 1
    if character.islower():
        lower_letters += 1

numbers = []

for word in chosen_text_slova:
    if word.isdigit():
        number = int(word)
        numbers.append(number)
sum_numbers = (len(numbers))

suma = sum(numbers)

#print results
print(f"There are {sum_words} words in the selected text.")
print(f"There are {title_letters} titlecase words.")
print(f"There are {upper_letters} uppercase words.")
print(f"There are {lower_letters} lowercase words.")
print(f"There are {sum_numbers} numeric strings.")
print(f"The sum of all the numbers is {suma}.")
print("-" * 38)

#graph
print("-" * 28)
print("LEN|".rjust(5), "OCCURENCES".ljust(15), "|NR.")
print("-" * 28)

occurence = {}

for word in chosen_text_slova:
    length = len(word)
    if length in occurence:
        occurence[length] += 1
    else:
        occurence[length] = 1

for length in sorted(occurence):
    stars = '*' * occurence[length]
    print(f"{str(length).rjust(3)} | {stars.ljust(15)} | {occurence[length]}")
print("-" * 28)

