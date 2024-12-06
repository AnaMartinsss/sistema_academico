professores = []
disciplina_prof = []

def cadastrar_prof():
  nome= input("Digite o nome do professor: ")
  matricula= input("Digite a matrícula do professor: ")
  data_nasc= input("Digite a data de nascimento do professor: ")
  sexo= input("Digite o sexo do professor: ")
  endereco= input("Digite o endereco do professor: ")
  telefone= input("Digite o telefone do professor: ")
  email= input("Digite o e-mail do professor: ")
  disciplina= input("Digite o código da disciplina do professor: ")
  return {"nome" : nome, "matricula": matricula, "data de nascimento": data_nasc, "sexo do aluno" :sexo, "endereço" : endereco , "telefone" : telefone, "email": email, "disciplina": disciplina }
