// Acá establezco diferentes variables para luego usarlas en el HTML
var email = document.getElementById("email");
var jsonBtn = document.getElementById("jsonbtn");
var jsonText = document.getElementById("jsontext");
var linkDescarga = document.getElementById("descarga"); // Enlace de descarga

// EventListener al hacer click en jsonBtn, este crea el texto en formato JSON
jsonBtn.addEventListener("click", function () {
  var data = {
    email: email.value,
  };

  // Generar JSON y URL de descarga
  var jsonData = JSON.stringify(data);
  var descargaURL = URL.createObjectURL(
    new Blob([jsonData], { type: "application/json" })
  );

  // Asignar URL al enlace de descarga
  linkDescarga.href = descargaURL;

  // Quitar atributo style (hidden) de los botones
  linkDescarga.removeAttribute("style");

  // Mostrar JSON
  jsonText.innerHTML = jsonData;
});
