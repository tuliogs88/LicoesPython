# Tabuada das 4 operações

def calculadora() :

    n1 = int(input("Digite um valor: ")) 
    print ("1 - Multiplicação , 2 - Divisão, 3 - Adição, 4 - Subtração") 
    funcao = int(input ("Digite entre 1 até 4: ")) 
    contador = 1

    if (funcao == 1) :
        while contador < 11:
            resultado = n1 * contador
            print(f"{n1} * {contador} = {resultado}")
            contador += 1
    elif  (funcao == 2) :
        while contador < 11:
            resultado = n1 / contador
            print(f"{n1} / {contador} = {resultado}")
            contador += 1
    elif  (funcao == 3) :
        while contador < 11:
            resultado = n1 + contador
            print(f"{n1} + {contador} = {resultado}")
            contador += 1
    elif  (funcao == 4) :
        while contador < 11:
            resultado = n1 - contador
            print(f"{n1} - {contador} = {resultado}")
            contador += 1
    else :
        print("Digitou uma função que não existe")

calculadora ()
