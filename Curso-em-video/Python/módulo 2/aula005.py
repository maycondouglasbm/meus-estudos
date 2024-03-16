
#43º exercício

peso = float(input('Qual o peso?'))
altura = float(input('Qual a altura?'))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('abaixo do peso')
elif imc > 18.5 and imc <= 24.99:
    print('peso ideal')
elif imc > 24.99 and imc <= 25:
    print('sobrepeso')
elif imc > 25 and imc <= 29.99:
    print('obesidade')
elif imc > 29.99 and imc <= 30:
    print('obesidade mórbida')

#44º exercício

print('-=' * 20)
valor = float(input('Qual o valor do produto?'))
print('-=' * 20)
print('''ESCOLHA UMA DAS OPÇÕES DE PAGAMENTO ABAIXO:
[1] A vista dinheiro/cheque: 10% de desconto
[2] A vista no cartão: 5% de desconto
[3] Em até 2x no cartão: preço normal
[4] Em 3x ou mais no cartão: 20% de juros''')
print('-=' * 20)
opção = int(input('Qual opção?'))
print('-=' * 20)
if opção == 1:
    total = valor - (valor * 10 / 100)
    parcela = total / 2
    print('O valor pago {:.0f} a vista dinheiro/cheque, ficará {:.2f}'.format(valor, total))
elif opção == 2:
    total = valor - (valor * 5 / 100)
    print('O valor pago {:.0f} ficará {:.2f}'.format(valor, total))
elif opção == 3:
    total = valor
    parcela = total / 2
    print('sua compra parcelada em 2x de {:.2f}'.format(parcela))
elif opção == 4:
    total = valor + (valor * 20 / 100)
    pac = int(input('Em quantas parcelas?'))
    parcelas = total / pac
    print('A compra de {:.0f} em {}x ficará {:.2f}'.format(valor, pac, parcelas))
    print('Sua compra de {:.0f} irá custar {} no final'.format(valor, total))
else:
    total = 0
    print("Opção invalida, tente novamente!")
print('-=' * 20)


#45º exercício:  desenvolver um programa que jogue pedra, papel e tesoura com você

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Escolha a sua opção:
[ 0 ] Pedra
[ 1 ] Papel 
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada?'))
print('Joken')
sleep(1)
print('POOO')
sleep(1)
print('<>' * 20)
print('o computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('<>' * 20)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('\033[0;30;44mJogador ganhou\033[m')
    elif jogador == 2:
        print('\033[0;31mComputador ganhou\033[m')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('\003[0;31mComputador ganhou\033[m')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('\033[0;30;44mJogador ganhou\033[m')
    else:
        print('jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('\033[0;30;44mJogador ganhou\033[m')
    elif jogador == 1:
        print('\033[0;31mComputador ganhou\033[m')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida')