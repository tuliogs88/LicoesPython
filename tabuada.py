# Fazer a tabuada 

# função 
  
def calcular(numero, opcao, oper, a):
  print(f"\n\n{oper}\n")
  for i in range(a):
    if(opcao=="+"):
      resultado=numero+i
      print(f"{numero} {opcao} {i} = {resultado}")
    elif(opcao=="-"):
      resultado=numero-i
      print(f"{numero} {opcao} {i} = {resultado}")
    elif(opcao=="/"):
      i+=1
      resultado=numero/i
      print(f"{numero} {opcao} {i} = {resultado}")
    elif(opcao=="*"):
      resultado=numero*i
      print(f"{numero} {opcao} {i} = {resultado}")
    else:
      print("Opção Inválida !!")
   
      

    
## Programa Principal 


continua=True
while(continua):
  numero=int(input("digite o numero da tabuada: "))
  opcao=input("Escolha a operação desejada (+ - / *): ")

  if opcao=="+":
    oper="ADIÇÃO"
    a=11
  elif opcao=="-":
    oper="SUBTRAÇAO"
    a=11
  elif opcao=="/":
    oper="DIVISAO"
    a=10
  elif opcao=="*":
    oper="MULTIPLICAÇÃO"
    a=11
  else:
    oper="Opção inválida "
    a=1
 
   
# Chamando subprogrma
  calcular(numero, opcao, oper, a)

# Continua 

  opcao=input("\n\n Deseja continuar ???  (S ou N): ")
  while(opcao.upper()!= "S" and  opcao.upper()!= "N"):
    opcao=input("Opção inválida !! --- Digite (S ou N)")
  if (opcao.upper()=="S"):
      continua=True
  else:
      continua=False


  
print("\n\n Fim de Programa !!!")
