import random

print('Bem vindo ao Jogo da Adivinhação!')
print('Você deve adivinhar um número de 0 a 100.')
print('Você tem apenas 10 chances. VAMOS LÁ!')
print('')


def retornaNumeroAleatorio():
    numero = random.randrange(0, 100)
    return numero

numero_correto = retornaNumeroAleatorio()

def daPalpite():
    palpite = int(input('Insira seu palpite: '))
    return palpite

palpite = daPalpite()

tentativas = 10

while tentativas > 0:
    if(palpite == numero_correto):
        print('Você acertou! Parabéns!')
        break
    else:
        
        if(palpite > numero_correto - 15 and palpite < numero_correto + 15):
            print('TA QUENTE!!!!!')
        else:
            print('TA FRIO!!!!!')

        if(palpite > numero_correto):
            
            print('Você errou! O número correto é menor.')
            print('Vamos, tente de novo...')
            palpite = daPalpite()

        elif(palpite < numero_correto):

            print('Você errou! O número correto é maior.')
            print('Vamos, tente de novo...')
            palpite = daPalpite()

        tentativas -= 1
    
    if(tentativas == 0):
        print('Infelizmente você não tem mais tentativas restantes :(')
        print('Você perdeu :(')
    else:
        if(palpite == numero_correto):
            pass
        else:
            print(f'Tentativas que restaram: {tentativas}')    
            
