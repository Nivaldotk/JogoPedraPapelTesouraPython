from random import randint

# Cria uma lista com as Opções
t = ['Pedra', 'Papel', 'Tesoura']

# Coloca o computador para jogar dentro das opções
computador = t[randint(0, 2)]

# Coloca o jogador como False
jogador = False

while jogador == False:
    jogador = input('Pedra, Papel, Tesoura? ')
    if jogador == computador:
        print('Empate!')
    elif jogador == 'Pedra':
        if computador == 'Papel':
            print('Você Perdeu', computador, 'embrulha', jogador)
        else:
            print('Você venceu!', jogador, 'esmaga', computador)
    elif jogador == 'Papel':
        if computador == 'Tesoura':
            print('Você Perdeu', computador, 'corta', jogador)
        else:
            print('Você venceu!', jogador, 'embrulha', computador)
    elif jogador == 'Tesoura':
        if computador == 'Pedra':
            print('Você Perdeu', computador, 'esmaga', jogador)
        else:
            print('Você venceu!', jogador, 'corta', computador)
    else:
        print('Essa não é uma jogada válida. Verifique a ortografia!')

    # Para continuar o jogo
    jogador = False
    computador = t[randint(0, 2)]