#simulação das operações de um caixa eletônico:

# um subprograma da operação de transação: operacao_transacao()
# Este subprograma chama outros subrogramas
def operacao_transacao():
   
    mensagem_abertura() # chamada do subprograma: mensagem_abertura()

    saldo = float(input("Entre com seu saldo ")) #saldo inicial

    continua = True # uma variável booleana (True ou False)

    while (continua):

        menu() # chamada do subrograma: menu()

        opcao = int(input("Escolhe sua opcao ! "))   

        if (opcao == 1):
            saldo = deposito(saldo)  # chamando o subprograma: deposito(saldo)
        elif (opcao == 2):
            saldo = saque(saldo)  # chamando o subprograma: saque(saldo)
        elif (opcao == 3):
            consulta(saldo) # chamando o subprograma: consulta(saldo)
        elif (opcao == 4):
            encerra_transacao() # chamando o subprograma: encerra_transacao()
            continua = not opcao == 4
        else :
            print("Por favor, digite opções entre 1 até 4")
        
        
    input("Fim das transacoes !") 

#um subprograma: mensagem_abertura()    
def mensagem_abertura():
    print("******************************************")
    print("Bem vindo à transação no caixa eletrônico!")
    print("******************************************")

#um subprograma: menu()
def menu():    
    print("\n\n Menu para sua transação : ")
    print("(1) Deposito (2) Saque (3) Saldo (4) Sair \n")
    print()   

#um subprograma como uma função : deposito(saldo) com parâmetro saldo
def deposito(saldo):
    valor = float(input("Valor do deposito: R$ "))
    saldo += valor  # saldo = saldo + valor atualizando o valor do saldo - acumulador 
    return saldo

#um subprograma como uma função : saque(saldo) com parâmetro saldo
def saque(saldo):
    valor = float(input("Valor do saque: R$ "))
    if (valor > saldo):
        print("Infelizmente o saldo insuficiente e verifique seu saldo:")
    else:
        saldo -= valor  # saldo = saldo - valor atualizando o valor do saldo
    return saldo

#um subprograma: consulta(salto) com parâmetro saldo
def consulta(saldo):
    print("Saldo atual: R$ {:.2f} ".format(saldo))

#um subprograma: encerra_transacao()
def encerra_transacao():
    print("Encerrando programa ! ")

#programa principal chama subprograma operacao_transacao() para executar
operacao_transacao()
