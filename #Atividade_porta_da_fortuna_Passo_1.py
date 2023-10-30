#Atividade_porta_da_fortuna_Passo_1
# Porta da da Fortuna

from random import *

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

Escolha uma porta (1, 2 or 3):
''')

#pegue a porta escolhida e armazene como um numero inteiro 
portaEscolhida = input()
portaEscolhida = int(portaEscolhida)

#escolha aleatoriamente a porta que esconde o prêmio ( entre 1 e 3)
portaCerta = randint(1,3)

#smostre ao jogador qual porta ele escolheu e qual era aporta certa
print("A porta escolhida foi a", portaEscolhida)
print("A porta certa foi a", portaCerta)

#o jogador ganha se o número da porta escolhida e o da porta certa forem o mesmo
if portaEscolhida == portaCerta:
    print("Parabéns!")
else:
    print("Que peninha!")