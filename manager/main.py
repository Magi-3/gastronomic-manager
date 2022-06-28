import pyfiglet
import inquirer
from tabulate import tabulate

#["spam",42,"cleiton"],["eggs",451, "jose"],["tofu",12,"maria"]
table = []
headers = ["Receita", "Tipo", "Criador"]
users = []

def create_user():
  name = str(input('Digite seu nome: '))
  username = str(input('Digite o login que deseja: '))
  password = str(input('Digite a senha que deseja: '))
  user = {
    'nome': name,
    'login': username,
    'senha': password
  }
  return user

def login_user(usuarios):
  global login
  login = str(input('Digite seu login: '))
  password = str(input('Digite sua senha: '))

  for usuario in usuarios:
    if usuario['login'] == login and usuario['senha'] == password:
      return True
  return False

def exit_user():
  print('Saindo da conta...')
  return False

def create_repice(usuarios):
  for usuario in usuarios:
    if usuario['login'] == login:
      author = usuario['nome']
  name = str(input('Digite o nome da receita: '))
  recipe_type = str(input('Digite o tipo da receita: '))
  ingredients = str(input('Digite os ingredientes necessários: '))
  preparation = str(input('Digite o modo de preparo da receita: '))
  recipe = {
    'nome': name,
    'type': recipe_type,
    'ingredientes': ingredients,
    'preparo': preparation,
    'autor': author
  }
  table.append([name, recipe_type, ingredients, preparation, author])
  return recipe 

def create_recipe_archive():
  recipes = open('receitas.txt', 'a')
  for recipe in table:
    for item in range(len(recipe)):
      if item == len(recipe) - 1:
        recipes.write(f'{recipe[item]}\n')
      else:
        recipes.write(f'{recipe[item]} - ')
  recipes.close()

def read_recipes():
  recipes = open('receitas.txt', 'r')
  for line in recipes:
    line = line.replace('\n', '').split(' - ')
    table.append([line[0], line[1], line[-1]])
  recipes.close()

def main_template():
  print(pyfiglet.figlet_format("ATOM"))
  print(tabulate(table, headers, tablefmt="fancy_grid"))


def main():
  is_logged = False
  read_recipes()
  while True:
    main_template()
    if(is_logged == False):
      selected_unit = inquirer.list_input("Escolha uma opção abaixo", choices=['Registrar', 'Logar', 'Sair'])
      if selected_unit == "Registrar":
        usuario = create_user()
        users.append(usuario)
        print("Registro feito com sucesso! 👍")
      elif selected_unit == "Logar":
        is_logged = login_user(users)
        if is_logged == True:
          print("Login feito com sucesso! 👍")
        else:
          print("Login inválido! 😢")
      elif selected_unit == "Sair":
        break
    elif (is_logged):
      selected_unit = inquirer.list_input("Escolha uma opção abaixo", choices=['Criar receita', 'Listar receitas', 'Criar arquivo de receitas', 'Deslogar'])
      if selected_unit == "Criar receita":
        recipe = create_repice(users)
      elif selected_unit == "Criar arquivo de receitas":
        print("Criando arquivo de receitas...")
        create_recipe_archive()
        print("Arquivo criado com sucesso! 👍")
      elif selected_unit == "Deslogar":
        is_logged = exit_user()


if __name__ == "__main__":
  main()