from email import message
from msilib.schema import SelfReg
from typing_extensions import Self


class Error (Exception):
    pass

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)

        break
    except ValueError:
        print('Valor invalido. Deve-se digitar apenas números')