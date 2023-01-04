# Calcular Média

# Função

def calcular_media():

    import os
    os.system("cls")

    print("Seja bem vindo ao sistema de Notas!!! ")

    aluno = input ("Entre com o nome do aluno")
    RA = input ("Entre com a Matricula")

    portfolio = float(input("Digite a nota do portfólio: "))
    exer_fixacao = float(input("Digite a nota dos exercicios de fixação: "))
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

calcular_media()
