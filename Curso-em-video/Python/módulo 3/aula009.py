#78º exercício

lista = []
for x in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {x}:')))
print('=-=' * 20)
print(f'Você digitou os valores {lista}')
maior = max(lista)
menor = min(lista)
print(f'O maior valor digitado foi {maior} na posição {lista.index(maior)}')
print(f'O menor valor digitado foi {menor} na posição {lista.index(menor)}')


#79º exercício

num = list()

while True:
    n = int(input('Digite um número:'))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, não vou adcionar')
    r = str(input('Dejesa continuar? [s/n]'))
    if r in 'Nn':
        break
print('=-=' * 20)
num.sort()
print(f'Os valores que você digitou foi {num}')


#80º exercício

valores = list()
while True:
    valores.append(int(input('Digite um número:')))
    peg = str(input('Quer continuar? [S/N]'))
    if peg in 'Nn':
        break
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 not in valores:
    print('O valor 5 não foi encontrado na lista!')


#81º exercício

lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um número:')))
    pg = str(input('Quer continuar? [S/N]'))
    if pg in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    if v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {lista}')
pares, impares.sort()
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')


#82º exercício

