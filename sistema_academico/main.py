

import aluno, professor


# ------- MENU 

def menu():
  print('MENU')
  print('1 - Cadastrar Aluno')
  print('2 - Cadastrar Professsor')
  print('3 - Cadastrar Turma')
  print('0 - Sair')

resp = 1
while resp != '0':
  
  menu()

  
  resp = input('Digite a opção desejada: ')
  
  if resp == 1:
    aluno.matricula()
  elif resp == 2:
    professor.cadastrar_prof()
  


#aluno.matricula()

#aluno.print_student()