import sqlite3
from random import choice, randint


def conectar_banco():
    return sqlite3.connect("sistema_academico.db")

def _gerar_codigo():
    num = str(randint(125000, 650000))
    letra = choice(('A', 'B', 'C', 'D', 'E', 'F'))
    return num+letra
  
def cadastrar_disciplina():
 nome = input("Digite o nome da disciplina:")
 codigo = _gerar_codigo()
 carga_horaria = input("Digite a carga horária da disciplina:")
 professor_nome = input("Digite o nome do professor responsável pela disciplina: ")
 conn = conectar_banco()
 cursor = conn.cursor()

 cursor.execute("INSERT INTO disciplinas (nome, codigo, carga_horaria, professor_nome) VALUES (?, ?, ?, ?)",
        (nome, codigo, carga_horaria, professor_nome),
    )

 conn.commit()
 conn.close()
 print(f"Disciplina '{nome}' cadastrada com sucesso! Código: {codigo}")


 
def listar_disciplinas():
    conn = conectar_banco()
    cursor = conn.cursor()

    # Selecionar disciplinas e exibir as informações
    cursor.execute("SELECT id, nome, codigo, carga_horaria, professor_nome FROM disciplinas")
    disciplinas = cursor.fetchall()
    conn.close()

    if not disciplinas:
        print("Nenhuma disciplina cadastrada!")
    else:
        print("Disciplinas cadastradas:")
        for disciplina in disciplinas:
            print(f"ID: {disciplina[0]}, Nome: {disciplina[1]}, Código: {disciplina[2]}, "
                  f"Carga Horária: {disciplina[3]}, Professor: {disciplina[4]}")
            
def consultar_professores_em_disciplinas(): 
    codigo_disciplina = input("Digite o código da disciplina para consulta: ")

    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT d.nome, p.nome FROM disciplinas d LEFT JOIN professores p ON d.professor_id = p.id WHERE d.codigo = ?",
        (codigo_disciplina,),
    )
    resultado = cursor.fetchone()
    conn.close()

    if not resultado:
        print("Disciplina não encontrada.")
    elif not resultado[1]:
        print(f"A disciplina '{resultado[0]}' não possui professor alocado.")
    else:
        print(f"O professor responsável pela disciplina '{resultado[0]}' é: {resultado[1]}")