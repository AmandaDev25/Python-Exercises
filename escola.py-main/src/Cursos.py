import psycopg2

class Cursos:

    def __init__(self, id, nome, periodo):
        self.id = id
        self.nome = nome
        self.periodo = periodo

    def save_curso(self):
        conn = psycopg2.connect("dbname=escola user=postgres password=minhasenha")
        cursor = conn.cursor()
        cursor.execute("insert into cursos (id, nome, periodo) values (%s, %s, %s)",(self.id, self.nome, self.periodo))
        conn.commit()
        conn.close()
    
    def delete_curso(self,id):
        conn = psycopg2.connect("dbname=escola user=postgres password=minhasenha")
        cursor = conn.cursor()
        cursor.execute("delete from cursos where id = %s",(id,))
        conn.commit()
        conn.close()

    def update_curso(self, id, nome, periodo):
        conn = psycopg2.connect("dbname=escola user=postgres password=minhasenha")
        cursor = conn.cursor()
        cursor.execute("update cursos set nome = %s, periodo = %s where id = %s",(nome, periodo, id))
        conn.commit()
        conn.close()