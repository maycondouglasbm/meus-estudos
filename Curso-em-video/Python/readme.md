# Módulo 1

### Documentação da linguagem

_Clique aqui_ ---> [PYTHON](https://docs.python.org/3/)

## Primeiros comandos

Primeiros comandos em **Python**:

```
- print('Olá mundo')

- A = int(input('Digite um número:))
- B = int(input('Digite outro:))
- S = A + B
- print('A soma de A e B é: {}', S)

 ```

## Tipos primitivos

- INT --> 7, -4, 0, 9875
- FLOAT --> 4.5, 0.076, -15.223, 7.0
- BOOL --> True, False
- STR --> 'Olá', '7.5', 'terra' 

## Operadores artméticos

- (+) adição
- (-) subtração
- (*) multiplicação
- (/) divisão 
- (**) potência
- (//) divisão inteira
- (%) resto da divisão
- (n**(1/2)) raiz quadrada ou pow(n, (1/2))

## Ordem de precendência

- 1ª) ()
- 2ª) **
- 3ª) *, /, //, %
- 4ª) +, -

   ## observação:

- \n --> quebra linha
- {:.2f} --> formatar
- != --> diferente

## Módulo

- import [módulo]
- from [módulo] import [objeto]


## _manipulando texto:_

frase = 'curso em video' 

```
c u r s o  e m  v i d e o
0 1 2 3 4 5 6 7 8 9 10 11 12 

```

## _Fatiamento:_

- frase[9] --> curso em 
- frase[9:13] --> vide  (para no 13 mas não lê a 13ª letra, o último valor não entra na contagem)

- frase[9:21:2] --> pula de 2 em 2 --> v d o  p t o
- frase[:5]  = frase[0:5]
- frase[9::3] --> pula de 3 em 3 


## _Análise:_

- len(frase) --> comprimento da frase
- frase.count('o') --> conta quantas vezes existe o 'o'
- frase.count('o', 0, 13) --> contagem já com fatiamento
- frase.find('deo') --> em que momento começou 'deo'
- frase.find('android') --> retorna o valor -1
- 'curso' in frase

## _Transformação:_


- frase.replace('python', 'android') --> troca 
- frase.upper() --> maiúsculo
- frase.lower() --> mantem o minúsculo e troca o maiúsculo por minúsculo
- frase.capitalize() --> todos os caracteres em minusculo e só 1 fica em maiúsculo (o da 1ª palavra da frase)
- frase.title() --> capitaliza todas as palavras da frase (deixa a primeira letra de todas as palavras em maiúsculo)
- frase.strip() --> remove os espaços no inicio e fim da frase
- frase.rstrip() --> lado direito removido (os últimos espaços)
- frase.lstrip() --> lado esquerdo removido (primeiros espaços)

## _Divisão:_

frase.split() --> feito nos espaços, divide uma string em uma lista

   * ex:

```
 c u r s o    e m    v i d e o 
|0 1 2 3 4|  |0 1|  |0 1 2 3 4|

```


## _Junção:_

'-'.join(frase) --> junta a frase com traços
  * ex:

```
frase = str(input('digite uma frase'))   ---> curso em video python
'-'.join(frase) ---> curso-em-video-python

print(''' texto ''')

```

## Condições

```
if carro.esquerda():
  bloco_a_
else:
  bloco_b_

````

  * ex:

```

tempo = int(input('Quantos anos tem seu carro?))
if tempo <= 3:
  print('carro novo')
else:
  print('carro velho')

```

## Cores no terminal
ANSI
escape sequence
\033[m

\003[style, text, back  m

* style
  * 0  none
  * 1  blod
  * 4  underline
  * 7  negative

* Text
  * 30 white
  * 31 red
  * 32 green
  * 33 yellow
  * 34 blue
  * 35 purple
  * 36 blue light
  * 37 NORMAL

* back 
  * 40
  * 41 
  * 42
  * 43
  * 44
  * 45
  * 46
  * 47

    * ex.:

```
print("\033[0;30;40mComputador bom\0333[m]])

```

# Módulo 2

## Dicas

- concentração;
- anote tudo;
- estude em grupo;
- ensine alguém;
- prátique muito;
- não pule exercícios;
- não copie as respostas;
- não desista.

## Condições aninhadas

```
if carro.esquerda():
elif carro.direita():
else:

```

Estrutura condicional **composta:**
```
if carro.esquerda():
   bloco 1 
elif carro.direita():
   bloco 2
elif carro.ré():
   bloco 3
else:
   bloco 4

```

```
if carro.esquerda():
   if  
   elif
   else:
elif 
else:

```

## Estrutura de repetição FOR

* Laços de repetição

```
for in ranger(1, 10):
   passo
pega

```

```
for c in ranger(0, 3):
  if x:
    pega
  passo
  pula
passo
pega

```

## Estrutura de repetição WHILE

```
while not y:
  if bloco:
    passo
  if buraco:
    pula
  if moeda:
    pega
  pega
```

## Interropendo repetições WHILE

```
while true:
   if bloco:
      passo
   if buraco:
      pula
   if moeda:
      pega
   if buraco:
      pula
      break
pega

```

**Módulo 3 em atualização...**


randint(a, b): Gera um número inteiro aleatório no intervalo [a, b], incluindo a e b.

uniform(a, b): Gera um número flutuante aleatório no intervalo [a, b], incluindo a e b.

random(): Gera um número flutuante aleatório no intervalo [0.0, 1.0].

randrange(start, stop, step): Gera um número inteiro aleatório no intervalo [start, stop), com passo step.

choice(seq): Seleciona um item aleatório de uma sequência, como uma lista ou string.

shuffle(seq): Embaralha os itens de uma sequência.

sample(population, k): Seleciona k elementos aleatórios de uma população sem repetição.