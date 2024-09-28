import csv
import os

file_name = 'cadastro.csv'

file_exist = os.path.exists('cadastro.csv')

file_exist = os.path.exists(file_name)
if not file_exist:
  with open(file_name, mode= 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['nome_completo', 'idade', 'CPF',
    'endereco','telefone', 'email','produto'])
    writer.writeheader()
    print(f'o arquivo {file_name} foi criado')

def cadastro():  
  nome_completo = input('digite seu nome completo: ').strip().title()
  while not nome_completo.replace(" ", "").isalpha():
    print("digite apenas letras por favor")
    nome_completo = input("digite seu nome completo: ").strip().title()
  idade = input('digite sua idade: ')
  while not idade.isdigit():
    print("a idade deve ser infomado apenas com digitos!")
    idade = input('digite sua idade: ')
  CPF = input('digite seu CPF: ')
  while not CPF.isdigit():
    print('Digite apenas os digitos do CPF devem ser informados: ')
    CPF = input('digite seu CPF: ')
  endereco = input('digite seu endereço: ')
  telefone = input('digite seu número de telefone: ')
  while not telefone.isdigit():
    print("digite apenas o número de seu telefone para contato")
    telefone = input('digite seu número corretamete: ')
  email = input('digite seu email: ').strip()
  produto = input("digite o nome do produto a ser entregue ou serviço que foi pedido: ").strip()
  with open('cadastro.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([nome_completo, idade, CPF, endereco, telefone, email, produto])

    print('cadastro realizado com sucesso')

def listar_cadastro():
      with open('cadastro.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row:
              for i in range(len(header)):
                  print(f"{header[i]}: {row[i]}")
              print("-" * 40)
            
def consulta_cadastro():
  nome_completo = input('Digite o nome do cadastrado que deseja consultar: ').strip().title()
  with open('cadastro.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      if row[0].strip().title() == nome_completo:
        print(row)
        break
    else:
      print('Cadastro não encontrado')

def excluir_cadastro():
  nome_completo = input('Digite o nome do cadastro que deseja excluir: ').strip().title()
  with open('cadastro.csv', 'r') as file:
      reader = csv.reader(file)
      rows = list(reader)
      for row in rows:
        if row[0] == nome_completo.strip().title():
          rows.remove(row)
          break

      else:
        print('Cadastro não encontrado')

  with open('cadastro.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerows(rows)

      print('Cadastro excluido com sucesso')

resposta = input("Você deseja se cadastrar um usuario, consultar um cadastro, excluir ou sair do sistema? ").strip().lower()
while resposta.lower != 'sair':
    if resposta.lower() == 'cadastrar':
      cadastro()
      input("Você deseja se cadastrar um usuario, consultar um cadastro, excluir ou sair do sistema? ")
    if resposta.lower() == 'consultar':
      consulta_cadastro()
      input("Você deseja se cadastrar um usuario, consultar um cadastro, excluir ou sair do sistema? ")
    if resposta.lower() == 'excluir':
      excluir_cadastro()
      input("Você deseja se cadastrar um usuario, consultar um cadastro, excluir, sair do sistema ou ver a lista toda? ")
    if resposta.lower() == 'ver':
      listar_cadastro()
    else:
      print('digite apenas as palavrar cadastrar, consultar, excluir, sair e ver!')
      break

print("Saindo do sistema...")



    