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

    def input_creation(self) -> dict:
        question = list_input(
            message = self.cta_message,
            choices = self.choices_list
            )
        answer  = question.lower()
        return {
            "choices_list": self.choices_list,
            "question": question,
            "answer": answer
            }

    # def associate_choice_to_module(self):
    #     if input_created["answer"] == input_created["choices_list"][0].lower():
    #         from functionnalities import l2s as letter2Sound
    #     elif input_created["answer"] == input_created["choices_list"][1].lower():
    #         from functionnalities import s2l as sound2Letter
    #     elif input_created["answer"] == input_created["choices_list"][2].lower():
    #         print("À bientôt !")
    #         exit(0)
    #     else:
    #         print("Entrée invalide")