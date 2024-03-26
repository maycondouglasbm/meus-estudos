#53º exercício

fras = str(input('digite uma frase: ')).strip().upper()
palavras = fras.split()
junta = ''.join(palavras)
inverso = junta[::-1]
print('o inverso de {} é {}'.format(junta, inverso))
if inverso == junta:
    print('é um palidromo')
else:
    print('não é um palidromo')


#54º exercício

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    ano = int(input('Qual o ano de nascimento do {}º?'.format(i)))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('temos {} de maior'.format(totmaior))
print('temos {} de menor'.format(totmenor))  

#55º exercício

maior = 0
menor = 0
for i in range(1,6):
    peso = float(input('Qual o peso da {}ª pessoa?'.format(i)))
    if i == 1:
        maior = i
        menor = i
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso que foi lido foi {}'.format(maior))
print('o menor peso que foi lido foi {}'.format(menor))


#57º exercício

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for i in range(1, 5):
    print('--- {}ª pessoa ---'.format(i))
    nome = str(input('NOME:'))
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO [M/F]:'))
    somaidade += idade
    if i == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O nome do homem mais velho é {} e se chama'.format(maioridadehomem, nomevelho))
print('são {} mulheres com mais de 20 anos'.format(totmulher20,))

#58º exercício

#59º exercício

#60º exercício

#61º exercício

#62º exercício

#63º exercício

#64º exercício

#65º exercício

#66º exercício

#67º exercício

#68º exercício

#69º exercício

#70º exercício

#71º exercício
