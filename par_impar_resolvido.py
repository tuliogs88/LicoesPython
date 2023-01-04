import random

nome = input("Introduza um nome: ")
pontosPlayer = 0
pontosCPU = 0
Computador = random.randint(0,10)

while True:
    utilizador = input('{} ,quer par ou impar? '.format(nome))
    if (utilizador == "par" or utilizador == "impar"):
        break

while (pontosPlayer != 3 and pontosCPU != 3):
    if utilizador == "par":
        par = utilizador
        impar = Computador
    elif utilizador == "impar":
        impar = utilizador
        par = Computador

numero = input("Digite o numero (0/10) ")
Computador = random.randint(1,10)

print('Computador escolheu: {}' .format(Computador))
print('{} Escolheu: {} ' .format(nome, numero))
total = int(numero) + Computador

print ('A soma é: {}' .format(total))
computador = ''

if total % 2 == 0:
    print("O Resultado é Par")
    Computador = "par"
else:
    print("O Resultado é Impar")
    Computador = "impar"

if utilizador == "par" and Computador == "par":
    print('Vencedor: {}' .format(nome))
    pontosPlayer += 1
    print('Computador {} x {} {}' .format(pontosCPU, nome, pontosPlayer))
elif utilizador == "impar" and Computador == "impar":
    print('Vencedor: {}' .format(nome))
    pontosPlayer += 1
    print('Computador {} x {} {}' .format(pontosCPU, nome, pontosPlayer))
else:
    print("Vencedor: Computador")
    pontosCPU += 1
    print('Computador {} x {} {}' .format(pontosCPU, nome, pontosPlayer))

if pontosPlayer == 3:
    print("O grande vencedor foi o: {} com {} pontos" .format(nome, pontosPlayer))
else:
    print("O grande vencedor foi o: Computador com {} pontos" .format(pontosCPU))