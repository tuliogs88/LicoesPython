# Calcular Média

def calcular_media_exercicio():

    import os
    os.system("cls")

    print("Seja bem vindo ao sistema de Notas!!! ")

    aluno = input ("Entre com o nome do aluno")

    portfolio = float(input("Digite a nota do portfólio: "))
    exer1 = float(input("Digite a nota do exercicio 1: "))
    exer2 = float(input("Digite a nota do exercicio 2: "))
    exer3 = float(input("Digite a nota do exercicio 3: "))
    exer4 = float(input("Digite a nota do exercicio 4: "))
    exer_fixacao = (exer1 + exer2 + exer3 + exer4) /4
    prova_eletronica = float(input("Digite a nota da prova: "))
    enade = float(input("Digite a nota do momento enade: "))
    

    nota_media = portfolio * 0.15 + exer_fixacao * 0.30 + prova_eletronica * 0.45 + enade * 0.10

    print("A media final é: {0:.2f}".format(nota_media))

    # Verificar a situação do aluno

    if (nota_media >= 6.0) :
        print(f"Você, {aluno} está aprovado com a média: {nota_media:.2f}")
        print("Você passou !!!")
    else:
        print(f"Você, {aluno} está reprovado com a média: {nota_media:.2f}")
        print("Você não passou, precisa reforçar os estudos !!!")

# Chamando a função

calcular_media_exercicio()
