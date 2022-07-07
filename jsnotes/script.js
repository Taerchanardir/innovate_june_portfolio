console.log("hello world");
// at first it objected to the double quotes, and then it didn't

// ';' are 'optional', which means they are ignored, same as in lua. Do they sometimes help with parsing whitespace between statements?

// declare a variable. 'var' is depreciated. 'let' is ancient
let myName = "Iain";
console.log(myName);

const fullName="Taerchanardir";
console.log(fullName);

myName="Fred";
console.log(myName);

// fullName="qwerty"; obviously not allowed

// if elseif endif syntax same as C/C++
if(myName==="Iain"){  // === means exactly equals, including data type
  console.log("Hello Iain");
} else if(myName==="Fred"){
  console.log("Hello Fred");
} else {
  console.log("Who??");
}

// define a function
function sayHello(){
  console.log("Hello!");
}

sayHello();