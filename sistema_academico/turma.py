from random import choice, randint
turmas = []

def turma():
  nome = input("Digite o nome da disciplina:")
  codigo = _gerar_codigo_turma()
  carga_horaria = input("Digite a carga horária da disciplina:")
  professor = input("Digite o professor da disciplina:")
  lista_aluno = []
  turmas.append({
    "nome" : nome,
    "codigo": codigo,
    "carga horária": carga_horaria,
    "professor": professor
    })
  print(f"Turma {nome} cadastrada com sucesso! Código: {codigo}")
  
  def _gerar_codigo_turma():
    num = str(randint(125000, 650000))
    letra = choice(('A', 'B', 'C', 'D', 'E', 'F'))
    return num+letra
  
def matricular_aluno_em_turma():
    codigo_turma = input("Digite o código da turma: ")
    matricula_aluno = input("Digite a matrícula do aluno: ")
    for turma in turmas:
        if turma['código'] == codigo_turma:
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