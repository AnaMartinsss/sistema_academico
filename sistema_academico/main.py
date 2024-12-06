

import aluno, professor, turma, disciplina


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
  elif resp == 3:
    turma.turma
  elif resp == '0':
        print("Saindo do sistema. Até mais!")
  else:
        print("Opção inválida! Tente novamente.")
  


#aluno.matricula()

#aluno.print_student()