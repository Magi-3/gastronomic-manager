# Importação dos módulos utilizados no programa
import os
import pyfiglet
import inquirer
from time import sleep
from tabulate import tabulate

# Variaveis utilizadas no programa
table = []
headers = ['Receita', 'Marcador', 'Autor']
menu_option = ['Registrar', 'Logar', 'Sair']
logged_option = ['Criar receita', 'Listar todas as receitas', 'Buscar receita', 'Deslogar']
info_login = []

# Função para criação dos arquivos essenciais
def start():
  if not os.path.isfile('db/usuarios_db.txt'):
    db_user = open('db/usuarios_db.txt', 'w')
    db_user.close()
  if not os.path.isfile('db/receitas_db.txt'):
    db_recipe = open('db/receitas_db.txt', 'w')
    db_recipe.close()

# Função para ler o banco de dados de usuários
def read_user_db():
  db_user = open('db/usuarios_db.txt', 'r')
  users = db_user.readlines()
  db_user.close()
  return users

# Função para ler o banco de dados de receitas
def read_recipe_db():
  db_recipe = open('db/receitas_db.txt', 'r')
  recipes = db_recipe.readlines()
  db_recipe.close()
  return recipes

# Função para criar um usuário
def create_user():
  name = str(input('\nDigite seu NOME: '))
  username = str(input('Digite o LOGIN que deseja: '))
  
  users = read_user_db()
  for user in users:
    user = eval(user)
    if user['login'] == username:
      print('\nLogin já existe! Tente novamente. 🙁\n')
      return
  
  password = str(input('Digite a SENHA que deseja: '))

  user_model = {
    'nome': name,
    'login': username,
    'senha': password
  }

  for key in user_model:
    if user_model[key] == '':
      print('\nPreencha todos os campos! 🙁\n')
      return

  db_user = open('db/usuarios_db.txt', 'a')
  db_user.write(str(user_model) + '\n')
  db_user.close()

  print('\nUsuário criado com sucesso! 🎉\n')

# Função para fazer o login do usuário
def login_user(usuarios):
  login = str(input('Digite seu LOGIN: '))
  password = str(input('Digite sua SENHA: '))
  
  for usuario in usuarios:
    usuario = eval(usuario)
    if usuario['login'] == login and usuario['senha'] == password:
      print(f'\nBem-vindo(a), {usuario["nome"]}. 🎉\n')
      info_login.append(usuario['nome'])
      return True
  
  print(f'\nLogin inválido! Tente novamente. 😢\n')
  return False

# Função para deslogar do sistema
def exit_user():
  print('Saindo...')
  print('Até mais! 👋\n')
  sleep(1.25)
  os.system('cls' or 'clear')
  return False

# Função para criar uma receita
def create_recipe():
  author = info_login[0]
  
  name = str(input('Digite o NOME da receita: '))
  recipe_type = str(input('Defina o TIPO de receita: '))
  ingredients = str(input('Liste os INGREDIENTES necessários: '))
  preparation = str(input('Digite o MODO DE PREPARO da receita: '))
  
  recipe = {
    'nome': name,
    'tipo': recipe_type,
    'ingredientes': ingredients,
    'preparo': preparation,
    'autor': author
  }

  for key in recipe:
    if recipe[key] == '':
      print('\nPreencha todos os campos! 🙁\n')
      return

  db_recipe = open('db/receitas_db.txt', 'a')
  db_recipe.write(str(recipe) + '\n')
  db_recipe.close()

  print('\nReceita criada com sucesso! 🎉\n')

# Função para listar as receitas
def list_recipes():
  recipes = read_recipe_db()
  table = []
  print('Essas são as receitas disponíveis:')
  for recipe in recipes:
    recipe = eval(recipe)
    table.append([recipe['nome'], recipe['tipo'], recipe['autor']])
  print(f'{tabulate(table, headers, tablefmt="fancy_grid")}\n')

# Função para exibir uma receita completa
def search_recipe():
  nome = str(input('Digite o NOME EXATO da receita que quer procurar: '))
  recipes = read_recipe_db()
  print('\nProcurando receita...')
  sleep(1.25)
  for recipe in recipes:
    recipe = eval(recipe)
    if recipe['nome'] == nome:
      print(f'\n\033[1mReceita encontrada:\033[m {recipe["nome"]}')
      print(f'\033[1mTipo:\033[m {recipe["tipo"]}')
      print(f'\033[1mAutor:\033[m {recipe["autor"]}')
      print(f'\033[1mIngredientes:\033[m {recipe["ingredientes"]}')
      print(f'\033[1mPreparo:\033[m {recipe["preparo"]}\n')
      return
  print('\nReceita não encontrada! Verifique o nome digitado e tente novamente. 😢\n')

# Função para limpar o terminal
def clear_terminal():
  sleep(2)
  os.system('cls' or 'clear')

# Função principal do programa
def main():
  is_logged = False

  start()
  print(pyfiglet.figlet_format("ATOM"))

  while True:
    
    if not is_logged:
      selected_unit = inquirer.list_input('Escolha uma opção', choices=menu_option)
      
      if selected_unit == "Registrar":
        create_user()
        clear_terminal()

      elif selected_unit == "Logar":
        usuarios = read_user_db()
        if usuarios == []:
          print('Não há usuários cadastrados! 🙁\n')
          clear_terminal()
        else:
          is_logged = login_user(usuarios)
          clear_terminal()
      elif selected_unit == "Sair":
        exit_user()
        break

    elif (is_logged):
      selected_unit = inquirer.list_input("Escolha uma opção abaixo", choices=logged_option)
      
      if selected_unit == "Criar receita":
        create_recipe()
        clear_terminal()
      elif selected_unit == "Listar todas as receitas":
        receitas = read_recipe_db()
        if receitas == []:
          print('Não há receitas cadastradas! 🙁\n')
          clear_terminal()
        else:
          list_recipes()
          input('Aperte ENTER para continuar...')
          clear_terminal()
      elif selected_unit == "Buscar receita":
        search_recipe()
        input('Aperte ENTER para continuar...')
        clear_terminal()
      elif selected_unit == "Deslogar":
        info_login.pop()
        is_logged = exit_user()

if __name__ == "__main__":
  main()