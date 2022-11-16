// function statement
function greet(name) {
    console.log('Hello 1 ' + name);   
}
greet('John');


// using a function expression
var greetFunc = function(name) {
    console.log('Hello 2 ' + name);
};
greetFunc('John');




// using an Immediately Invoked Function Expression (IIFE)
// usos: https://javascript.plainenglish.io/4-practical-use-cases-for-iifes-in-javascript-6481dcb0ba7d
var greeting = function(name) {
    
    return 'Hello 3 ' + name;
    
}('John');

console.log(greeting);


// IIFE
var firstname = 'John';

(function(name) {
    
    var greeting = 'Inside IIFE: Hello';
    console.log(greeting + ' ' + name);
    
}(firstname)); // IIFE






















