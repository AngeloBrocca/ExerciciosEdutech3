import random

dados = open('dados.txt', 'a+')

ip = random.randrange(111111, 999999)
email = input('Insira seu e-mail: ')
nome = input('insira seu nome: ')

dados.writelines(f'{email} - {nome} - {ip}\n')
