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
