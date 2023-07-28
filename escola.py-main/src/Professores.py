import psycopg2

class Professores:

    def __init__(self, id, nome, data_nascimento, documento):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.documento = documento
        
    def save_professor(self):
        conn = psycopg2.connect("dbname=escola user=postgres password=minhasenha")
        cursor = conn.cursor()
        cursor.execute("insert into professores (id, nome, data_nascimento, documento) values (%s, %s, %s, %s)",(self.id, self.nome, self.data_nascimento, self.documento))
        conn.commit()
        conn.close()
    
    def delete_professor(self,id):
        conn = psycopg2.connect("dbname=escola user=postgres password=minhasenha")
        cursor = conn.cursor()
        cursor.execute("delete from professores where id = %s",(id,))
        conn.commit()
        conn.close()

    def update_professor(self, id, nome, data_nascimento, documento):
        conn = psycopg2.connect("dbname=escola user=postgres password=minhasenha")
        cursor = conn.cursor()
        cursor.execute("update professores set nome = %s, data_nascimento = %s, documento = %s where id = %s",(nome, data_nascimento, documento, id))
        conn.commit()
        conn.close()