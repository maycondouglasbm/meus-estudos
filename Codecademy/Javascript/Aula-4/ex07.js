let isLocked = false;

//código refatorado
isLocked ? console.log('You will need a key to open the door.') : console.log('You will not need a key to open the door.')

//código inteiro
if (isLocked) {
  console.log('You will need a key to open the door.');
} else {
  console.log('You will not need a key to open the door.');
}

//
let isCorrect = true;
//código refatorado
isCorrect ? console.log('Correct!') : console.log('Incorrect!');

//código inteiro
if (isCorrect) {
  console.log('Correct!');
} else {
  console.log('Incorrect!');
}

//
let favoritePhrase = 'Love That!';

//
favoritePhrase === 'Love That!' ? console.log('I love that!') : console.log("I don't love that!");

//
if (favoritePhrase === 'Love That!') {
  console.log('I love that!');
} else {
  console.log("I don't love that!");
}