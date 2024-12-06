disciplinas = []

def disciplina():
  nome= input("Digite o nome da disciplina:")
  codigo= input("Digite o código da disciplina:")
  carga_horaria = input("Digite a carga horária da disciplina:")
  professor = input("Digite o professor da disciplina:")

  return {"nome" : nome, "codigo": codigo, "carga horária": carga_horaria, "professor": professor   }
