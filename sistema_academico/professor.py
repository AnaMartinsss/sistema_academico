from random import choice, randint
professores = []
disciplina_prof = []

def cadastrar_prof():
  nome = input("Digite o nome do professor: ")
  matricula = _gerar_mat_prof()
  data_nasc = input("Digite a data de nascimento: ")
  genero = _genero()
  endereco = input("Digite o endereço: ")
  telefone = input("Digite o telefone: ")
  email = input("Digite o e-mail: ")
  disciplina = input("Digite o código da disciplina: ")
  professores.append({"nome" : nome, "matricula": matricula, "data de nascimento": data_nasc, "sexo do aluno" :genero, "endereço" : endereco , "telefone" : telefone, "email": email, "disciplina": disciplina })

def _gerar_mat_prof():
    letra = choice(('A', 'B', 'C', 'D', 'E', 'F'))
    num = str(randint(120000, 55000))
    return letra+'-'+num

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