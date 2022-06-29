import pyfiglet
import inquirer
from tabulate import tabulate

table = []
headers = ["Receita", "Tipo", "Criador"]
users = []

def create_user():
  name = str(input('Digite seu nome: '))
  username = str(input('Digite o login que deseja: '))
  password = str(input('Digite a senha que deseja: '))
  if username in [user['login'] for user in users]:
    return False
  user = {
    'nome': name,
    'login': username,
    'senha': password
  }
  return user

def insert_user(usuario):
  usuarios = open('manager\\users\\usuarios.txt', 'a')
  usuarios.write(f'{usuario["nome"]} - {usuario["login"]} - {usuario["senha"]}\n')

def create_user_archives():
  usuarios = open('manager\\users\\usuarios.txt', 'a')
  usuarios.close()

def read_users():
  usuarios = open('manager\\users\\usuarios.txt', 'r')
  for line in usuarios:
    line = line.replace('\n', '').split(' - ')
    users.append({
      'nome': line[0],
      'login': line[1],
      'senha': line[2]
    })
  usuarios.close()

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

def create_recipe(usuarios):
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
  return recipe 

def insert_recipe(recipe):
  recipes = open('manager\\users\\receitas.txt', 'a')
  recipes.write(f'{recipe["nome"]} - {recipe["type"]} - {recipe["ingredientes"]} - {recipe["preparo"]} - {recipe["autor"]}\n')

def create_recipe_archive():
  recipes = open('manager\\users\\receitas.txt', 'w')
  recipes.close()

def read_recipes():
  recipes = open('manager\\users\\receitas.txt', 'r')
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
  read_users()
  while True:
    main_template()
    if(is_logged == False):
      selected_unit = inquirer.list_input("Escolha uma opção abaixo", choices=['Registrar', 'Logar', 'Sair'])
      if selected_unit == "Registrar":
        usuario = create_user()
        if usuario == False:
          print("Login já existe! 😢")
        else:
          insert_user(usuario)
          read_users()
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
      selected_unit = inquirer.list_input("Escolha uma opção abaixo", choices=['Criar receita', 'Listar receitas', 'Deslogar'])
      if selected_unit == "Criar receita":
        recipe = create_recipe(users)
        insert_recipe(recipe)
        read_recipes()
      elif selected_unit == "Deslogar":
        is_logged = exit_user()


if __name__ == "__main__":
  main()