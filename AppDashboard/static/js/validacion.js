// const regionSelect = document.getElementById("regRegion");
// const comunaSelect = document.getElementById("regComuna");
const nombre = document.getElementById("nuevoNombre");
const direc = document.getElementById("nuevaDirec");
const numero = document.getElementById("nuevoNum");


nombre.addEventListener('DOMContentLoaded',validarVacio)

function validarVacio(){

    if (nombre.value.length =3) {
        nombre.classList.remove("is-invalid");
        nombre.classList.add("is-valid");
        
      } else {
        nombre.classList.add("is-invalid");
      
      }

}