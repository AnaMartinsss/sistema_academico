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
  
  professores.append({
    "nome" : nome,
    "matricula": matricula,
    "data de nascimento": data_nasc,
    "sexo do aluno" :genero,
    "endereço" : endereco,
    "telefone" : telefone,
    "email": email,
    "disciplina": disciplina 
    })
print(f"Professor cadastrado com sucesso!")
 
def _gerar_mat_prof():
    letra = choice(('A', 'B', 'C', 'D', 'E', 'F'))
    num = str(randint(12000, 55000))
    return letra+'-'+num

def _genero():
     while True:
      print(f"1 - Feminino")
      print(f"2 - Masculino")
      opcao = input("Digite a opção desejada (1 ou 2): ")
      
      if opcao == '1':
       return "Feminino"
      elif opcao == '2':
       return "Masculino"
      else:
       print(f"Opção invalida. Digite um número válido! (1 ou 2)")
      
def listar_professores():
    if not professores:
        print("Nenhum professor cadastrado!")
    else:
        for professor in professores:
            print(professor)
            
def listar_professores_por_disciplina():
    disciplina_busca = input("Digite o nome da disciplina: ")

    professores_filtrados = [professor for professor in professores if professor["disciplina"].lower() == disciplina_busca.lower()]

    if professores_filtrados:
        print(f"Professores que lecionam a disciplina {disciplina_busca}:")
        for professor in professores_filtrados:
            print(f"Nome: {professor['nome']}, Matrícula: {professor['matricula']}")
    else:
        print(f"Nenhum professor encontrado para a disciplina {disciplina_busca}.")
    