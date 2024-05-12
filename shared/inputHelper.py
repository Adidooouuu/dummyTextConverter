import inquirer
from inquirer import list_input

class InputHelper:
    def __init__(
        self,
        choices_list: list[str],
        cta_message: str = ""
        ):
        self.choices_list = choices_list
        self.cta_message = cta_message

    def get_user_choice(self) -> str:
        question = list_input(
            message = self.cta_message,
            choices = self.choices_list
            )
        choice  = question.lower()
        return choice

    def use_correct_import(self, choice: str, choices_list: list[str]):
        choices_list_lowered = [element.lower() for element in choices_list]
        if choice == choices_list_lowered[0]:
            from functionnalities import l2s as letter2Sound
        elif choice == choices_list_lowered[1]:
            from functionnalities import s2l as sound2Letter
        elif choice == choices_list_lowered[2]:
            print("À bientôt !")
            exit(0)
        else:
            print("Entrée invalide")
            exit(0)