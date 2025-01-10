import sqlite3
from random import choice, randint
from datetime import datetime
from time import time

def conectar_banco():
    return sqlite3.connect("sistema_academico.db")

def _gerar_matricula():
    letra = choice(('A', 'B', 'C', 'D', 'E', 'F'))
    numero = str(randint(12300, 50000))
    return numero+'-'+letra

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

def matricula():
  nome = input("Digite o nome do aluno:")
  matricula = _gerar_matricula()
  while True:
   data_nasc = input("Digite a data de nascimento do aluno (DD/MM/AAAA): ")
   data_validada = validar_data(data_nasc)
   if data_validada:
     break
   else:
    print("Data inválida! Por favor, insira no formato DD/MM/AAAA.")
    time.sleep(1.5)
  genero = _genero()
  endereco = input("Digite o endereco do aluno:")
  telefone = input("Digite o telefone do aluno:")
  email = input("Digite o e-mail do aluno:")
  
  conn = sqlite3.connect("sistema_academico.db")
  cursor = conn.cursor()

  cursor.execute('''INSERT INTO alunos (nome, matricula, data_nascimento, genero, endereco, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)''',
    (nome, matricula, data_nasc, genero, endereco, telefone, email))
  
  conn.commit()
  conn.close()
  
  print(f"Aluno cadastrado com sucesso! Matricula : {matricula}")

      
def listar_alunos():
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall() #vai me retornar todas as linhas
    conn.close()

    if not alunos:
        print("Nenhum aluno cadastrado!")
    else:
        print("Alunos cadastrados:")
        for aluno in alunos:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Matrícula: {aluno[2]}, Data de Nascimento: {aluno[3]}, "
                  f"Gênero: {aluno[4]}, Endereço: {aluno[5]}, Telefone: {aluno[6]}, Email: {aluno[7]}")


def matricular_em_turma():
    aluno_matricula = input("Digite a matrícula do aluno: ")
    turma_codigo = input("Digite o código da turma: ")
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM alunos WHERE matricula = ?", (aluno_matricula,))
    aluno = cursor.fetchone() # vai me retornar uma linha
    if not aluno:
        print("Aluno não encontrado!")
        conn.close()
        return

    cursor.execute("SELECT id FROM turmas WHERE codigo = ?", (turma_codigo,))
    turma = cursor.fetchone()
    if not turma:
        print("Turma não encontrada!")
        conn.close()
        return

    cursor.execute(f"INSERT INTO alunos_turmas (aluno_id, turma_id) VALUES (?, ?)({aluno[0]}, {turma[0]})")

    conn.commit()
    conn.close()

    print(f"Aluno com matrícula {aluno_matricula} matriculado na turma {turma_codigo} com sucesso!")
    
