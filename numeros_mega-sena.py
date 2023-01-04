# Criar uma sequencia de numeros

import random

#criar uma lista
mega-sena = []

# colocar os numeros

for i in range(6):
    mega-sena.append(random.randrange(1,60))

mega-sena.sort()

print (mega-sena)

mega-sena.sort(reverse=True)

print (mega-sena)
