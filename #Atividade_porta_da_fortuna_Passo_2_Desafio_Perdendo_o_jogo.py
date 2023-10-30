#Atividade_porta_da_fortuna_Passo_2
# Desafio: Perdendo o Jogos

from random import *

#O usuário muda esta variável para terminar o jogo
jogando = True 
score = 0 
#Imprima as 3 portas e as instruções do jogo
print('''
Porta da Fortuna
=========

Existe um super prêmio atrás de uma destas 3 portas!
Advinhe qual é a porta certa para ganhar o prêmio!
  _____   _____   _____
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |   o | |   o | |   o |
 |_____| |_____| |_____|

''')
#repetir, enquanto a variável 'jogando' estiver com valor 'True'(verdadeiro)
while jogando == True:
    print("\nEscolha uma porta(1 , 2, ou 3):")
    # pegue a porta escolhida e armazene como um número inteiro
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)
    #escolha aleatoriamente a porta que esconde o prêmio ( entre 1 e 3)
    portaCerta = randint(1,3)

    #mostre ao jogador qual porta ele escolheu e qual era aporta certa
    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa foi a", portaCerta)

    #o jogador ganha se o número da porta escolhida e o da porta certa forem o mesmo
    if portaEscolhida == portaCerta:
        print("Parabéns!")
        score = score + 1
    else:
        print("Que peninha!")
        score = 0
    print(" Sua pontuação é ," ,score)
    print("\nVocê quer jogar de novo? (s/n)")
    resposta = input()
    if resposta == 'n':
        jogando = False
print('Obrigado por jogar!')
print("Sua pontuação final é de", score)
    