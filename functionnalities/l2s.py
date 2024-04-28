from src import letterWithSound

userInput = input("Entrez votre phrase à encoder : \n>>>")
userInput = userInput.lower()

for letter in userInput:
    for sound in letterWithSound.sounds:
        if letter == sound:
            print(letter + " : " + letterWithSound.sounds[sound])
        else:
            continue

#Arichikatakitoku