#Projeto 1 
# Crie um sistema escolar que permita cadastrar alunos, professores, disciplina e turma.
# O sistema deve permitir a alocação de professores em disciplinas. 
# O sistema deve permitir a matrícula de alunos em turmas.
# O sistema deve permitir a alocação em disciplinas em turmas. 
# O sistema deve permitir a consulta de alunos matriculados em turmas.
# o sistema deve permitir a consulta de professores alocados em disciplinas.
# O sistema deve permitir a consulta de disciplinas alocadas em turmas.

# Alunos: nome, matrícula, data de nasc. , sexo, endereço, telefone e e-mail.
# Professores: nome, matrícula, data de nasc. , sexo, endereço, telefone, disciplina e e-mail,
# Disciplina: nome, código (A1234), carga horária, professor. 
# Turmas: nome, código (A1234), disciplina, professor, alunos (lista matrícula)

# O sistema deve permitir a filtragem de professor por disciplina

# Usar biblioteca que gera os nomes aleatórios

def cadastrar_aluno():
  nome= input("Digite o nome do aluno:")
  matricula= input("Digite a matrícula do aluno:")
  data_nasc= input("Digite a data de nascimento do aluno:")
  sexo= input("Digite o sexo do aluno:")
  endereco= input("Digite o endereco do aluno:")
  telefone= input("Digite o telefone do aluno:")
  email= input("Digite o e-mail do aluno:")
  return {"nome" : nome, "matricula": matricula, "data de nascimento": data_nasc, "sexo do aluno" :sexo, "endereço" : endereco , "telefone" : telefone, "email": email }

def cadastrar_prof():
  nome= input("Digite o nome do professor:")
  matricula= input("Digite a matrícula do professor:")
  data_nasc= input("Digite a data de nascimento do professor:")
  sexo= input("Digite o sexo do professor:")
  endereco= input("Digite o endereco do professor:")
  telefone= input("Digite o telefone do professor:")
  email= input("Digite o e-mail do professor:")
  disciplina= input("Digite a disciplina do professor:")
  return {"nome" : nome, "matricula": matricula, "data de nascimento": data_nasc, "sexo do aluno" :sexo, "endereço" : endereco , "telefone" : telefone, "email": email, "disciplina": disciplina }

def disciplina():
  nome= input("Digite o nome da disciplina:")
  codigo= input("Digite o código da disciplina:")
  carga_horaria = input("Digite a carga horária da disciplina:")
  professor = input("Digite o professor da disciplina:")

  return {"nome" : nome, "codigo": codigo, "carga horária": carga_horaria, "professor": professor   }


cadastrar_aluno()
cadastrar_prof()