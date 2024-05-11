from shared import inputHelper

inputHelper = inputHelper.InputHelper(
  choices_list = [
  "Convertir une phrase en syllabes",
  "Convertir des syllabes en mots",
  "Annuler"
  ],
  cta_message = "Sélectionne une conversion "
)

input_created = inputHelper.input_creation()

print(f"Tu veux donc {input_created["answer"]}. Eh beh go baby go!")

if input_created["answer"] == input_created["choices_list"][0].lower():
  from functionnalities import l2s as letter2Sound
elif input_created["answer"] == input_created["choices_list"][1].lower():
  from functionnalities import s2l as sound2Letter
elif input_created["answer"] == input_created["choices_list"][2].lower():
  print("À bientôt !")
  exit(0)
else:
  print("Entrée invalide")