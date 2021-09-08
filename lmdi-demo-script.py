from typing import List
from math import sinh


class LmdiEmployee:

    def __init__(self, name: str, lastname: str) -> None:
        self.name = name
        self.lastname = lastname
        self.lmdi_function = "placeholder"
        self._print_employee()

    def upgrade_function(self, job_description: str) -> None:
        self.lmdi_function = self.lmdi_function.change()
        return print(f'{self.name} job changed to ')

    def change_name(self, name: str):
        if type(name) == str:
            self.name = name
        else:
            return print('incorrect dataype')

    def _print_employee(self):
        return print(f'{self.name} {self.lastname}, created')

    def _private_function(self):
        pass


if __name__ == "__main__":

    nick = LmdiEmployee("Nick", "Polman")
    jeffey = LmdiEmployee("jeffrey", "?")
    jimmy = LmdiEmployee("Jimmy", "Hendriks")

    nick.change_name('nickolasandros')
    jimmy.change_name('')
    print(nick.name)
