import random

arquivo = open('arquivo.txt', 'r', encoding='utf-8')

palavras = []
for linha in arquivo.readlines():
    palavras.append(linha)

print('Bem vindo!')
print('Vamos ver se o computador lê sua mente?')
print('Você vai pensar em uma das 100 palavras mais buscadas no dicionário')
print('Após isso, o computador vai tentar advinhar essa palavra que você pensou.')
print('VAMOS LÁ:')
print('')

input('Aperte ENTER para começar...')
print('')

def adivinha():
    palpite = random.choice(palavras)

    print('A palavra que você pensou é...')
    print(f'* {palpite} *')
    print('')

    verificacao_palpite = input('Está correto(sim ou não)? ')
    verificacao_palpite = verificacao_palpite.lower()

    print('')

    if(verificacao_palpite == 'sim'):
        print('YEAH! A MÁQUINA VENCE!')
        print('Obrigado por jogar :)')
    elif(verificacao_palpite == 'não'):
        print('poxa :(')
        print('Ok... Você me venceu.')
        print('Obrigado por jogar :)')

adivinha()


