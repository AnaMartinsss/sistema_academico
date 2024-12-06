from random import choice, randint

alunos = []


def matricula():
  nome = input("Digite o nome do aluno:")
  matricula = _gerar_matricula()
  data_nasc = input("Digite a data de nascimento do aluno:") # date
  sexo = input("Digite o sexo do aluno:")
  endereco = input("Digite o endereco do aluno:")
  telefone = input("Digite o telefone do aluno:")
  email = input("Digite o e-mail do aluno:")
  alunos.append({"nome" : nome, "matricula": matricula, "data de nascimento": data_nasc, "sexo do aluno" :sexo, "endereço" : endereco , "telefone" : telefone, "email": email })

def _gerar_matricula():
    letra = choice(('A', 'B', 'C'))
    numero = str(randint(12300, 50000))
    return numero+'-'+letra

def print_student():
    print(alunos)