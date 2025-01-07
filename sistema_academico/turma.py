from random import choice, randint
import aluno
turmas = []

def _gerar_codigo_turma():
    num = str(randint(1000, 9999))
    letra = choice(('A', 'B', 'C', 'D', 'E', 'F'))
    return num + letra

def turma():
  nome = input("Digite o nome da turma:")
  codigo = _gerar_codigo_turma()
  print(codigo)
  turmas.append({
    "nome" : nome,
    "codigo": codigo,
    "alunos" : []
    })
  print(f"Turma {nome} cadastrada com sucesso! Código: {codigo}")
  
  
def matricular_aluno_em_turma():
    codigo_turma = input("Digite o código da turma: ")
    matricula_aluno = input("Digite a matrícula do aluno: ")
    for turma in turmas:
        if turma['codigo'] == codigo_turma:
            turma['alunos'].append(matricula_aluno)
            print(f"Aluno {matricula_aluno} matriculado na turma {turma['nome']}.")
            return
    print("Turma não encontrada!")

def listar_turmas():
    if not turmas:
        print("Nenhuma turma cadastrada!")
    else:
        for turma in turmas:
            print(turma)
            
def alocar_disciplina_em_turma(disciplinas):
    if not turmas:
        print("Nenhuma turma cadastrada. Cadastre uma turma primeiro.")
        return
    if not disciplinas:
        print("Nenhuma disciplina cadastrada. Cadastre uma disciplina primeiro.")
        return

def consultar_disciplinas_em_turma():
    if not turmas:
        print("Nenhuma turma cadastrada.")
        return
    listar_turmas()
    turma_id = int(input("Digite o ID da turma para consulta: "))
    turma = next((t for t in turmas if t["id"] == turma_id), None)
    if not turma:
        print("Turma não encontrada.")
        return
    if not turma["disciplinas"]:
        print(f"A turma '{turma['nome_turma']}' não possui disciplinas alocadas.")
    else:
        print(f"Disciplinas alocadas na turma '{turma['nome_turma']}':")
        for disciplina in turma["disciplinas"]:
            print(f"- {disciplina['nome_disciplina']}")