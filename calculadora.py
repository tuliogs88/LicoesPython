# Tabuada das 4 operações

def calculadora() :

    n1 = int(input("Digite um valor: "))
    funcao = input ("Digite uma operação: ")
    contador = 0

    if (funcao == "Multiplicação") :
        while contador < 10:
            print(contador * n1)
            contador += 1
    elif  (funcao == "Divisão") :
        while contador < 10:
            print(contador / n1)
            contador += 1
    elif  (funcao == "Adição") :
        while contador < 10:
            print(contador + n1)
            contador += 1
    elif  (funcao == "Subtração") :
        while contador < 10:
            print(contador - n1)
            contador += 1
    else :
        print("Digitou uma função que não existe")

calculadora ()

    

    
