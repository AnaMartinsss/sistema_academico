from random import choice, randint

alunos = []


def matricula():
  nome = input("Digite o nome do aluno:")
  matricula = _gerar_matricula()
  data_nasc = input("Digite a data de nascimento do aluno:") # date
  genero = _genero()
  endereco = input("Digite o endereco do aluno:")
  telefone = input("Digite o telefone do aluno:")
  email = input("Digite o e-mail do aluno:")
  alunos.append({"nome" : nome, "matricula": matricula, "data de nascimento": data_nasc, "genero do aluno" :genero, "endereço" : endereco , "telefone" : telefone, "email": email })

def _gerar_matricula():
    letra = choice(('A', 'B', 'C', 'D', 'E', 'F'))
    numero = str(randint(12300, 50000))
    return numero+'-'+letra

def _genero():
    while True:
     print(f'1 - Feminino')
     print(f'2 - Masculino')
     opcao = input("Digite a opção desejada (1 ou 2): ")
    
     if opcao == 1:
      print(f'Feminino')
     elif opcao == 2:
      print(f"Masculino")
     else:
      print(f'Opção invalida. Digite um número válido! (1 ou 2)')
    
def print_student():
    print(alunos)