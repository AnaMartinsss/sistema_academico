from random import choice, randint
disciplinas = []

def cadastrar_disciplina():
  nome = input("Digite o nome da disciplina:")
  codigo = _gerar_codigo()
  carga_horaria = input("Digite a carga horária da disciplina:")
  professor = input("Digite o professor da disciplina:")
  disciplinas.append({
    "nome" : nome,
    "codigo": codigo,
    "carga horária": carga_horaria,
    "professor": professor  
    })
  print(f"Disciplina {nome} cadastrada com sucesso! Código: {codigo}")

def _gerar_codigo():
    num = str(randint(125000, 650000))
    letra = choice(('A', 'B', 'C', 'D', 'E', 'F'))
    return num+letra
  
def listar_disciplinas():
    if not disciplinas:
        print("Nenhuma disciplina cadastrada!")
    else:
        for disciplina in disciplinas:
            print(disciplina)

def consultar_professores_em_disciplinas():
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return
    print("Disciplinas cadastradas:")
    for disciplina in disciplinas:
        print(f"- ID: {disciplina['id']} | Nome: {disciplina['nome_disciplina']}")
    disciplina_id = int(input("Digite o ID da disciplina para consulta: "))
    disciplina = next((d for d in disciplinas if d["id"] == disciplina_id), None)
    if not disciplina:
        print("Disciplina não encontrada.")
    elif "professor" not in disciplina or not disciplina["professor"]:
        print(f"A disciplina '{disciplina['nome_disciplina']}' não possui professor alocado.")
    else:
        print(f"O professor responsável pela disciplina '{disciplina['nome_disciplina']}' é: {disciplina['professor']['nome']}")