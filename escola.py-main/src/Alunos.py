import psycopg2

class Alunos:

    def __init__(self, id, nome, data_nascimento, documento, data_entrada, cursando):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.documento = documento
        self.data_entrada = data_entrada
        self.cursando = cursando

    def save_aluno(self):
        conn = psycopg2.connect("dbname=escola user=postgres password=minhasenha")
        cursor = conn.cursor()
        cursor.execute("insert into alunos (id, nome, data_nascimento, documento, data_entrada, cursando) values (%s, %s, %s, %s, %s, %s)",(self.id, self.nome, self.data_nascimento, self.documento, self.data_entrada, self.cursando))
        conn.commit()
        conn.close()
    
    def delete_aluno(self,id):
        conn = psycopg2.connect("dbname=escola user=postgres password=minhasenha")
        cursor = conn.cursor()
        cursor.execute("delete from alunos where id = %s",(id,))
        conn.commit()
        conn.close()

    def update_aluno(self, id, nome, data_nascimento, documento, data_entrada, cursando):
        conn = psycopg2.connect("dbname=escola user=postgres password=minhasenha")
        cursor = conn.cursor()
        cursor.execute("update alunos set nome = %s, data_nascimento = %s, documento = %s, data_entrada = %s, cursando = %s where id = %s",(nome, data_nascimento, documento, data_entrada, cursando, id))
        conn.commit()
        conn.close()