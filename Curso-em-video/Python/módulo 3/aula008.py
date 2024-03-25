"""num = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
       'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
       'quinte', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    dig = int(input('Digite um número entre 0 e 20:'))
    if 0 <= dig <= 20:
        break
    print('tente novamente')
print(f'Você digitou o número {num[dig]}')

"""

## 
"""
from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Eu pensei nos números {num}')
print(f'O menor é {min(num)}')
print(f'O maior é {max(num)}')
"""

##
"""
num1 = (int(input('Digite um número:')), int(input('Digite outro número:')), int(input('Digite outro:')), int(input('Digite mais um:')))

print(f'O número 9 apareceu {num1.count(9)}x')

if 3 in num1:
    print(f'O 3 aparece na {num1.index(3)+1}ª posição')
else:
    print('O número 3 não aparece')
print('Os números pares que digitou foram:', end='')
for x in num1:
    if x % 2 == 0:
        print(x, end=' ')
"""

##
 
lista = ('Macarrão', 3.24,
         'Arroz', 8.90,
         'Feijão', 9.72,
         'cuscuz', 1,80,
         'alface', 0.97,
         'tomate', 1.00)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<20}', end='')
    else:
        print(f'{lista[pos]: >10}')