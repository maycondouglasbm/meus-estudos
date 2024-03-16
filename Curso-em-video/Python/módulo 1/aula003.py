#17º exercício

CO = float(input('O tamanho do cateto oposto:'))
CA = float(input('O tamanho do cateto adjacente:'))
hipotenusa = (CO ** 2 + CA ** 2) ** (1/2)
print('O comprimento da hipotenusa é o quadrado do primeiro que equivale a {} mais o quadrado do segundo que equivale a {}'
      '\nque é igual a hipotenusa que vale {:.2f}'.format(CO, CA, hipotenusa))

#18º exercício

import math
num = float(input('Digite um número para ver seu seno, cos e tangente:'))
seno = math.sin(math.radians(num))
print("O ângulo {} convertido para seno é {:.2f}".format(num, seno))
cos = math.cos(math.radians(num))
print("O ângulo {} convertido para cosseno é {:.2f}".format(num, cos))
tang = math.tan(math.radians(num))
print("O ângulo {} convertido para tangente é {:.2f}".format(num, tang))


print('---------------------------------------------------------------------')

from math import radians, sin, cos, tan
num = float(input('Digite um número para ver seu seno, cos e tangente:'))
seno = sin(radians(num))
print("O ângulo {} convertido para seno é {:.2f}".format(num, seno))
cos = cos(radians(num))
print("O ângulo {} convertido para cosseno é {:.2f}".format(num, cos))
tang = tan(radians(num))
print("O ângulo {} convertido para tangente é {:.2f}".format(num, tang))

#19º exercício

import random

n1 = str(input('Primeiro nome:'))
n2 = str(input('Segundo nome:'))
n3 = str(input('Terceiro nome:'))
n4 = str(input('Quarto nome:'))
Lista = [n1, n2, n3, n4]
escolhido = random.choice(Lista)
print('O escolhido foi: {}'.format(escolhido))

#20º exercício

import random
n1 = str(input('Primeiro nome:'))
n2 = str(input('Segundo nome:'))
n3 = str(input('Terceiro nome:'))
n4 = str(input('Quarto nome:'))
Lista = [n1, n2, n3, n4]
random.shuffle(Lista)
print('A ordem sorteada foi:')
print(Lista)

#21º exercício

#import pygame
#pygame.init()
#pygame.mixer.music.load('ex020.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()