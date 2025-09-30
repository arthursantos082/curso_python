#Calculadora utilizando While

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    numero_1_float = 0
    numero_2_float  = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float  = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_validos = '+-/*'

    if operador not in operadores_validos:
        print('Digite apenas operadores válidos.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um númerador.')
        continue

    print('O resultado da sua conta é: ')
    if operador == '+':
        print(f'{numero_1_float}+{numero_2_float}=',numero_1_float + numero_2_float)
    
    elif operador == '-':
        print(f'{numero_1_float}-{numero_2_float}=',numero_1_float - numero_2_float)
    
    elif operador == '/':
        print(f'{numero_1_float}/{numero_2_float}=', numero_1_float / numero_2_float)
    
    elif operador == '*':
        print(f'{numero_1_float}*{numero_2_float}=', numero_1_float * numero_2_float)

    else:
        print('Não deveria chegar aqui.')
    
    sair = input(f'Deseja sair? [S]im/ ').lower().startswith('s')
    if sair == True:
        break