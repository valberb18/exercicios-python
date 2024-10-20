"""
Iterando strings com while
"""

nome = input("Informe seu nome: ")

tamanho_nome =  len(nome)

novo_nome = ''

passar = 0

while passar < tamanho_nome:
    letra = nome[passar]
    novo_nome += letra
    passar += 1


print(novo_nome)