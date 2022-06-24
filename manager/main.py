def create_user():
  registro = str(input('Digite seu primeiro nome, login e senha (separados por vírgula): ')).strip().split(',')
  
  usuario = {
    'nome': registro[0].strip(),
    'login': registro[1].strip(),
    'senha': registro[2].strip()
  }

  return usuario

users = []

import pyfiglet
import inquirer
from tabulate import tabulate

is_logged = False
table = [["spam",42,"cleiton"],["eggs",451, "jose"],["bacon",0]]
headers = ["Receita", "Tipo", "Criador"]

print(pyfiglet.figlet_format("ATOM"))
print(tabulate(table, headers, tablefmt="fancy_grid"))

while True:
  if (is_logged == False):
    selected_unit = inquirer.list_input("Escolha uma opção abaixo", choices=['Registrar', 'Logar'])
    if selected_unit == "Registrar":
      users.append(create_user())
      print("Registro feito com sucesso! 👍")
    elif selected_unit == "Logar":
      dados = str(input("Digite seu login e senha: (separados por vírgula): ")).strip().split(',')
      if (dados[0].strip() == users[0]['login'] and dados[1].strip() == users[0]['senha']):
        is_logged = True
        print("Login feito com sucesso! 👍")
    print(pyfiglet.figlet_format("ATOM"))
    print(tabulate(table, headers, tablefmt="fancy_grid"))
  elif (is_logged):
    selected_unit = inquirer.list_input("Escolha uma opção abaixo", choices=['Criar receita', 'Listar receitas', 'Sair']) 


listar_receitas = []

def receitas():
  nome = str(input("digite seu nome: "))
  nomereceita = str(input("digite o nome da sua receita: "))  
  ingre = str(input("digite os ingridientes necessários: "))
  preparo = str(input("digite o modo de preparo: "))
  
  receita = {"criador":nome,
             "nome da receita":nomereceita,
             "ingredientes": ingre,
             "modo de preaparo": preparo,}
  return receita


listar_receitas.append(receitas())          
             