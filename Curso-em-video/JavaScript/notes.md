# Notas do curso JavaScript

[Clique aqui](https://developer.mozilla.org/pt-BR/docs/Learn/JavaScript) para ver o guia de Javascript


## EM ATUALIZAÇÃO👇

HTML --> conteúdo
CSS --> estilo
JavaScript --> interação

### variáveis e tipos primitivos

vaga a1 = carro 1 <-- "=" recebe
vaga a1 = carro 2
vaga a1 = null

n1 5 var n1 = 5
n2 8.5 var n2 = 8.5
n3 15 var n3 = 15 

var s1 = "javascript"     --> no js além de ultilizar VAR também podemos usar o LET
var s2 = 'curso em video'
var s3 = `guanabara`

s1 = javascript
s2 = curso em video
s3 = guanabara

### Identificadores

- Podemos começar com letra, $ ou _
- Não podemos começar com números
- É possível usar letras ou números
- É possível usar acentos e símbolos
- Não podem conter espaços
- Não podem ser palavras reservadas

## Dicas

- Maiusculos e minuscolos fazem a diferença
- Tente utilizar nomes coerentes para as variáveis
- Evite se tornar um "programador alfabeto/contador"

### Tipos primitivos

number --> 5; 18; 12; 0.5; -15.9; 8.0 
strings --> "google", 'javascript,`maria`
boolean --> True, False

date types:

number: infinity, NaN;
string;
boolean;
null;
undefined;
object: array;
function;

### Tratamento de dados

string --> number

number.parseInt(n)
number.parseFloat(n)
number(n)

número --> string

string(n)
n.ToString()

formatando strings:

var s = `javascript`    s.legth
'estou aprendendo s' // não faz interpolação
'estou aprendendo' + s // usa concatenação
'estou aprendendo ${s} // usa template string
s.ToUpperCase()
s.ToLowerCase()

Formatar números:

var n1 = 1543.5
n1
n1.ToFixed(2)
n1.ToLocalString('pt-br', {style:`currency`, currency: 'BRL'})

### Operadores 

**aritméticos**

5+2 -> 7
5-2 -> 3
5*2 -> 10
5/2 -> 2.5
5%2 -> 1
5**2 -> 25

ordem de precendência:

() 
**
* / %
+ -

**atibuição simples**

var a = 5+3 -> 8
var b = a%5 -> 3
var c = 5*b**2 -> 45
var d = 10-a//2 -> 6
var e = 6*2//d
var f = b%e+4//e

**auto-atribuições**

var n = 3    --> 3
n = n + 4    n += 4  --> 7
n = n - 5    n -= 5  --> 2
n = n * 4    n *= 4  --> 8
n = n /2     n /= 4  --> 4
n = n**2     n **=2  --> 16
n = n%5      n %=5   --> 1

**incremento**

var x = 5
x = x + 1    x ++   --> 6
x = x - 1    x --   -->

**relacionais**

5 > 2  -> true
  < 4  -> false
8>= 8  -> true
8<=7   -> false
5==5   -> true
!=4   -> false

**identidade**

5==5 -> true
5=='5' -> true
5==='5' -> false
5===5 -> true

**lógicos**

!  negação
&& conjunção
|| disjunção 

**precendência**

() ** /
> <> = 
!
&&
||

**ternário**

teste ? true : false

média >= 7.0 ? "aprovado" : "reprovado"

### Entendendo o DOM

dom --> document object model

**árvore dom**

**selecionando**

- por marca
- por id
- por nome
- por classe
- por seletor 

por marca -> getElementsByTagName()
por id -> getElementsById()
por nome -> getElementsByName()
por classe -> getElementsByClasseName()
por seletor -> querySelector()     querySelectorAll()

### Eventos Dom 

**<div>**
mouseenter        mousemove
mousedown         mouseup
click             mouseout

**funções**

```
function ação(paramêtro){

}
```

### Condições 

**Sequências**

° -> var n = 3 -> n += 2 -> window.alert(n) -> °

**condições simples**
```
if (condições){
    true
}
```

**condições compostas**

```
if(condição){
    true
} else{
    false
}
```

**condições aninhadas**

```
if (condição){
    bloco1
} else{
    if(condição2){
        bloco2
    } else{
        bloco3
    }
}
```

**condição multipla**

```
switch (expressão){
    case valor 1:
      bloco
    break
    case valor 2: 
      bloco 
    break
    case valor 3:
      bloco 
    break
    default:
      bloco
    breake
}
```

### repetições 

```
while (condição){
    bloco
}

do{
    bloco
} while(condição)
```

```
for(inicio; teste; incr){
    bloco
}
```

```
for(var c = 1; c<=10; c++){
    bloco
}
```

### variáveis 

**simples:** so consegue armazenar um valor por vez
**composta:** armazenar vários valores em uma mesma estrutura

vaga a = [ ,  , ]

let num = [5, 8, 4]

### funções

São ações executadas assim que são chamados ou em decorrencia de algum evento.
Pode receber paramêtros e retornar um resultado.