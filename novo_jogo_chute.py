from random import randint

print ('Bem-Vindo! \n')
sorteado = randint(1,100)
chute = 0
chances = 0

while chute != sorteado:
    chute = int(input ('Chute: '))
    if chute == sorteado:
        print ('Venceu! \n')
    if chute > sorteado:
        print ('Menor! \n')
        chances += 1
    if chute < sorteado:
        print ('Maior! \n')
        chances += 1
print ('Fim do jogo!')
chances += 1
print ("Voce teve ", chances ,"Chances para acertar")