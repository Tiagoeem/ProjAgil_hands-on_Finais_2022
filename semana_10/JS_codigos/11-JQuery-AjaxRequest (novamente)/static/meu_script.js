$(document).ready(function () {

  $("#meu-form").submit(function (event) {
    
    event.preventDefault();

    var id_livro = $("#id-livro").val()

    var settings = {
      "url": "livro/"+ id_livro.toString(),
      "method": "POST",
      "timeout": 0,
      "headers": {
        "Content-Type": "application/json"
      },
      "data": JSON.stringify({
        "nome": $("#nome").val(),
        "isbn": $("#isbn").val()
      }),
    };
    
    $.ajax(settings).done(function (response) {
      console.log(response);

      $("#ul-resp").append("<li>id:" + String(response.id) + "</li>")
      $("#ul-resp").append("<li>nome:" + response.nome + "</li>")
      $("#ul-resp").append("<li>isbn:" + response.isbn + "</li>")

    });
  });
});