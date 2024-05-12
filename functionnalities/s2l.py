from src import letterWithSound
from shared import inputHelper
import unidecode as uniDecoder

userInput = inputHelper.set_user_input(cta_message="Phrase à décoder : \n>>>")

syllable = []
answer = ""
separator = ""

for letter in userInput:
    if not letter.isalpha():
        answer += letter
    elif letter.isalpha():
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
