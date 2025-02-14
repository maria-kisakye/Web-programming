// // synchronous
// //step one
// console.log('1.boiling water')

// //step 2
// console.log('2.water is ready')

// //step 3
// console.log('3.other tasks ie bring cups')



//asynchronous
console.log("1.boiling the water");
setTimeout(() => {
    console.log("2.water is ready");
}, 2000);
console.log("3.other tasks")   