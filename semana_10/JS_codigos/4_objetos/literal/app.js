var Tony = { 
    firstname: 'Tony', 
    lastname: 'Alicea',
    address: {
        street: '111 Main St.',
        city: 'New York',
        state: 'NY'
    },
    idade: function () {return 10;}
};

function greet(person) {
    console.log('Hi ' + person.firstname);
}


