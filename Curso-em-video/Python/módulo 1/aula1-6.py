#1º exercício

print('Olá, mundo!')
print('Hello, world!')
print('-----------')
print('Olá! seja bem vindo!')
print('Hello! Welcome!')

#2º exercício

nome = input('Qual o seu nome?')
print('Prazer em te conhecer,', nome)

# or

print('Prazer em te conhecer, {}!'.format(nome))

print("------------------")

nome = input('Qual o seu nome?')
print('Prazer em te conhecer,', nome, ', eu mim chamo PY')
idade = input('Quantos anos você tem?')
print('Que legal!')
profissão = input('Com o que você trabalha atualmente?')
print('Que bacana, adorei isso!')

#3º exercício

num = int(input('Digite um número:'))
num2 = int(input('Digite outro:'))
s = num + num2
print('A soma de {} e {} é igual a {}'.format(num, num2, s))

print('----------------')

t1 = int(input('Digite qualquer número:'))
t2 = int(input('Digite outro:'))
T = t1 - t2
print('A diferença/subtração entre {} e {} é igual a {}'.format(t1, t2, T))

#4º exercício

num = (input('Digite algo:'))
print('O tipo primitivo dele é', type(num))
print('É um número?', num.isnumeric())
print('É um alfanumérico?', num.isalnum())
print('É alfabetico?', num.isalpha())
print('É um digito?', num.isdigit())
print('É um decimal?', num.isdecimal())
print('É minusculo?', num.islower())
print('É maiusculo?', num.isupper())
print('Só tem espaços?', num.isspace())
print('É capitalizado?', num.istitle())
print('', num.isidentifier())
print('', num.isprintable())

