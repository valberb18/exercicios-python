primeiro_valor = input("informe o primeiro valor: ")
segundo_valor = input("informe o segundo valor: ")

if primeiro_valor > segundo_valor:
    print(f"o primeiro valor: {primeiro_valor} é maior que o segundo valor: {segundo_valor}")
elif segundo_valor> primeiro_valor:
    print(f"o segundo valor: {segundo_valor} é maior que o primeiro valor: {primeiro_valor}")
elif primeiro_valor == segundo_valor:
    print(f"o primeiro valor: {primeiro_valor} e o segundo valor: {segundo_valor} tem valores iguais")