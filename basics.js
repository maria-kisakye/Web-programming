//- single line comment
/*
multi-line comment
*/

//variables
//var

var numberOne = 3;

//const

const numberTwo = 5;
const PI = 3.14;

//let
let numberThree = 9;

//console.log(PI);

function checkLet(){
    let numberFour = 10;
    console.log(numberFour);
}
//console.log(numberThree);
//checkLet()

//string dtypes
'',"",``
let firstName = 'Maria';
let lastName = "John";
let middleName = `Doe${lastName}`;
let welcomeStatement = 'Welcome back ${first'
//console.log(firstName,lastName,middleName);

console.log(middleName);

//boolean dtypes
let isStudent = true;
let hasgraduated = true;

console.log(isStudent || hasgraduated);//or logical operator
console.log(isStudent && hasgraduated);//and logical operator

//array dtpes
let numberListOne = [1,2,3,4,5]
let numberListTwo = [6,7,8]
//console.log(numberList[3]);
//console.log(numberListOne+numberListTwo);

let fruitList = ['apple','banana','orange'];
console.log(fruitList);

fruitList.push('grape');
console.log(fruitList);

fruitList.pop();
console.log(fruitList);


let personObject = {
    'name': 'John',
    'gender': 'male',
}
//console.log(personObject);

//arithmetic operators
console.log(numberOne+numberTwo);
console.log(numberOne-numberTwo);
console.log(numberOne*numberTwo);
console.log(numberOne/numberTwo);

//comparison operators
let numberSix = 1;
let numberFive = 1;

console.log(numberSix == numberFive);
console.log(numberSix === numberFive);