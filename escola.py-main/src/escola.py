import psycopg2
from Alunos import Alunos
from Cursos import Cursos
from Professores import Professores

conn = psycopg2.connect("dbname=escola user=postgres password=minhasenha")
cursor = conn.cursor()
curso = Cursos(0,"",0)
aluno = Alunos(0,"",0,0,0,0)
professor = Professores(0,"",0,0)

usuario = input("Digite seu nome: \n")
print(f"Ola {usuario}, selecione uma das opções abaixo:")

def cursos():
    opcoes = ["1 -) Listar cursos", "2 -) Inserir um curso", "3 -) Atualizar um curso", "4 -) Excluir um curso", "0 -) Sair"] #Cria uma lista de opções para o usuário ver na tela
    while True:
        print(f"{usuario}, selecione uma das seguintes opções:")
        for opcao in opcoes:
            print(opcao)
        selecionada = int(input(""))
        if selecionada == 1:
            cursor.execute("select * from cursos")
            result = cursor.fetchall()
            print("Os cursos são:")
            print(result)
        elif selecionada == 2:
            id = input("Insira o id do curso\n")
            nome = input("Insira o nome do curso\n")
            periodo = input("Insira o periodo do curso\n")
            curso = Cursos(id,nome,periodo)
            curso.save_curso()
            print("Curso inserido\n")
        elif selecionada == 3:
            cursor.execute("select * from cursos")
            result = cursor.fetchall()
            print("Os cursos são:")
            print(result)
            id = input("insira o id do curso que você deseja atualizar\n")
            nome = input("Digite o novo nome:\n")
            periodo = input("Digite o novo período:\n")
            print("Curso atualizado!\n")
            curso.update_curso(id, nome, periodo)
        elif selecionada == 4:
            cursor.execute("select * from cursos")
            result = cursor.fetchall()
            print("Os cursos são:")
            print(result)
            id = input("insira o id do curso que você deseja apagar\n")
            curso.delete_curso(id) 
            print("Curso apagado!\n")    
        elif selecionada == 0:
            print("Você saiu do sistema!")
            break
        elif selecionada not in(0,1,2,3,4):
            print("Opção errada ou inexistente!")

def alunos():
    opcoes = ["1 -) Listar alunos", "2 -) Inserir um aluno", "3 -) Atualizar um aluno", "4 -) Excluir um aluno", "0 -) Sair"] #Cria uma lista de opções para o usuário ver na tela
    while True:
        print(f"{usuario}, selecione uma das seguintes opções:")
        for opcao in opcoes:
            print(opcao)
        selecionada = int(input(""))
        if selecionada == 1:
            cursor.execute("select * from alunos")
            result = cursor.fetchall()
            print("Os alunos são:")
            print(result)
        elif selecionada == 2:
            id = input("Insira o id do aluno\n")
            nome = input("Insira o nome do aluno\n")
            data_nascimento = input("Insira a data de nascimento do aluno\n")
            documento = input("Insira o documento do aluno\n")
            data_entrada = input("Insira a data de entrada do aluno\n")
            cursando = input("Insira se o aluno esta cursando ou não\n")
            aluno = Alunos(id,nome,data_nascimento,documento,data_entrada,cursando)
            aluno.save_aluno()
            print("Aluno inserido!\n")
        elif selecionada == 3:
            cursor.execute("select * from alunos")
            result = cursor.fetchall()
            print("Os alunos são:")
            print(result)
            id = input("insira o id do aluno que você deseja atualizar\n")
            nome = input("Digite o novo nome:\n")
            data_nascimento = input("Digite a nova data de nascimento:\n")
            documento = input("Digite o novo documento:\n")
            data_entrada = input("Digite a nova data de entrada:\n")
            cursando = input("Digite o novo status se esta cursando ou não:\n")
            print("Aluno atualizado!\n")
            aluno.update_aluno(id, nome, data_nascimento, documento, data_entrada, cursando)
        elif selecionada == 4:
            cursor.execute("select * from alunos")
            result = cursor.fetchall()
            print("Os alunos são:")
            print(result)
            id = input("insira o id do aluno que você deseja apagar\n")
            curso.delete_curso(id)
            print("Aluno apagado!\n")     
        elif selecionada == 0:
            print("Você saiu do sistema!")
            break
        elif selecionada not in(0,1,2,3,4):
            print("Opção errada ou inexistente!")

def professores():
    opcoes = ["1 -) Listar professores", "2 -) Inserir um professor", "3 -) Atualizar um professor", "4 -) Excluir um aluno", "0 -) Sair"] #Cria uma lista de opções para o usuário ver na tela
    while True:
        print(f"{usuario}, selecione uma das seguintes opções:")
        for opcao in opcoes:
            print(opcao)
        selecionada = int(input(""))
        if selecionada == 1:
            cursor.execute("select * from professores")
            result = cursor.fetchall()
            print("Os professores são:")
            print(result)
        elif selecionada == 2:
            id = input("Insira o id do professor\n")
            nome = input("Insira o nome do professor\n")
            data_nascimento = input("Insira a data de nascimento do professor\n")
            documento = input("Insira o documento do professor\n")
            professor = Professores(id,nome,data_nascimento,documento)
            professor.save_professor()
            print("Professor inserido!\n")
        elif selecionada == 3:
            cursor.execute("select * from professores")
            result = cursor.fetchall()
            print("Os professores são:")
            print(result)
            id = input("insira o id do professor que você deseja atualizar\n")
            nome = input("Digite o novo nome:\n")
            data_nascimento = input("Digite a nova data de nascimento:\n")
            documento = input("Digite o novo documento:\n")
            print("Professor atualizado!\n")
            aluno.update_professor(id, nome, data_nascimento, documento)
        elif selecionada == 4:
            cursor.execute("select * from professores")
            result = cursor.fetchall()
            print("Os professores são:")
            print(result)
            id = input("insira o id do professor que você deseja apagar\n")
            professor.delete_professor(id)
            print("Professor apagado!\n")     
        elif selecionada == 0:
            print("Você saiu do sistema!")
            break
        elif selecionada not in(0,1,2,3,4):
            print("Opção errada ou inexistente!")

opcoes = ["1-) Cursos","2-) Alunos","3-) Professores"]
for opcao in opcoes:
    print(opcao)
selecionada = int(input(""))
if selecionada == 1:
    cursos()
elif selecionada == 2:
    alunos()
elif selecionada == 3:
    professores()
elif selecionada not in(1,2,3):
    print("Opção errada ou inexistente!")