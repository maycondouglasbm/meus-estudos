#6º exercício

num = int(input('Digite um número para ver seu sucessor e antecessor:'))
s = num + 1
a = num - 1
print('O sucessor de {} é {} e o antecessor de {} é {}.' .format(num, s, num, a))

#7º exercício

Y = int(input('Digite um número para ver seu dobro, triplo e raiz:'))
D = Y * 2
T = Y * 3
R = Y ** (1/2)
print('O dobro de {} é igual a {:.2f},\nO triplo de {} é igual a {:.2f}, \nE a raiz quadrada de {} é igual a {:.0f}.'.format(Y, D, Y, T, Y, R))

#8º exercício

nota1 = int(input('Primeira nota:'))
nota2 = int(input('Segunda nota:'))
média = (nota1 + nota2) / 2
print('A média do aluno(a) é: {}' .format(média))

print('Outro método para ver se foi aprovado ou reprovado')

print('1° bimestre:')
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
média1 = (nota1 + nota2) / 2
print("A média do aluno(a) é: {}".format(média1))

print('-----------------------------------------------------------------------')

print('2° bimestre:')
nota1 = float (input('Primeira nota:'))
nota2 = float (input('Segunda nota:'))
média2 = (nota1 + nota2) / 2
print('A média do aluno(a) é: {}' .format(média2))

print('-----------------------------------------------------------------------')

print('3° bimestre:')
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
média3: float = (nota1 + nota2) / 2
print('A média do aluno(a) é: {}' .format(média3))

print('-----------------------------------------------------------------------')

print('4° bimestre:')
nota1 = float (input('Primeira nota:'))
nota2 = float (input('Segunda nota:'))
média4 = (nota1 + nota2) / 2
print('A média do aluno(a) é: {}' .format(média4))

print('-----------------------------------------------------------------------')
print('Olhe se você foi aprovado ou reprovado:')
print('-----------------------------------------------------------------------')

m1 = (média1 + média2 + média3 + média4)
print('A média total do aluno nos 4 bimestres é: {}'.format(m1))
if m1 >= 28:
    print('Parabéns, você foi aprovado!')
else:
    print('Reprovado...')

medida = float(input('Qual a medida em metros?'))
c = medida * 100
m = medida * 1000
print(' A medida {} em centimetros é {:.0f}cm e em milimetros é {:.0f}mm'.format(medida, c, m))

#9º exercício

num = int (input("Digite um número para ver a tabuada:"))
for i in range(0, 11):
    print(num, "x", i, "=", num * i)

# aaaaa

print('------------')

num1 = int(input('Digite um número:'))
print('{} * 1 = {}'.format(num1, num1 * 1)),
print('{} * 2 = {}'.format(num1, num1 * 2)),
print('{} * 3 = {}'.format(num1, num1 * 3)),
print('{} * 4 = {}'.format(num1, num1 * 4)),
print('{} * 5 = {}'.format(num1, num1 * 5)),
print('{} * 6 = {}'.format(num1, num1 * 6)),
print('{} * 7 = {}'.format(num1, num1 * 7)),
print('{} * 8 = {}'.format(num1, num1 * 8)),
print('{} * 9 = {}'.format(num1, num1 * 9)),
print('{} * 10 = {}'.format(num1, num1 * 10)),

#10º exercício

num = float(input('Quanto dinheiro em R$ você tem:'))
s = num / 5.15
print('Com R${} você poderá comprar U${:.2f}'.format(num, s))

# com o dolar valendo R$ 3,21
print('----------------------------------------------------------')

real = float(input('Quantos R$ você poderá compra dolares:'))
t = num / 3.21
print("Com R${} você pode comprar U${:.2f}".format(real, t)) 

#11º exercício

alt = float(input('Qual a altura?'))
larg = int(input('Qual a largura?'))
área = alt * larg
print('A área total é de {:.0f} metros'.format(área))
tinta = área / 2
print('A quantidade de tinta necessária para tintá-la é de {}l'.format(tinta))

#12º exercício

preço = float(input('Qual o preço do produto?'))
nov = preço - (preço * 5 / 100)
print("Esse preço com - 5% de desconto fica R${:.2f},".format(nov))

#13º exercício

salário = float(input('Qual o seu salário?'))
nv = salário + (salário * 15 / 100)
print('O salário R${} com 15% de aumento é igual a R${:.2f}'.format(salário, nv))

#14º exercício

temp = int(input("A temperatura em °c:"))
f = temp * 9 / 5 + 32
print('A temperatura {}°c é igual a {}°f'.format(temp, f))

#15º exercício

km = float(input('Qual a quantidade de quilometros pecorridos?'))
dias = int(input('Qual a quantidade de dias que foi alugado?'))
preço = (dias * 60) + (km * 0.15)
print('O total que ele terá a pagar po ter pecorrido {}km em {} dias será de R${:.2f}'.format(km, dias, preço))

#16º exercício

from math import trunc
num = float(input('Digite um número:'))
print('O número digitado foi {} e sua parte inteira é {}'.format(num, trunc(num)))

# outra forma sem importar o módulo

num = float(input('Digite um número:'))
print('O número digitado foi {} e sua parte inteira é {}'.format(num, int(num)))

