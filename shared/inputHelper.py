import inquirer
from inquirer import list_input


class InputHelper:
    def __init__(self, choices_list: list[str], cta_message: str = ""):
        self.choices_list = choices_list
        self.cta_message = cta_message

    def get_user_choice(self) -> str:
        question = list_input(message=self.cta_message, choices=self.choices_list)
        choice = question.lower()
        return choice

    def lower_choices(self, choices_list: list[str]) -> list[str]:
        return [element.lower() for element in choices_list]

    def use_correct_import(self, choice: str = "") -> callable:
        choices_list_lowered = self.lower_choices(self.choices_list)

        choices_dict = {
            choices_list_lowered[0]: "functionnalities.l2s",
            choices_list_lowered[1]: "functionnalities.s2l",
        }

        if choice in choices_dict:
            try:
                from importlib import import_module

                return import_module(choices_dict[choice])
            except (ImportError, AttributeError) as e:
                print(f"Erreur d'import: {e}")
                return None
        elif choice == choices_list_lowered[2]:
            print("À bientôt !")
            exit(0)
        else:
            print("Entrée invalide")
            exit(0)


def set_user_input(cta_message: str) -> str:
    while True:
        user_input = input(cta_message)
        user_input = user_input.strip()
        if user_input:
            user_input = user_input.lower()
            return user_input
        else:
            print("Valeur vide.")
