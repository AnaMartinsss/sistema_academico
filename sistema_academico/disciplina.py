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
