//KISAKYE MARIA SENGENDO    B30260   S24B38/033  
//ASSIGNMENT 1

const fs = require("fs");
const readline = require("readline");
const bcrypt = require("bcrypt");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const USERS_FILE = "users.json";

// Load users from the JSON file
function loadUsers() {
  if (!fs.existsSync(USERS_FILE)) {
    return [];
  }
  const data = fs.readFileSync(USERS_FILE, "utf8");
  return JSON.parse(data);
}

// Save users to the JSON file
function saveUsers(users) {
  fs.writeFileSync(USERS_FILE, JSON.stringify(users, null, 2));
}

// Register a new user
function register() {
  rl.question("Enter your name: ", (name) => {
    rl.question("Enter your email: ", (email) => {
      rl.question("Enter your password: ", async (password) => {
        const users = loadUsers();
        const userExists = users.some((user) => user.email === email);
        if (userExists) {
          console.log("User already exists!");
          mainMenu();
        } else {
          const hashedPassword = await bcrypt.hash(password, 10);
          users.push({ name, email, password: hashedPassword });
          saveUsers(users);
          console.log("Registration successful!");
          mainMenu();
        }
      });
    });
  });
}

// Login an already registered user
function login() {
  rl.question("Enter your email: ", (email) => {
    rl.question("Enter your password: ", async (password) => {
      const users = loadUsers();
      const user = users.find((user) => user.email === email);
      if (user && (await bcrypt.compare(password, user.password))) {
        console.log("Login successful!");
        userMenu(user);
      } else {
        console.log("Invalid email or password!");
        mainMenu();
      }
    });
  });
}

// Display user menu after login
function userMenu(user) {
  console.log(`\nWelcome, ${user.name}!`);
  console.log("1. View Profile");
  console.log("2. Logout");
  console.log("3. Exit");
  rl.question("Choose an option: ", (choice) => {
    switch (choice) {
      case "1":
        console.log(`\nName: ${user.name}`);
        console.log(`Email: ${user.email}`);
        userMenu(user);
        break;
      case "2":
        console.log("Logging out...");
        mainMenu();
        break;
      case "3":
        console.log("Exiting...");
        rl.close();
        break;
      default:
        console.log("Invalid choice!");
        userMenu(user);
    }
  });
}

// Main menu
function mainMenu() {
  console.log("\n1. Register");
  console.log("2. Login");
  console.log("3. Exit");
  rl.question("Choose an option: ", (choice) => {
    switch (choice) {
      case "1":
        register();
        break;
      case "2":
        login();
        break;
      case "3":
        console.log("Exiting...");
        rl.close();
        break;
      default:
        console.log("Invalid choice!");
        mainMenu();
    }
  });
}

// Start the application
mainMenu();

