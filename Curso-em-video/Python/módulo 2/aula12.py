#36º exercício

valor = float(input('Qual o valor da casa?'))
s = float(input('Qual o salário?'))
a = int(input('Em quantos anos pretende pagar?'))
prestacao = valor / (a * 12)
min = s * 30 /100
print('Para pagar a casa em {}anos'.format(a), end='')
print('a prestação será de {}'.format(prestacao))
if prestacao >= min:
    print('O emprestimo foi negado')
else:
    print('o emprestimo foi aprovado')

#37º exercício

num = int(input('Digite um número inteiro:'))
print('''Escolha uma opção:'
[1] converta para binário
[2] converta para actual
[3] converta para hexadecimal''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('O valor {} inteiro em binários é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} em actual é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} em hexadecimal é {}'.format(num, hex(num)[:2]))
else:
    print('Tente novamente...')

#38º exercício

n1 = float(input('digite um número:'))
n2 = float(input('digite outro:'))
if n1 > n2:
    print('o primeiro número é maior')
elif n2 > n1:
    print('o segundo numero é maior')
else:
    print('Não existe valor maior, os dois são iguais')

#39º exercício

print("-=-" * 20)

from datetime import date
ano_atual = date.today().year
data = int(input('Em qual ano você nasceu?'))
print("-=-" * 20)
idade = ano_atual - data
print('Quem nasceu em {} tem {} anos em {}'.format(data,idade, ano_atual))
print("-=-" * 20)
if idade == 18:
    print('você irá se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('ainda falta {} ano(s) para o seu alistamento'.format(saldo))
    ano = ano_atual + saldo
    print('O ano que você irá se alistar é {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Já se passaram {} ano(s) do seu alistamento'.format(saldo))
    ano = ano_atual - saldo
    print('o ano que você deveria ter se alistado era {}'.format(ano))

#40º exercício

nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
média = (nota1 + nota2) / 2
if média >= 7:
    print('Aprovado!')
elif média >= 5 or média <= 6.9:
    print('Recuperação')
elif média < 7:
    print('Reprovado!')

#41º exercício

ano = int(input('Ano de nascimento:'))
if ano >=5 and ano <=9:
    print('categoria mirim')
elif ano >9 and ano <=14:
    print('categoria infántil')
elif ano >14 and ano <=19:
    print('categoria Junior')
elif ano >19 and ano <=20:
    print('categoria sênior')
elif ano >20 :
    print('categoria master')

#42º exercício

print('-=-' * 20)
print("analisador de triangulos")
print('-=-' * 20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem formar triangulos')
    if r1 == r2 == r3:
      print('Todos os lados são iguais, EQUIÁTERO')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
      print('Dois lados são iguais, ISOSCELES')
    else:
      print('Todos os lados diferentes, ESCALENO')
else:
    print('Não podem formar triângulos')


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