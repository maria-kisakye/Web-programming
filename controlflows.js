/**if statements */

// if(condition){
//     logic
// }else if(condition){
//     logic
// }else{
//     logic
// }

// age, child, adult, invalid

//  let age = 2
// if(age<0){
//     console.log("invalid")
// }else if(age>=18){
//     console.log("child")
// }else{
//     console.log("child")
// }

/**switch statement */
//  switch (key) {
//     case value:
//         break;
    
//     case value:
//         break;

//     case value:
//         break;

//     default:
//         break;
// }

// let number =5;

// switch(number){
//     case 1:
//         console.log("This is Sunday");
//         break;
    
//     case 2:
//         console.log("This is Monday");
//         break;
    
//     case 3:
//         console.log("This is Tuesday");
//         break;
    
//     case 4:
//         console.log("This is Wednesday");
//         break;
    
//     case 5:
//         console.log("This is Thursday");
//         break;
    
//     case 6:
//         console.log("This is friday");
//         break;
    
//     case 7:
//         console.log("This is Saturday");
//         break;
//     default:
//         console.log("this day does not exist");
//         break;
// }


let password = '12345'
let confirmPassword = '123456'

if(password === confirmPassword){
    console.log("password is the same")
}
else{
    console.log("password is not the same\n try again")
}

/**for loop */
// for (initialization, condition, increment){
//     results
// }

// print the first 100 counting numbers

for (i=0; i<101; i+=1){
    console.log(i)
}

//while loop

//initialization

// while(condition){
//     results
//     increment
// }

let i=0
while(i<101){
    console.log(i)
    i+=1
}

//for in loop // arrays
let fruitList = ['apple','banana','orange'];
for (fruit in fruitList){
    console.log(fruitlist[fruit]);
}

//for of loop
for (fruit of fruitList){
    console.log(fruit);
}