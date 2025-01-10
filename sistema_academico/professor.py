import sqlite3
from random import choice, randint
from datetime import datetime
from time import time

def conectar_banco():
    return sqlite3.connect("sistema_academico.db")

def _gerar_cod_prof():
    letra = choice(('A', 'B', 'C', 'D', 'E', 'F'))
    num = str(randint(12000, 55000))
    return letra+'-'+num

def validar_data(data):
    try:
        return datetime.strptime(data, "%d/%m/%Y").date()
    except ValueError:
        return
    
def _genero():
     while True:
      print(f"1 - Feminino")
      print(f"2 - Masculino")
      opcao = input("Digite a opção desejada (1 ou 2): ")
      
      if opcao == '1':
       return "Feminino"
      elif opcao == '2':
       return "Masculino"
      else:
       print(f"Opção invalida. Digite um número válido! (1 ou 2)")
      

def cadastrar_prof():
  nome = input("Digite o nome do professor: ")
  codigo = _gerar_cod_prof()
  while True:
   data_nasc = input("Digite a data de nascimento (DD/MM/AAAA): ")
   data_validada = validar_data(data_nasc)
   if data_validada:
     break
   else:
    print("Data inválida! Por favor, insira no formato DD/MM/AAAA.")
    time.sleep(1)
  genero = _genero()
  endereco = input("Digite o endereço: ")
  telefone = input("Digite o telefone: ")
  email = input("Digite o e-mail: ")
  disciplina = input("Digite o código da disciplina que o professor leciona: ")
  
  conn = conectar_banco()
  cursor = conn.cursor()
  cursor.execute('''INSERT INTO professores (nome, codigo, data_nascimento, genero, endereco, telefone, email, disciplina)VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        (nome, codigo, data_nasc, genero, endereco, telefone, email, disciplina))
  conn.commit()
  conn.close()
    
  print(f"Professor cadastrado com sucesso! Código : {codigo}") 

def listar_professores():
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()
    conn.close()

    if not professores:
        print("Nenhum professor cadastrado!")
    else:
        print("Professores cadastrados:")
        for professor in professores:
            print(f"ID: {professor[0]}, Nome: {professor[1]}, Código: {professor[2]}, Data de Nascimento: {professor[3]}, "
                  f"Gênero: {professor[4]}, Endereço: {professor[5]}, Telefone: {professor[6]}, Email: {professor[7]}, Disciplina: {professor[8]}")

def listar_professores_por_disciplina():
    disciplina_busca = input("Digite o código da disciplina: ")
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM professores WHERE disciplina = ?", (disciplina_busca,))
    professores_filtrados = cursor.fetchall()
    conn.close()

    if professores_filtrados:
        print(f"Professores que lecionam a disciplina {disciplina_busca}:")
        for professor in professores_filtrados:
            print(f"ID: {professor[0]}, Nome: {professor[1]}, Código: {professor[2]}")
    else:
        print(f"Nenhum professor encontrado para a disciplina {disciplina_busca}.") 