//OGENRWOT FRANCIS

//Explanation of async and await Keywords in JavaScript

//What is async?
/*The async keyword is used to declare a function as asynchronous.
 An asynchronous function automatically returns a Promise. This means the function doesn't block the execution
of the program and returns a promise that will eventually resolve with a value or reject with an error.*/

//Syntax
async function fetchData() {
    // asynchronous code here
  }

//What is await?
/*The await keyword is used inside an async function to pause its execution until a Promise is resolved or rejected.
It allows you to write asynchronous code in a more synchronous-like manner, making it more readable and maintainable.*/

//Syntax
async function fetchData() {
    let result = await someAsyncFunction(); // Waits for promise to resolve
    console.log(result);
  }
/*Key Points:

-await can only be used inside an async function.
-await waits for a Promise to resolve before continuing with the next line of code.
-If the Promise rejects, an error is thrown, and we can handle it using try/catch blocks.*/

/*How They Simplify Asynchronous Code:
Before async/await, asynchronous operations were handled using callbacks or .then() methods on Promises.
 However, this often led to "callback hell" or complicated chaining of .then() calls. Here's a comparison:*/

//Using Callbacks:
function fetchData(callback) {
  setTimeout(() => {
    callback('Data fetched');
  }, 1000);
}
fetchData(function(result) {
  console.log(result);
});

//Using Promises (Chaining):
function fetchData() {
    return new Promise(resolve => {
      setTimeout(() => {
        resolve('Data fetched');
      }, 1000);
    });
  }
  
fetchData().then(result => {
    console.log(result);
  });

//Using async/await:
async function fetchData() {
    return new Promise(resolve => {
      setTimeout(() => {
        resolve('Data fetched');
      }, 1000);
    });
  }
  async function run() {
    const result = await fetchData();
    console.log(result);
  }
  
  run();
  //As you can see, using async/await results in more readable and synchronous-looking code, making it much easier to handle asynchronous operations.

 //Real-World Use Cases:
/*1.Fetching Data from APIs: One of the most common use cases for async/await is fetching data from APIs. 
For example, when you need to fetch user information from a server, you can use async/await to simplify the process.*/

//Example: Fetching user details from an API:
async function getUserData(userId) {
    try {
      const response = await fetch(`https://api.example.com/users/${userId}`);
      const user = await response.json();
      console.log(user);
    } catch (error) {
      console.error('Error fetching user data:', error);
    }
  }
  
  getUserData(1);
  //2.Handling Timeouts: In scenarios like setting a timeout, async/await can simplify waiting for a certain condition or time period before proceeding.

//Example: Delaying code execution using setTimeout: 
  function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
  async function fetchDataWithDelay() {
    console.log('Fetching data...');
    await delay(2000);  // Wait for 2 seconds
    console.log('Data fetched after delay');
  }
  
  fetchDataWithDelay();
   
  

