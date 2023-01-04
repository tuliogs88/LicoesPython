from random import randint

print ('Bem-Vindo! \n')
sorteado = randint(1,100)
chute = 0

while chute != sorteado:
    chute = int(input ('Chute: '))
    if chute == sorteado:
        print ('Venceu! \n')
    if chute > sorteado:
        print ('Menor! \n')
    if chute < sorteado:
        print ('Maior! \n')
print ('Fim do jogo!')