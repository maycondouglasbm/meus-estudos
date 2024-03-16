# **Algoritmos e Lógica de programação :computer:** 

---

## **Algoritmo:**


Conjuntos de instruções sequenciais e precisas projetadas para resolver um problema ou realizar uma tarefa específica. Eles são uma parte fundamental da ciência da computação e da programação, pois permitem que os computadores executem ações de maneira eficiente e consistente.

## **Algoritmos computacionais:**

São passos a seres seguidos por um módulo processador e seus respectivos usuários que, quando executados na ordem correta, conseguem realizar determinada tarefa.

## **Comandos de saída:**

Escreva("qualquer coisa")

Escreval("qualquer coisa")


## **Variáveis:**

Na programação são nomes simbólicos usados para armazenar e representar dados em um programa de computador. Elas são essenciais para a manipulação e armazenamento de informações durante a execução de um programa. Cada variável possui um nome único que serve como uma referência para acessar seu conteúdo na memória do computador.

Var
indentificador: tipo

_identificadores:_
- Deve começar com uma letra
- os próximos podem ser numeros ou letras
- não se pode ultilizar nenhum simbolo, exceto _
- não podem conter espaços em branco
- não pode ter caracteres acentuados
- não pode ser uma palavra reservada


## **tipos primitivos**

- inteiro: 1, 3, -5, 198, 0  
- real: 0.5, 9.8, 3.1415
- caractere: "Olá mundo", "Maycon", "123" 
- logico: verdadeiro, falso


## **atribuições**

var
msg: caractere

msg <- "Olá, mundo!"


## **comandos de saída**

escreva("msg")

escreva(msg)

escreva("mensagem", msg)


## **Comando de Entrada e Operadores**

````
Algoritmo "MeuNome"
var
    nome: caractere
inicio 
    Escreva("Digite seu nome")
    Leia(nome)
    Escreva("Muito prazer ", nome)
Fimalgoritmo
````

## **Operadores aritmeticos**

\+ adição

\- subtração

/ divisão

\ divisão inteira

^ exponenciação

% módulo


## **Ordem de precedência**

()

^

\* /

\+ - 


## **Funções aritméticas**

Abs - valor absoluto

exp - exponenciação

Int - valor inteiro

RaizQ - Raiz quadrada

Pi - retorna o valor pi

Sen - Seno

Cos - Cosseno

Tan - tangente

GraupRad - Graus para rad



## **Operadores lógicos e relacionais**

_Relacionais_

\> maior que

< menor que

\>= maior ou igual a

<= menor ou igual a 

= igual a 

<> diferente de

_Lógicos_

p | q | p e q
:--: | --: | :---:
v | v  |  v 
v | f  |  f 
f | v  |  f 
f | f  |  f 

p | q | p ou q
:--: | --: | :---:
v | v |  v 
v | f |  v
f | v |  v 
f | f |  f 

p | NÃO p
:--: | :--:
v  | f 
f  |v 

````
Algoritmo "semnome"
Var
   A, B, C: Inteiro

Inicio
    A <- 2
    B <- 3
    C <- 5
    Escreva((A=B) ou (C>A))

Fimalgoritmo
````



## **Ordem de precedência geral**


1º Aritméticos

()

^

*/

2º Relacionais

todos

3º Lógicos

E

Ou 

Não

````
Algoritmo "semnome"
Var
   L1, L2, L3: Real
   EQ, ES: Logico

Inicio
    Escreva("Digite o primeiro lado: ")
    Leia(L1)
    Escreva("Digite o segundo lado: ")
    Leia(L2)
    Escreva("Digite o terceiro lado: ")
    Leia(L3)
    EQ <- (L1 = L2) e (L2 = L3)
    ES <- (L1 <> L2) e (L2 <> L3)
    Escreval("O triangulo é equilatero: ", EQ)
    Escreval("O triangulo é escaleno: ", ES)

Fimalgoritmo
````



````
Algoritmo "semnome"

Var
   L1, L2, L3: Real
   EQ, ES, TRI: Logico

Inicio
    Escreva("Digite o primeiro lado: ")
    Leia(L1)
    Escreva("Digite o segundo lado: ")
    Leia(L2)
    Escreva("Digite o terceiro lado: ")
    Leia(L3)
    TRI <- (L1 > L2 + L3) e (L2 > L1 + L3) e (L3 < L1 + L2)
    EQ <- (L1 = L2) e (L2 = L3)
    ES <- (L1 <> L2) e (L2 <> L3)
    Escreval("Pode formar um triangulo? ", TRI)
    Escreval("O triangulo é equilatero: ", EQ)
    Escreval("O triangulo é escaleno: ", ES)

Fimalgoritmo
````