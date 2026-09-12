# Jogo de pedra, papel e tesoura

jogada_primeiro_usuario = input('Player 1, Escolha sua jogada: ')
jogada_segundo_usuario = input('Player 2, Escolha sua jogada: ')

if jogada_primeiro_usuario == jogada_segundo_usuario:
    print ('Empate!')

elif jogada_primeiro_usuario == 'pedra' and jogada_segundo_usuario == 'tesoura':
    print ('Vitória do Player 1')

elif jogada_primeiro_usuario == 'pedra' and jogada_segundo_usuario == 'papel':
    print ('Vitória do Player 2')

elif jogada_primeiro_usuario == 'tesoura' and jogada_segundo_usuario == 'pedra':
    print ('Vitória do Player 2')

elif jogada_primeiro_usuario == 'tesoura' and jogada_segundo_usuario == 'papel':
    print ('Vitória do Player 1')

elif jogada_primeiro_usuario == 'papel' and jogada_segundo_usuario == 'tesoura':
    print ('Vitória do Player 2')

elif jogada_primeiro_usuario == 'papel' and jogada_segundo_usuario == 'pedra':
    print ('Vitória do Player 1')

else: 
    print('Jogada Inválida, Erro de Digitação')