/*let num = [5, 8, 2, 9, 3]
num [] = 
num.push()
num.length   <-- comprimento
console.log(`nosso vetor é ${num}`)
num.sort  <-- troca de elemeto para ordem crescente*/

let num = [5, 8, 2, 9, 3]
num.push(1)
num.sort()
console.log(num)
console.log(`nosso vetor tem ${num.length} posições`)
console.log(`o primeiro valor do vetor é ${num[0]}`)
let pos = num.indexOf(8)
console.log(`o valor 8 esta na posição ${pos}`)
if (pos == -1) {
    console.log('o valor não foi encontrado')
} else{
    console.log(`o valor esta na posição ${pos}`)
}