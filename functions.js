//two types

//-void functions
//-returning functions

//-returning functions
function addition(numberOne, numberTwo){
    return numberOne + numberTwo;
}

//-void functions
function sum(numberOne, numberTwo){
    let summation = numberOne + numberTwo;
    console.log(summation);
}

sum(6, 8)
console.log(addition(32, 67));

//arrow functions
// const subtraction = (numberOne, numberTwo) =>{
//     return numberOne - numberTwo;
// }

// const difference = (numberOne, numberTwo) =>{
//     console.log(`the difference is ${numberOne - numberTwo}`);
// }

// console.log(subtraction(67, 32));
// difference(99, 67)



// const welcome = (username) =>{
//     console.log(`welcome back ${username}`);
//     console.log(`Hi, ${username}`);
// }

// welcome("Maria");



let firstName = 'John'; //global variable

const welcome = () =>{
    let firstName = 'Jane'; //local variable
    console.log(`welcome back ${firstName}`);
    console.log(`Hi, ${firstName}`);
}

welcome();


