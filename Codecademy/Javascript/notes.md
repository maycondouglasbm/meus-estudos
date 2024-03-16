## O que é JavaScript

JavaScript é uma linguagem de programação poderosa, flexível e rápida que agora está sendo usada para desenvolvimento web cada vez mais complexo e além!

Surgido em 4 de dezembro de 1995; 

Última versão ECMAScript 2022;

## Console

o console palavra-chave refere-se a um objeto, uma coleção de dados e ações, que podemos usar em nosso código. Palavras-chave são palavras que são construídas na linguagem JavaScript, de modo que o computador as reconhece e as trata especialmente.

Quando escrevemos `console.log()` o que colocamos dentro dos parênteses será impresso ou registrado no console.

## Comentários

Os comentários podem explicar o que o código está fazendo, deixar instruções para os desenvolvedores que usam o código ou adicionar outras anotações úteis.

Um comentário de linha única //.

Um comentário de várias linhas, será indicado por /*para iniciar o comentário e */para terminar o comentário.

## Tipos de dados

- Número : Qualquer número, incluindo números com decimais: 4, 8, 1516, 23.42.

- String : Qualquer agrupamento de caracteres em seu teclado (letras, números, espaços, símbolos, etc.) entre aspas simples: ' ... ' ou aspas duplas " ... ", embora prefiramos aspas simples. Algumas pessoas gostam de pensar em `string` como uma palavra chique para texto.

- Boolean : Este tipo de dados tem apenas dois valores possíveis - true ou false(sem aspas).

- Nulo : esse tipo de dado representa a ausência intencional de um valor e é representado pela palavra-chave `null`(sem aspas).

- Indefinido : Este tipo de dados é indicado pela palavra-chave `undefined` (sem aspas). Também representa a ausência de um valor, embora tenha um uso diferente de null. undefined significa que um determinado valor não existe.

- Símbolo : um recurso mais recente da linguagem, os símbolos são identificadores exclusivos, úteis em códigos mais complexos. Não precisa se preocupar com isso por enquanto.

- Objeto : Coleções de dados relacionados.

## Operadores aritméticos

Um operador é um personagem que executa uma tarefa em nosso código.

- Adicionar: +
- Subtrair: -
- Multiplicar: *
- Dividir: /
- Restante: %

```
console.log(3 + 4); // Prints 7
console.log(5 - 1); // Prints 4
console.log(4 * 2); // Prints 8
console.log(9 / 3); // Prints 3

```

## Concatenação de strings

processo de anexar uma string a outra.

```
console.log('hi' + 'ya'); // Prints 'hiya'
console.log('wo' + 'ah'); // Prints 'woah'
console.log('I love to ' + 'code.')// Prints 'I love to code.'
console.log('middle' + ' ' +'space'); // Prints 'middle space'

```

## Propriedades

```
console.log('Hello'.length); // Prints 5

```

O `.` é outro operador! Nós o chamamos de operador ponto .

o valor salvo na `length` propriedade é recuperado da instância da string, 'Hello'. O programa imprime 5 no console, pois Hello contém cinco caracteres.

## Métodos

Os tipos de dados têm acesso a métodos específicos que nos permitem manipular instâncias desse tipo de dados.

- um ponto (o operador ponto)
- o nome do método
- abrindo e fechando parênteses

Ex.: 'example string'.methodName()

```
console.log('hello'.toUpperCase()); // Prints 'HELLO'
console.log('Hey'.startsWith('H')); // Prints true

```

## Objetos embutidos

`Math` Por exemplo, se você deseja executar operações matemáticas mais complexas do que aritméticas, o JavaScript possui o objeto integrado.

```
console.log(Math.random()); // Prints a random number between 0 and 1

```

Este método retorna um número aleatório entre 0 (inclusivo) e 1 (exclusivo)

Para gerar um número aleatório entre 0 e 50, poderíamos multiplicar esse resultado por 50, assim:

```
Math.random() * 50;

```

`Math.floor()` pega um número decimal e arredonda para baixo para o número inteiro mais próximo.


# Variáveis

## Crie uma variável: var

```
var myName = 'Arya';
console.log(myName); // Output: Arya

```

var, abreviação de variável, é uma palavra-chave que cria ou declara uma nova variável.

myName é o nome da variável.

= é o operador de atribuição. Atribui o valor ( 'Arya') à variável ( myName).

'Arya'é o valor atribuído ( = ) à variável myName.

