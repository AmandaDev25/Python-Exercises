# Conversor de Unidades: Graus Celsius e Fahrenheit

def menu_inicial():
    print('Programa para Conversão de Temperaturas')
    print('1. Converter de Celsius para Fahrenheit')
    print('2. Converter de Fahrenheit para Celsius')
    print('3. Converter de Celsius para Kelvin')

def cel_fahr():
    C = float(input('Entre com a temperatura em graus Celsius: '))
    F = C * (9 / 5) + 32
    print('Valor em Fahrenheit: {0}°F'.format(F))

def fahr_cel():
    F = float(input('Entre com a temperatura em graus Fahrenheit: '))
    C = (F - 32) * (5 / 9)
    print('Valor em Celsius: {0}°C'.format(C))

def cel_kel():
    C = float(input('Entre com a temperatura em graus Kelvin: '))
    K = (C + 32) * (5 / 9)
    print('Valor em Kelvin: {0}°C'.format(C))



if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de conversão que deseja realizar: ')

    if escolha == '1':
        cel_fahr()

    if escolha == '2':
        fahr_cel()
    
    if escolha == '3':
        fahr_cel()