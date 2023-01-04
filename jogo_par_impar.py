import random

nome = input("Introduza um nome: ")
b = 0
Computador = random.randint(0,10)

while True:
    utilizador = input("Quer par ou impar? ")
    if (utilizador == "par" or utilizador == "impar"):
        break

if utilizador == "par":
    par = utilizador
    impar = Computador
elif utilizador == "impar":
    impar = utilizador
    par = Computador

numero = input("Digite o numero (0/10) ")
Computador = random.randint(1,10)

print("\n Computador escolheu ", Computador)
print(nome ,"Escolheu ", numero)

total = int(numero) + Computador
print ("A soma é: ", total)
computador = "0"

if total % 2 == 0:
    print("O Resultado é Par")
    Computador = "par"
else:
    print("O Resultado é Impar")
    Computador = "impar"

if utilizador == "par" and Computador == "par":
    print("Vencedor: ", nome)
elif utilizador == "impar" and Computador == "impar":
    print("Vencedor: ", nome)
else:
    print("Vencedor: ", Computador)