Depois que a variável é declarada, o valor da string 'Arya' é impresso no console fazendo referência ao nome da variável: `console.log(myName)`.

* regras gerais para nomear variáveis:

​- Não podem começar com números.

​- ​Diferenciam maiúsculas de minúsculas, portanto, myNamee mynameseriam variáveis ​​diferentes. É uma prática ruim criar duas variáveis ​​com o mesmo nome usando maiúsculas e minúsculas diferentes.

- Não podem ser iguais às palavras-chave.


## Crie uma Variável: let

let palavra-chave sinaliza que a variável **pode receber um valor diferente**. 

```

let meal = 'Enchiladas';
console.log(meal); // Output: Enchiladas

meal = 'Burrito';
console.log(meal); // Output: Burrito

```

podemos declarar uma variável **sem atribuir um valor à variável**.

```

let price;
console.log(price); // Output: undefined

price = 350;
console.log(price); // Output: 350

```

## Crie uma variável: const

abreviação da palavra constant. Você **pode armazenar qualquer valor** em uma `const` variável.

**não pode ser reatribuída** porque é constante. (Se você tentar reatribuir uma constvariável, obterá um arquivo TypeError)

Se você tentar declarar uma `const` variável sem um valor, obterá um SyntaxError. 

Se você está tentando decidir entre qual palavra-chave usar let ou const, pense se precisará reatribuir a variável mais tarde. `Se você precisar reatribuir a variável, use let, caso contrário, use const.`


## Operadores de atribuição matemática

```

let w = 4;
w = w + 1;
 
console.log(w); // Output: 5

```

```

let w = 4;
w += 1;
 
console.log(w); // Output: 5

```

```

let x = 20;
x -= 5; // Can be written as x = x - 5
console.log(x); // Output: 15
 
let y = 50;
y *= 2; // Can be written as y = y * 2
console.log(y); // Output: 100
 
let z = 8;
z /= 2; // Can be written as z = z / 2
console.log(z); // Output: 4

```

## O operador de incremento e decremento

```

let a = 10;
a++;
console.log(a); // Output: 11

```

```

let b = 20;
b--;
console.log(b); // Output: 19

```

## Concatenação de strings com variáveis

O + operador pode ser usado para combinar dois valores de string, mesmo que esses valores estejam sendo armazenados em variáveis:

```

let myPet = 'armadillo';
console.log('I own a pet ' + myPet + '.');  // Output: 'I own a pet armadillo.

```

## Interpolação de String

podemos inserir ou interpolar variáveis ​​em strings usando literais de modelo.


```

const myPet = 'armadillo';
console.log(`I own a pet ${myPet}.`);// Output: I own a pet armadillo.

```

um literal de modelo é envolvido por acentos graves `

Dentro do modelo literal, você verá um espaço reservado, ${myPet}. O valor de myPeté inserido no literal de modelo.

Quando interpolamos `I own a pet ${myPet}.`, a saída que imprimimos é a string:'I own a pet armadillo.'

Usando literais de modelo, você pode saber mais facilmente qual será a nova string.

## tipo de operadores

Se você precisar verificar o tipo de dados do valor de uma variável, poderá usar o `typeof` operador.

O `typeof` operador verifica o valor à sua direita e retorna , ou devolve, uma string do tipo de dados

```

const unknown1 = 'foo';
console.log(typeof unknown1); // Output: string
 
const unknown2 = 10;
console.log(typeof unknown2); // Output: number
 
const unknown3 = true; 
console.log(typeof unknown3); // Output: boolean

```

## O que são declarações condicionais?

Uma instrução condicional verifica uma(s) condição(ões) específica(s) e executa uma tarefa com base na(s) condição(ões).

if, else if else declarações

operadores de comparação

Operadores lógicos

valores verdadeiros vs falsos

operadores ternários

switch declaração

## if declaração

```

if (true) {
  console.log('This message will print!'); // Prints: This message will print!
}  

```

`if` declaração é composta por:

A `if` palavra-chave seguida por um conjunto de parênteses () que é seguido por um bloco de código ou instrução de bloco , indicado por um conjunto de chaves {}.

Dentro dos parênteses (), é fornecida uma condição avaliada como true ou false.

Se a condição for avaliada como true, o código dentro das chaves {} será executado ou será executado. Se a condição for avaliada como false, o bloco não será executado.

## Declarações If...Else

`else` instrução para executar um bloco de código quando a condição for avaliada como false

```

