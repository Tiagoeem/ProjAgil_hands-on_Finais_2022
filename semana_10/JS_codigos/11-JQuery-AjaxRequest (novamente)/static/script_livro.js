$(document).ready(function () {

  $("#meu-form").submit(function (event) {
    
    event.preventDefault();

    var settings = {
      "url": "livro",
      "method": "GET",
      "timeout": 0
    };
    
    $.ajax(settings).done(function (response) {
      console.log(response);
      for (var i = 0; i < response.livros.length; ++i) {

        $("#ul-resp"+String(i)).remove()
        $("#div-respostas").append("<ul id=\"ul-resp"+i+"\">"+ "Livro " + String(i) +"</ul>")
        $("#ul-resp"+String(i)).append("<li>id:" + String(response.livros[i].id) + "</li>")
        $("#ul-resp"+String(i)).append("<li>nome:" + response.livros[i].nome + "</li>")
        $("#ul-resp"+String(i)).append("<li>isbn:" + response.livros[i].isbn + "</li>")
        $("#ul-resp"+String(i)).append("<li>isbn:" + JSON.stringify(response.livros[i].emprestimos) + "</li>")

      }


    });
  });
  
});