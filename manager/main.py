import pyfiglet
import inquirer
from tabulate import tabulate

def create_user():
  registro = str(input('Digite seu primeiro nome, login e senha (separados por vírgula): ')).strip().split(',')
  
  usuario = {
    'nome': registro[0].strip(),
    'login': registro[1].strip(),
    'senha': registro[2].strip()
  }

  return usuario

def create_recipe():
  check_login(dados)
  author = users[0]['nome']
  recipe_name = str(input("Digite o nome da sua receita: "))  
  ingredients = str(input("Digite os ingredientes necessários: "))
  preparation = str(input("Digite o modo de preparo: "))
  
  recipe = {
    "autor": author,
    "receita": recipe_name,
    "ingredientes": ingredients,
    "preparo": preparation
}
  
  return recipe

def check_login(dados):
  if (dados[0].strip() == users[0]['login'] and dados[1].strip() == users[0]['senha']):
    return True
  else:
    return False

users = []
recipes = []

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
      is_logged = check_login(dados)
      if is_logged:
        print("Login feito com sucesso! 👍")
      elif not is_logged:
        print("Login inválido! 🤔")
    print(pyfiglet.figlet_format("ATOM"))
    print(tabulate(table, headers, tablefmt="fancy_grid"))
  elif (is_logged):
    selected_unit = inquirer.list_input("Escolha uma opção abaixo", choices=['Criar receita', 'Listar receitas', 'Sair']) 
    if selected_unit == "Criar receita":
      recipes.append(create_recipe())
      print(recipes)
      print("Receita criada com sucesso! 👍")    