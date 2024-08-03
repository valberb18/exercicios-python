nome = str(input("Informe seu nome: "))
altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))

imc = peso / (altura * altura)

print(f"{nome} tem {altura} de altura")
print(f"pesa {peso} e seu imc é {imc}")