#22º exercício
nome = str (input('Digite seu nome completo:'))
print('Analisando seu nome...')
print('Seu nome em letras maiusculas é: {}' .format(nome.upper()))
print('Seu nome em letras minusculas é: {}' .format(nome.lower()))
print("O seu nome completo possui o total de: {} letras" .format(len(nome) - nome.find(' ')))
print('O primeiro nome tem no total de letras de: {}'.format(nome.find(' ')))

#23º exercício

num = int(input('Digite um número com mais de 4 algarismos:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade desse número: {}'.format(u))
print('Dezena desse número: {}'.format(d))
print('Centena desse número: {}'.format(c))
print('Milhar desse número: {}'.format(m))

#24º exercício

city = str(input('Digite um nome de uma cidade:')).strip()
print(city[:6].upper() == 'SANTOS')

#25º exercício

nom = str(input('Digite seu nome completo:')).strip()
print('Seu nome tem silva? {}'.format('silva' in nom.lower()))

#26º exercício

frase = (input("digite uma frase:")).upper().strip()
print('A letra (a) aparece {} vezes nesta frase'.format(frase.count('A')))
print('A posição que aparece o (a) pela primeira vez é: {}'.format(frase.find('A')+1))
print('A posição que a letra (A) aparece pela ultima vez é: {}'.format(frase.rfind('A')+1))

