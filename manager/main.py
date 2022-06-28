import pyfiglet
import inquirer
from tabulate import tabulate

table = [["spam",42,"cleiton"],["eggs",451, "jose"],["bacon",0]]
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
  ingredients = str(input('Digite os ingredientes necessários: '))
  preparation = str(input('Digite o modo de preparo da receita: '))
  recipe = {
    'nome': name,
    'ingredientes': ingredients,
    'preparo': preparation,
    'autor': author
  }
  return recipe 
  
def main_template():
  print(pyfiglet.figlet_format("ATOM"))
  print(tabulate(table, headers, tablefmt="fancy_grid"))


def main():
  is_logged = False
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
      selected_unit = inquirer.list_input("Escolha uma opção abaixo", choices=['Criar receita', 'Listar receitas', 'Deslogar'])
      if selected_unit == "Criar receita":
        recipe = create_repice(users)
      elif selected_unit == "Deslogar":
        is_logged = exit_user()


if __name__ == "__main__":
  main()