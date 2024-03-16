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
