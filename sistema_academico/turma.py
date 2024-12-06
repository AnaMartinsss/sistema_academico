from random import choice, randint
turmas = []

def turma():
  nome = input("Digite o nome da disciplina:")
  codigo = _gerar_codigo_turma()
  carga_horaria = input("Digite a carga horária da disciplina:")
  professor = input("Digite o professor da disciplina:")
  lista_aluno = []
  turmas.append({"nome" : nome, "codigo": codigo, "carga horária": carga_horaria, "professor": professor   })
  
  def _gerar_codigo_turma():
    num = str(randint(125000, 650000))
    letra = choice(('A', 'B', 'C', 'D', 'E', 'F'))
    return num+letra

