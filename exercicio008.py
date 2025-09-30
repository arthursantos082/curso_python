"""
Iterando strings com while
"""

nome = 'Arthur'
tamanho_nome = len(nome)
contador = 0
novo_nome = ''

while contador < tamanho_nome:
    letra = nome[contador]
    novo_nome += f'*{letra}'    
    contador += 1
 
print(f'{novo_nome}*')    