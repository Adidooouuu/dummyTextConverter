from src import letterWithSound
import unidecode as uniDecoder

userInput = input("Entrée : \n>>>")
userInput = userInput.lower()

syllable = []
answer = ""
separator = ""

for letter in userInput:
    if letter.isalpha():
        syllable.append(letter)
    else:
        continue
    stringedSyllable = separator.join(syllable)
    stringedSyllable = uniDecoder.unidecode(stringedSyllable)
    for realLetter, sound in letterWithSound.sounds.items():
        if stringedSyllable == sound:
            answer += realLetter
            syllable.clear()
            stringedSyllable = ""
print(answer)





#Arichikatakitoku