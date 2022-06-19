import random

print("="*32)
print("Bem Vindo ao Gerador de Senhas!")
print("="*32)

chars = 'abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ0123456789!@#$%&*<>,.?'

number = input('Diga quantas senhas deseja: ')
number = int(number)

lenght = input("Diga o tamanho da senha: ")
lenght = int(lenght)

print('\nAqui estão suas senhas: ')

for senha in range(number):
    senha = ''
    for c in range(lenght):
        senha += random.choice(chars)
    print(senha)
