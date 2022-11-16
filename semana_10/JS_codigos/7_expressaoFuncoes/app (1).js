minhaFuncao();

function minhaFuncao() {
    console.log('Ola minha funcao');   
}

var funcaoAnonima = function() {
    console.log('Ola anonima');   
}

funcaoAnonima();

function log(a) {
   a();    
}

log(function() {
    console.log('hi');   
});


