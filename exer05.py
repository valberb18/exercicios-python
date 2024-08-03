nome = input("Informe sua nome: ")
idade = input("Informe sua idade: ")

if nome != None and idade != None:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")

    if ' ' in nome:
        print("Seu nome contem espaços")
    else:
        print("Seu nome não contem espaços")

    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")

else:
    print("Nada foi digitado")