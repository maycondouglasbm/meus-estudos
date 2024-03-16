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

