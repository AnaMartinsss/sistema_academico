import sqlite3

# Função para conectar ao banco de dados

def conectar_banco():
    conn = sqlite3.connect("sistema_academico.db")  # Cria o arquivo do banco de dados
    cursor = conn.cursor()
    return conn, cursor



# Função para criar as tabelas no banco de dados

def criar_tabelas():
    conn, cursor = conectar_banco()
    
    cursor.execute("DROP TABLE IF EXISTS professores")

    cursor.execute('CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, matricula TEXT, data_nascimento TEXT, genero TEXT, endereco TEXT, telefone TEXT, email TEXT)')
    cursor.execute('''CREATE TABLE disciplinas (id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT,codigo TEXT,carga_horaria TEXT,professor_nome TEXT)''')
    cursor.execute('CREATE TABLE IF NOT EXISTS turmas (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, codigo TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS alunos_turmas (id INTEGER PRIMARY KEY AUTOINCREMENT, aluno_id INTEGER, turma_id INTEGER)')
    cursor.execute('''CREATE TABLE IF NOT EXISTS disciplinas_turmas (id INTEGER PRIMARY KEY AUTOINCREMENT,disciplina_id INTEGER,turma_id INTEGER,FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id),FOREIGN KEY (turma_id) REFERENCES turmas(id) ) ''')
    cursor.execute('CREATE TABLE IF NOT EXISTS professores (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, codigo TEXT, data_nascimento TEXT, genero TEXT, endereco TEXT, telefone TEXT, email TEXT)')
       
    #TABELA PROFESSORES NÃO ESTÁ CRIANDO, AINDA NÃO CONSEGUI RESOLVER!
    
    conn.commit() 
    conn.close()
    print("Banco de dados e tabelas configurados com sucesso!")
    
    if __name__ == "__main__":
     criar_tabelas()
    
  