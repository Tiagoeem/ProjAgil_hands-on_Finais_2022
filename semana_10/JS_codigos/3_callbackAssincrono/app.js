function waitThreeSeconds() {
    var ms = 3000 + new Date().getTime();
    while (new Date() < ms){}
    console.log('Funcao de delay acabou');
}

function clickHandler() {
    console.log('Evento de click!');   
}

// Adiciona um listener para click
document.addEventListener('click', clickHandler);


waitThreeSeconds();
console.log('Fim de execução do escopo global');