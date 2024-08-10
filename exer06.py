bom_dia = float_horario >= 0 and float_horario <= 11
boa_tarde = float_horario >= 12 and float_horario <= 17
boa_noite = float_horario >= 18 and float_horario <= 23

if bom_dia:
    print("Bom dia")

if boa_tarde:
    print("Boa tarde")

if boa_noite:
    print("Boa noite")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Informe seu nome: ")

tamanho_do_nome = len(nome)

if tamanho_do_nome <= 4:
    print("Seu nome é curto")

if tamanho_do_nome >= 5 and tamanho_do_nome <=6:
    print("Seu nome é normal")

if tamanho_do_nome > 6:
    print("Seu nome é muito grande ")