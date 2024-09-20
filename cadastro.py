import csv

usuarios = {}


def cadastrar_usuario():
  id_usuario = input("Digite o ID do usuário:")
  if id_usuario in usuarios:
    print("Usuário já cadastrado.")
  else:
    nome = input("Digite o nome do usuário:")
    email = input("Digite o email do usuário:")
    usuarios[id_usuario] = {"nome": nome, "email": email}
    print("Usuário cadastrado com sucesso.")


def listar_usuarios():
  if not usuarios:
    print("Nenhum usuário cadastrado.")
  else:
    print("\nLista de Usuários:")
    for id_usuario, dados in usuarios.items():
      print(
          f"ID: {id_usuario}, Nome: {dados['nome']}, E-mail: {dados['email']}")


def consultar_usuario():
  id_usuario = input("Digite o ID do usuário:")
  if id_usuario in usuarios:
    dados = usuarios[id_usuario]
    print(f"ID: {id_usuario}, Nome: {dados['nome']}, E-mail: {dados['email']}")

  else:
    print("Usuário não encontrado.")


def excluir_usuario():
  id_usuario = input("Digite o ID do usuário:")
  if id_usuario in usuarios:
    del usuarios[id_usuario]
    print("Usuário excluído com sucesso.")

  else:
    print("Usuário não encontrado.")


def exportar_para_csv():
  with open("usuarios.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Nome", "E-mail"])
    for id_usuario, dados in usuarios.items():
      writer.writerow([id_usuario, dados['nome'], dados['email']])

  print("Dados exportados para usuarios.csv com sucesso.")


def menu():
  while True:
    print("\nMenu:")
    print("0. Sair")
    print("1. Cadastrar um novo usuário")
    print("2. Listar todos os usuários cadastrados")
    print("3. Consultar um usuário")
    print("4. Excluir um usuário")
    escolha = input("Escolha uma opção (0-4):")
    if escolha == "0":
      print("Saindo do programa...")
      exportar_para_csv()
      break

    elif escolha == "1":
      cadastrar_usuario()

    elif escolha == "2":
      listar_usuarios()

    elif escolha == "3":
      consultar_usuario()

    elif escolha == "4":
      excluir_usuario()

    else:
      print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
  menu()