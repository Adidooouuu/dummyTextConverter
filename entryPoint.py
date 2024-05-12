from shared import inputHelper

inputHelper = inputHelper.InputHelper(
  choices_list = [
  "Convertir une phrase en syllabes",
  "Convertir des syllabes en mots",
  "Annuler"
  ],
  cta_message = "Sélectionne une conversion "
)

choice = inputHelper.get_user_choice()

print(f"Tu veux donc {choice}. Eh beh go baby go!")

inputHelper.use_correct_import(choice)