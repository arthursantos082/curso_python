# if e comparacao

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if int(primeiro_valor) > int(segundo_valor):
    print(f'O primeiro valor {primeiro_valor} é maior que o segundo valor {segundo_valor}')
elif int(segundo_valor) > int(primeiro_valor):
    print(f'O segundo valor {segundo_valor} é maior que o primeiro valor {primeiro_valor}') 

# ou

if int(primeiro_valor) > int(segundo_valor):
    print(f'O primeiro valor {primeiro_valor} é maior que o segundo valor {segundo_valor}')
else:
    print(f'O segundo valor {segundo_valor} é maior que o primeiro valor {primeiro_valor}')
