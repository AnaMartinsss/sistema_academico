import sqlite3
from random import choice, randint

def conectar_banco():
    return sqlite3.connect("sistema_academico.db")


def _gerar_codigo_turma():
    num = str(randint(1000, 9999))
    letra = choice(('A', 'B', 'C', 'D', 'E', 'F'))
    return num + letra

def turma():
  nome = input("Digite o nome da turma:")
  codigo = _gerar_codigo_turma()
  print(codigo)
  
  conn = conectar_banco()
  cursor = conn.cursor()
  cursor.execute('''INSERT INTO turmas (nome, codigo)VALUES (?, ?)''',
        (nome, codigo))
  conn.commit()
  conn.close()

  print(f"Turma {nome} cadastrada com sucesso! Código: {codigo}")
  
  
def matricular_aluno_em_turma():
    codigo_turma = input("Digite o código da turma: ")
    matricula_aluno = input("Digite a matrícula do aluno: ")
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM turmas WHERE codigo = ?", (codigo_turma,))
    turma = cursor.fetchone()
    if not turma:
        print("Turma não encontrada!")
        conn.close()
        return   

    cursor.execute("SELECT id FROM alunos WHERE matricula = ?", (matricula_aluno,))
    aluno = cursor.fetchone()
    if not aluno:
        print("Aluno não encontrado!")
        conn.close()
        return
    cursor.execute(
        '''INSERT INTO alunos_turmas (aluno_id, turma_id)
        VALUES (?, ?)''',
        (aluno[0], turma[0])
    )
    conn.commit()
    conn.close()

    print(f"Aluno com matrícula {matricula_aluno} matriculado na turma {codigo_turma} com sucesso!")


def listar_turmas():
   conn = conectar_banco()
   cursor = conn.cursor()

   cursor.execute("SELECT * FROM turmas")
   turmas = cursor.fetchall()
   conn.close()

   if not turmas:
        print("Nenhuma turma cadastrada!")
   else:
        print("Turmas cadastradas:")
        for turma in turmas:
            print(f"ID: {turma[0]}, Nome: {turma[1]}, Código: {turma[2]}")

            
def alocar_disciplina_em_turma(disciplinas):
    codigo_turma = input("Digite o código da turma: ")
    
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome FROM turmas WHERE codigo = ?", (codigo_turma,))
    turma = cursor.fetchone()
    if not turma:
        print("Turma não encontrada!")
        conn.close()
        return

    cursor.execute("SELECT * FROM disciplinas")
    disciplinas = cursor.fetchall()
    if not disciplinas:
        print("Nenhuma disciplina cadastrada!")
        conn.close()
        return

    print("Disciplinas disponíveis:")
    for disciplina in disciplinas:
        print(f"ID: {disciplina[0]}, Nome: {disciplina[1]}, Código: {disciplina[2]}")

    disciplina_id = input("Digite o ID da disciplina para alocar na turma: ")

    cursor.execute("SELECT * FROM disciplinas WHERE id = ?", (disciplina_id,))
    disciplina = cursor.fetchone()
    if not disciplina:
        print("Disciplina não encontrada!")
        conn.close()
        return


def consultar_disciplinas_em_turma():
   codigo_turma = input("Digite o código da turma para consulta: ")

   conn = conectar_banco()
   cursor = conn.cursor()

   cursor.execute("SELECT id, nome FROM turmas WHERE codigo = ?", (codigo_turma,))
   turma = cursor.fetchone()
   if not turma:
        print("Turma não encontrada!")
        conn.close()
        return

   cursor.execute('''SELECT d.nome FROM disciplinas_turmas dt JOIN disciplinas d ON dt.disciplina_id = d.id WHERE dt.turma_id = ?''',
    (turma[0],))
   disciplinas = cursor.fetchall()
   conn.close()

   if not disciplinas:
        print(f"A turma '{turma[1]}' não possui disciplinas alocadas.")
   else:
        print(f"Disciplinas alocadas na turma '{turma[1]}':")
        for disciplina in disciplinas:
            print(f"- {disciplina[0]}")