if (false) {
  console.log('The code in this block will not run.');
} else {
  console.log('But the code in this block will!'); // Prints: But the code in this block will!
}

```

else declaração:

Usa a `else` palavra-chave após o bloco de código de uma if instrução.

Tem um bloco de código que é envolvido por um conjunto de chaves {}.

O código dentro do `else` bloco de código da instrução será executado quando a `if` condição da instrução for avaliada como false.

if...else As declarações nos permitem automatizar soluções para questões de sim ou não, também conhecidas como decisões binárias .

## Operadores de Comparação

- Menor que: <

- Maior que: >

- Menos que ou igual a: <=

- Melhor que ou igual a: >=

- igual a: ===

- Não é igual a:!==

Os operadores de comparação comparam o valor à esquerda com o valor à direita. Por exemplo:

10 < 12 // Evaluates to true

Também podemos usar operadores de comparação em diferentes tipos de dados, como strings:

'apples' === 'oranges' // false

Todas as declarações de comparação são avaliadas como true ou falsee são compostas por:

- Dois valores que serão comparados.

- Um operador que separa os valores e os compara adequadamente ( >, <, <=, >=, ===, !==).

## Operadores lógicos

- o operador E --> && ( )
- o operador OU || ( )
- o operador not , também conhecido como operador bang (!)

**Quando usamos o `&&` operador**, estamos verificando se duas coisas são true:

```

if (stopLight === 'green' && pedestrians === 0) {
  console.log('Go!');
} else {
  console.log('Stop');
}

```

Ao usar o `&&` operador, ambas as condições devem ser avaliadas como true para que toda a condição seja avaliada true e executada. Caso contrário, se uma das condições for false, a `&&` condição será avaliada como false e o `else` bloco será executado.

Se nos importarmos apenas com o fato de qualquer condição ser true, podemos usar **o || operador:**

```
if (day === 'Saturday' || day === 'Sunday') {
  console.log('Enjoy the weekend!');
} else {
  console.log('Do some work.');
}
```

Ao usar o || operador, apenas uma das condições deve ser avaliada como true para que a instrução geral seja avaliada como true

**O ! operador** not inverte, ou nega , o valor de um booleano:

```

let excited = true;
console.log(!excited); // Prints false
 
let sleepy = false;
console.log(!sleepy); // Prints true

```

Essencialmente, o ! operador pegará um true valor e passará de volta false ou pegará um false valor e passará de volta true.

*Os operadores lógicos são frequentemente usados ​​em declarações condicionais para adicionar outra camada de lógica ao nosso código.*

## Truthy and Falsy

```

let myVariable = 'I Exist!';
 
if (myVariable) {
   console.log(myVariable)
} else {
   console.log('The variable does not exist.')
}

```

O bloco de código na if instrução será executado porque myVariablepossui um valor verdadeiro; mesmo que o valor de myVariable não seja explicitamente o valor true, quando usado em um contexto booleano ou condicional, ele é avaliado como true porque foi atribuído a ele um valor não falso.

**Então, quais valores são falsos - ou avaliados false quando verificados como uma condição?** A lista de valores falsos inclui:

- 0
- Strings vazias como ""ou''
- nullque representam quando não há valor algum
- undefinedque representam quando uma variável declarada não possui um valor
- NaN, ou não é um número

## Truthy and Falsy Assignment

Às vezes, o usuário não possui uma conta, tornando a username variável falsa. O código abaixo verifica se username está definido e atribui uma string padrão caso não esteja:

```

let username = '';
let defaultName;
 
if (username) {
  defaultName = username;
} else {
  defaultName = 'Stranger';
} 
console.log(defaultName); // Prints: Stranger

```

Em uma condição booleana, o JavaScript atribui o valor true a uma variável se você usar o || operador em sua atribuição:


```

let username = '';
let defaultName = username || 'Stranger';
 
console.log(defaultName); // Prints: Stranger

```

Como || as instruções ou verificam primeiro a condição do lado esquerdo, a variável defaultName receberá o valor real username se for verdadeira e receberá o valor 'Stranger'se username for falsa. Este conceito também é conhecido como avaliação de curto-circuito.


## Operador Ternário

```

let isNightTime = true;
 
if (isNightTime) {
  console.log('Turn on the lights!');
} else {
  console.log('Turn off the lights!');
}

```

Podemos usar um operador ternário para executar a mesma funcionalidade:


```

isNightTime ? console.log('Turn on the lights!') : console.log('Turn off the lights!');

```