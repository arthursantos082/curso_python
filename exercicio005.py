#Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('Esse número é par.')
    else:
        print('Esse número é impar.')
except:
    print('Não é um número inteiro.')