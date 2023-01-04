# Calcular Média

def calcular_media_exercicio():

    
    print("Seja bem vindo ao sistema de Notas!!! ")

    aluno = input ("Entre com o nome do aluno")

    portfolio = float(input("Digite a nota do portfólio: "))
    while (portfolio < 0 or portfolio >= 10):
        portfolio = float(input("Nota inválida --- Digite entre 0 até 10 "))
        
    exer1 = float(input("Digite a nota do exercicio 1: "))
    while (exer1 < 0 or exer1 >= 10):
        exer1 = float(input("Nota inválida --- Digite entre 0 até 10 "))
                      
    exer2 = float(input("Digite a nota do exercicio 2: "))
    while (exer2 < 0 or exer2 >= 10):
        exer2 = float(input("Nota inválida --- Digite entre 0 até 10 "))
                      
    exer3 = float(input("Digite a nota do exercicio 3: "))
    while (exer3 < 0 or exer3 >= 10):
        exer3 = float(input("Nota inválida --- Digite entre 0 até 10 "))
        
    exer4 = float(input("Digite a nota do exercicio 4: "))
    while (exer4 < 0 or exer4 >= 10):
        exer4 = float(input("Nota inválida --- Digite entre 0 até 10 "))
        
    exer_fixacao = (exer1 + exer2 + exer3 + exer4) /4
    
    prova_eletronica = float(input("Digite a nota da prova: "))
    while (prova_eletronica < 0 or prova_eletronica >= 10):
        prova_eletronica = float(input("Nota inválida --- Digite entre 0 até 10 "))
        
    enade = float(input("Digite a nota do momento enade: "))
    while (enade < 0 or enade >= 10):
        enade = float(input("Nota inválida --- Digite entre 0 até 10 "))
    

    nota_media = portfolio * 0.15 + exer_fixacao * 0.30 + prova_eletronica * 0.45 + enade * 0.10

    print("A media final é: {0:.2f}".format(nota_media))

    # Verificar a situação do aluno

    if (nota_media >= 6.0) :
        print(f"Você, {aluno} está aprovado com a média: {nota_media:.2f}")
        print("Você passou !!!")
    else:
        print(f"Você, {aluno} está reprovado com a média: {nota_media:.2f}")
        print("Você não passou, precisa reforçar os estudos !!!")

calcular_media_exercicio()
