import csv
import os

file_name = 'cadastro.csv'

file_exist = os.path.exists('cadastro.csv')

file_exist = os.path.exists(file_name)
if not file_exist:
  with open(file_name, mode= 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['nome_completo', 'idade', 'CPF',
    'endereço','telefone', 'email'])
    writer.writeheader()

print(f'o arquivo {file_name} foi criado')
resposta = input("Você deseja se cadastrar um usuario, consuntar um cadastro ou excluir?").strip()

def cadastro():  
    nome_completo = input('digite seu nome completo:').title().isalpha()
    while not nome_completo.title().isalpha():
      print("digite apenas letras por favor")
      nome_completo = input("digite seu nome completo: ")
    idade = input('digite sua idade: ')
    while not idade.isdigit():
      print("a idade deve ser infomado apenas com digitos!")
      idade = input('digite sua idade: ')
    CPF = input('digite seu CPF:')
    while not CPF.isdigit():
      print('apenas os números devem ser informados: ')
      CPF = input('digite seu CPF: ')
    endereco = input('digite seu endereço:').istitle()
    telefone = input('digite seu número de telefone:').isnumeric
    email = input('digite seu email:').strip()

    with open('cadastro.csv', 'a', newline='') as file:
      writer = csv.writer(file)
      writer.writerow([nome_completo, idade, CPF, endereco, telefone, email])

      print('cadastro realizado com sucesso')

def listar_cadastro():
    with open('cadastro.csv', 'r') as file:
      reader = csv.reader(file)
      for row in reader:
        print(row)


def consulta_cadastro():
    nome_completo = input('Digite o nome dp cadastrp que deseja consultar: ').strip()
    with open('cadastro.csv', 'r') as file:
      reader = csv.reader(file)
      for row in reader:
        if row[0] == nome_completo:
          print(row)
          break
      else:
        print('Cadastro não encontrado')



def excluir_cadastro():
  nome_completo = input('Digite o nome do cadastro que deseja excluir: ').strip()
  with open('cadastro.csv', 'r') as file:
      reader = csv.reader(file)
      rows = list(reader)
      for row in rows:
        if row[0] == nome_completo:
          rows.remove(row)
          break

      else:
        print('Cadastro não encontrado')

  with open('cadastro.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerows(rows)

      print('Cadastro excluido com sucesso')

if resposta.lower() == 'cadastrar':
  cadastro()

if resposta.lower() == 'consultar':
  consulta_cadastro()

if resposta.lower() == 'excluir':
  excluir_cadastro()