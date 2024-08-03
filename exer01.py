nome = str(input("informe seu nome: "))
sobrenome = str(input("informe seu sobrenome: "))
idade = int(input("informe sua idade: "))
nascimento = int(input("informe sua data de nascimento: "))
altura = float(input("informe sua altura: "))

if idade >= 18:
    maior_idade = "é maior de idade"
else:
    maior_idade = "é menor de idade"


print(f"nome: {nome}")
print(f"sobrenome: {sobrenome}")
print(f"idade: {idade}")
print(f"ano de nascimento: {nascimento}")
print(f"é maior de idade ? {maior_idade}")
print(f"altura em metros: {altura}")