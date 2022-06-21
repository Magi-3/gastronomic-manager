import pyfiglet
import inquirer
from tabulate import tabulate

is_logged = False
table = [["spam",42,"cleiton"],["eggs",451, "jose"],["bacon",0]]
headers = ["Receita", "Tipo", "Criador"]


print(pyfiglet.figlet_format("ATOM"))
print(tabulate(table, headers, tablefmt="fancy_grid"))

selected_unit = inquirer.list_input("Escolha uma opção abaixo", choices=['Registrar', 'Logar'])
if selected_unit == "Registrar":
  pass
elif selected_unit == "Logar":
  pass


def soma_dois():
  pass