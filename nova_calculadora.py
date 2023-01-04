# Fazer a tabuada 

def calculadora():
    numero=int(input("digite o numero da tabuada: "))

# rotina de repetição para cálculo da tabuada
print("\n\n SOMA\n")

for i in range(11):
    resultado=numero+i
    print(f"{numero} + {i} = {resultado}")
    print("\n\n SUBTRAÇÃO\n") 

for i in range(11):
  resultado=numero-i
  print(f"{numero} - {i} = {resultado}")
print("\n\n DIVISÃO\n")

for i in range(10):
  i+=1 
  resultado=numero/i
  print(f"{numero} / {i} = {resultado}")
print("\n\n MULTIPLICAÇÃO\n") 

for i in range(11):
  resultado=numero*i
  print(f"{numero} * {i} = {resultado}")
print("\n\n") 


calculadora()
