import inquirer
from inquirer import List

choicesList = [
  "Convertir une phrase en syllabes",
  "Convertir des syllabes en mots",
  "Annuler"
  ]
question = [
  List("conversions", message="Sélectionne une conversion :", choices=choicesList),
]

answers = inquirer.prompt(question)
answer = "".join(answers['conversions'])
print(f"Tu veux donc {answer.lower()}. Eh beh go baby go!")

if answer == choicesList[0]:
  from functionnalities import l2s as letter2Sound
elif answer == choicesList[1]:
  from functionnalities import s2l as sound2Letter
elif answer == choicesList[2]:
  print("À bientôt !")
else:
  print("Entrée invalide")
  answers = inquirer.prompt(question)
