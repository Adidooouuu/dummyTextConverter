from src import letterWithSound
from shared import inputHelper

userInput = inputHelper.set_user_input(cta_message="Phrase à encoder : \n>>>")
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
