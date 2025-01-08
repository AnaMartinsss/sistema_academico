from random import choice, randint
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

    listar_turmas()
    turma_id = input("Digite o código da turma para alocar a disciplina: ")

    for turma in turmas:
        if turma["codigo"] == turma_id:
            print("Disciplinas disponíveis:")
            for disciplina in disciplinas:
                print(f"- Código: {disciplina['codigo']} | Nome: {disciplina['nome']}")
            disciplina_codigo = input("Digite o código da disciplina para alocação: ")
            for disciplina in disciplinas:
                if disciplina["codigo"] == disciplina_codigo:
                    if "disciplinas" not in turma:
                        turma["disciplinas"] = []
                    turma["disciplinas"].append(disciplina)
                    print(f"Disciplina '{disciplina['nome']}' alocada na turma '{turma['nome']}' com sucesso!")
                    return
            print("Disciplina não encontrada.")
            return
    print("Turma não encontrada.")


def consultar_disciplinas_em_turma():
    if not turmas:
        print("Nenhuma turma cadastrada.")
        return
    listar_turmas()
    turma_id = input("Digite o código da turma para consulta: ")
    for turma in turmas:
        if turma["codigo"] == turma_id:
            if not turma["disciplinas"]:
                print(f"A turma '{turma['nome']}' não possui disciplinas alocadas.")
            else:
                print(f"Disciplinas alocadas na turma '{turma['nome']}':")
                for disciplina in turma["disciplinas"]:
                    print(f"- {disciplina['nome']}")
            return
    print("Turma não encontrada.")