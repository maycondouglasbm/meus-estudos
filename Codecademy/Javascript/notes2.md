## Instruções Else If

permite mais de dois resultados possíveis. Você pode adicionar quantas else ifdeclarações quiser, para fazer condicionais mais complexos!

sempre vem depois da `if` declaração e antes da `else` declaração. A else if instrução também requer uma condição.

```

let stopLight = 'amarelo'; 
 
if (stopLight ===  'vermelho') {
    console.log('Parem!' ); 

} else if (stopLight ===  'amarelo') {
    console.log('Desacelere'. ); 

} else if (stopLight ===  'verde') {
    console.log('Vai!' ); 
} else {
    console.log('Cuidado, desconhecido!' );
}

```

permitem que você tenha vários resultados possíveis.


##  A palavra-chave switch

Um switch declaração fornece uma sintaxe alternativa que é mais fácil de ler e gravar.

```
let groceryItem = 'papaya';
 
switch (groceryItem) {
  case 'tomato':
    console.log('Tomatoes are $0.49');
    break;
  case 'lime':
    console.log('Limes are $1.49');
    break;
  case 'papaya':
    console.log('Papayas are $1.29');
    break;
  default:
    console.log('Invalid item');
    break;
}
 
// Prints 'Papayas are $1.29'

```

- A palavra-chave inicia a instrução e é seguida porque contém o valor que cada uma irá comparar. No exemplo, o valor ou expressão da instrução é: switch( ... ) case switch groceryItem

- Dentro do bloco, há vários s. A palavra-chave verifica se a expressão corresponde ao valor especificado que vem depois dela. O valor seguinte ao primeiro é. Se o valor de igualado , que iria correr. { ... } case case case 'tomato 'groceryItem' tomato' case console.log()

- O valor de é , portanto, a terceira execução — é registrada no console.groceryItem 'papaya' case Papayas are $1.29

- A palavra-chave diz ao computador para sair do bloco e não executar mais nenhum código ou verificar quaisquer outros casos dentro do bloco de código. Nota: Sem palavras-chave, o primeiro caso correspondente será executado, mas todos os casos subsequentes também, independentemente de corresponderem ou não, incluindo o padrão. Esse comportamento é diferente de / instruções condicionais que executam apenas um bloco de código. break break if else

- Ao final de cada depoimento, há uma declaração. Se nenhum dos s for verdadeiro, o código na instrução será executado. switch default case default