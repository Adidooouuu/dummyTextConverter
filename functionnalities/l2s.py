from src import letterWithSound

userInput = input("Phrase à encoder : \n>>>")
userInput = userInput.lower()
answer = ""

for letter in userInput:
    if not letter.isalpha():
        answer += letter
    else:
        for sound in letterWithSound.sounds:
            if letter == sound:
                answer += letterWithSound.sounds[sound]
            else:
                continue
print(answer)