import pyfiglet
import inquirer
from tabulate import tabulate

table = [["spam",42,"cleiton"],["eggs",451, "jose"],["bacon",0]]
headers = ["Receita", "Tipo", "Criador"]

def create_user():
  registro = str(input('Digite seu primeiro nome, login e senha (separados por vírgula): ')).strip().split(',')
  usuario = {
    'nome': registro[0].strip(),
    'login': registro[1].strip(),
    'senha': registro[2].strip()
  }
  return usuario

def exit_user():
  print('Saindo da conta...')
  return False
  
  
def main_template():
  print(pyfiglet.figlet_format("ATOM"))
  print(tabulate(table, headers, tablefmt="fancy_grid"))


users = []

def main():
  is_logged = False
  while True:
    main_template()
    if(is_logged == False):
      selected_unit = inquirer.list_input("Escolha uma opção abaixo", choices=['Registrar', 'Logar', 'Sair'])
      if selected_unit == "Registrar":
        users.append(create_user())
        print("Registro feito com sucesso! 👍")
      elif selected_unit == "Logar":
        dados = str(input("Digite seu login e senha: (separados por vírgula): ")).strip().split(',')
        if (dados[0].strip() == users[0]['login'] and dados[1].strip() == users[0]['senha']):
          is_logged = True
          print("Login feito com sucesso! 👍")
      elif selected_unit == "Sair":
        break
    elif (is_logged):
      selected_unit = inquirer.list_input("Escolha uma opção abaixo", choices=['Criar receita', 'Listar receitas', 'Sair'])
      if selected_unit == "Sair":
        is_logged = exit_user()


if __name__ == "__main__":
  main()