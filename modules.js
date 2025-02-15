// .fs

// const { error } = require('console');
// const {fs} = require('fs');

// fs.writeFile("code.txt", "Hello, World!", (error)=>{
//     if(error) throw error;
//     console.log('the file is created.')
// })

// fs.appendFile('code.txt', "\n this is line two", (error)=>{
//     if(error) throw error;
//     console.log('the text is added.')
// })
 
// fs.readFile("code.txt", "utf8", (err, data)=>{
//     if(err) throw err;
//     console.log(data);
// })

// //path
// const path = require('path');
// let fullPath = path.join(__dirname, "code.txt")
// console.log(fullPath);

// //os
// const os = require('os');
// console.log(`the free space i have is : ${os.freemem()}`);