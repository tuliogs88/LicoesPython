# Importar Random

import random

# numeros

nome = input("Entre com seu nome ")
idade = int(input("Entre com a sua idade "))

if (idade >= 18):
    print("Você pode jogar!!!")

    print("Como você quer fazer o jogo? 1 - Escolhendo você mesmo, 2 - Modo Aleatório ")
    opcao = input("Entre com a sua opção ")

    if (opcao == 1):
        n = int(("Quantos numeros você deseja "))
        if (n > 5 and n <= 15):
             numero = 1
             while numero < n:
                 jogo = []
                 opcao_jogo = input("Escolha entre 1 até 60")
                 jogo.append(opcao_jogo)
                 numero += 1

        else:
            print("Escolha entre 6 até 15 numeros para jogar ")
    return jogo

    elif (opcao == 2):
        n = int(("Quantos numeros você deseja "))
        if (n > 5 and n <= 15):
            numero = 1
            while  numero < n:
                jogo = []
                numero_randomico = random.randrange(1,60)
                jogo.append(numero_randomico)
                numero += 1

        else:
            print("Escolha entre 6 até 15 numeros para jogar ")

        return jogo
    else:
        print("Escolha entre 6 até 15 numeros para jogar ")

else:
    print("Escolha entre 1 até 2 para jogar (1 - Escolhendo você mesmo, 2 - Modo Aleatório)")
