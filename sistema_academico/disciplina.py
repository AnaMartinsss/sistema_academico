from random import choice, randint
disciplinas = []

def _gerar_codigo():
    num = str(randint(125000, 650000))
    letra = choice(('A', 'B', 'C', 'D', 'E', 'F'))
    return num+letra
  
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
        print(f"- Código: {disciplina['codigo']} | Nome: {disciplina['nome']}")
    codigo_disciplina = input("Digite o código da disciplina para consulta: ")

    for disciplina in disciplinas:
        if disciplina["codigo"] == codigo_disciplina:
            if not disciplina["professor"]:
                print(f"A disciplina '{disciplina['nome']}' não possui professor alocado.")
            else:
                print(f"O professor responsável pela disciplina '{disciplina['nome']}' é: {disciplina['professor']}")
            return
    print("Disciplina não encontrada.")