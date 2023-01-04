# Criar matriz 3 x 3 usando conceito de lista

matriz = [[1, 2, 3], [4, 5, 6] , [7, 8, 9]]
print("Matriz 3 x 3 ", matriz)

print ("\n\n Matriz impressa de outra forma")

for lista in matriz:
    for elemento in lista:
        print(elemento, end= ' ')
    print()
