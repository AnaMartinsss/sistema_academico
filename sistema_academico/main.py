

import aluno, professor, turma, disciplina




# ------- MENU 

def menu():
  print('MENU')
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
  print("0 - Sair")

resp = ''
while resp != '0':
  
  menu()

  
  resp = input('Digite a opção desejada: ')
  
  if resp == '1':
    aluno.matricula()
  elif resp == '2':
    professor.cadastrar_prof()
  elif resp == '3':
    disciplina.cadastrar_disciplina()
  elif resp == '4':
    turma.turma()
  elif resp == '5':
    turma.matricular_aluno_em_turma()
  elif resp == '6':
    aluno.listar_alunos()
  elif resp == '7':
    professor.listar_professores()
  elif resp == '8':
    disciplina.listar_disciplinas()
  elif resp == '9':
    turma.listar_turmas()
  elif resp == '10':
    professor.listar_professores_por_disciplina()
  elif resp == '0':
    print("Saindo do sistema. Até mais!")
  else:
    print("Opção inválida! Tente novamente.")
  


#aluno.matricula()

#aluno.print_student()