import aluno, professor, turma, disciplina
import time
from banco import criar_tabelas

# ------- MENU 

def menu():
  print('MENU')
  time.sleep(1)
  print("1 - Cadastrar Aluno")
  print("2 - Cadastrar Professsor")
  print("3 - Cadastrar Disciplina")
  print("4 - Cadastrar Turma")
  print("5 - Matricular Aluno em Turma")
  print("6 - Listar Alunos")
  print("7 - Listar Professores")
  print("8 - Listar Disciplinas")
  print("9 - Listar Turmas")
  print("10 - Filtrar Professores por Disciplina")
  print("11 - Alocar Disciplina em Turma")
  print("12 - Consultar Professores Alocados em Disciplinas")
  print("13 - Consultar Disciplinas Alocadas em Turmas")
  print("0 - Sair")
  
acoes = {
    '1': aluno.matricula,
    '2': professor.cadastrar_prof,
    '3': disciplina.cadastrar_disciplina,
    '4': turma.turma,
    '5': turma.matricular_aluno_em_turma,
    '6': aluno.listar_alunos,
    '7': professor.listar_professores,
    '8': disciplina.listar_disciplinas,
    '9': turma.listar_turmas,
    '10': professor.listar_professores_por_disciplina,
    '11': turma.alocar_disciplina_em_turma,
    '12': disciplina.consultar_professores_em_disciplinas,
    '13': turma.consultar_disciplinas_em_turma,
}

resp = ''
while resp != '0': 
  menu()  
  resp = input('Digite a opção desejada: ')
  
  if resp in acoes:
        acoes[resp]()  
        time.sleep(3)
  elif resp == '0':
        print("Saindo do sistema. Até mais!")
  else:
        print("Opção inválida! Tente novamente.")
        time.sleep(2)
