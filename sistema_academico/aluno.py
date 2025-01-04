from random import choice, randint
import turma
alunos = []


def matricula():
  nome = input("Digite o nome do aluno:")
  matricula = _gerar_matricula()
  data_nasc = input("Digite a data de nascimento do aluno:") # date
  genero = _genero()
  endereco = input("Digite o endereco do aluno:")
  telefone = input("Digite o telefone do aluno:")
  email = input("Digite o e-mail do aluno:")
  
  alunos.append({
    "nome" : nome,
    "matricula": matricula,
    "data de nascimento": data_nasc,
    "genero do aluno" :genero,
    "endereço" : endereco ,
    "telefone" : telefone,
    "email": email })
  
  print(f"Aluno cadastrado com sucesso!")
  
def _gerar_matricula():
    letra = choice(('A', 'B', 'C', 'D', 'E', 'F'))
    numero = str(randint(12300, 50000))
    return numero+'-'+letra

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
      
def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado!")
    else:
        for aluno in alunos:
            print(aluno)
            

def matricular_em_turma():
    aluno_matricula = input("Digite a matrícula do aluno: ")
    turma_codigo = input("Digite o código da turma: ")

    turma = next((t for t in turma.turmas if t['codigo'] == turma_codigo), None)
    if turma:
        
        aluno = next((a for a in alunos if a['matricula'] == aluno_matricula), None)
        if aluno:
            turma['alunos'].append(aluno_matricula)
            print(f"Aluno {aluno_matricula} matriculado na turma {turma_codigo}.")
        else:
            print("Aluno não encontrado!")
    else:
        print("Turma não encontrada!")   
        
def print_student():
    print(alunos)