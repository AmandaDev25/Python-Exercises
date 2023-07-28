lista = [1, 10]

try:
    arquivo = open ('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 0
    numero = lista[1]
except ZeroDivisionError: 
    print('Não é possivel realizar divisão por 0')   
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmetica')
except IndexError :
    print('Erro ao acessar um indice invalido da lista')
except BaseException as ex:
    print('erro desconhecido. Erro {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    
