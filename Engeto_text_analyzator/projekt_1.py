"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Romana Bělohoubková
email: romanabelohoubkova@gmail.com
discord: romana_belohoubkova
"""

# Definování registrovaných uživatelů a hesel
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Texty k analýze
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

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

username = input("username: ")
password = input("password: ")

if username in users and users[username] == password:
        
    separator = "-" * 40

    print(separator)
    print(f"Welcome to the app, {username}")
    print(f"We have 3 texts to be analyzed.")
    print(separator)

    text_input = input("Enter a number btw. 1 and 3 to select: ")
    print(separator)

    if not text_input.isdigit() or int(text_input) not in range(1, 4):
        print("invalid selection, terminating the program..")
        exit()
    else:
        text_input = int(text_input)
        selected_text = TEXTS[text_input - 1]

    words = selected_text.split()
    word_count = len(words)

    total_word_count = 0
    titlecase_words = 0
    uppercase_words = 0
    lowercase_words = 0
    numeric_strings = []
    word_lengths = []

    for word in words:

        word = word.strip('.,?!')
        total_word_count += 1
        
        if word.istitle():
            titlecase_words += 1       
        if word.isupper() and word.isalpha():
            uppercase_words += 1 
        if word.islower():
            lowercase_words += 1
        if word.isdigit():
            numeric_strings.append(int(word))
    
        word_lengths.append(len(word))

    print(f"There are {word_count} words in the selected text.")
    print(f"There are {titlecase_words} titlecase words.")
    print(f"There are {uppercase_words} uppercase words.")
    print(f"There are {lowercase_words} lowercase words.")
    print(f"There are {len(numeric_strings)} numeric strings.")
    print(f"The sum of all the numbers {sum(numeric_strings)}")
    print(separator)
    print(f"LEN|{'OCCURENCES'.center(18)}|NR.")
    print(separator)
    
    length_frequency = {}
    for length in word_lengths:

        if length in length_frequency:
            length_frequency[length] += 1
        else:
            length_frequency[length] = 1

    for length in sorted(length_frequency):
        print(f"{length:3}|{'*' * length_frequency[length]:18}|{length_frequency[length]}")
        
else:
    print("unregistered user, terminating the program..")