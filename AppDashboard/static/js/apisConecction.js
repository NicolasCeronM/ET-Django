//DECLARACION DE VARIABLES API DE COMUNAS Y REGIONES

const url =
  "https://gist.githubusercontent.com/juanbrujo/0fd2f4d126b3ce5a95a7dd1f28b3d8dd/raw/b8575eb82dce974fd2647f46819a7568278396bd/comunas-regiones.json";
const regionSelect = document.getElementById("regRegion");
const comunaSelect = document.getElementById("regComuna");

function obtener_comunas_regiones() {
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      // Obtener lista de regiones
      const regiones = data.regiones;
      //console.log(data.regiones)

      // Agregar opciones al select de regiones
      regiones.forEach((region) => {
        const option = document.createElement("option");
        option.value = region.region;
        //console.log(option.value)
        option.text = region.region;
        regionSelect.appendChild(option);
        //console.log(option)
      });

      // Función que actualiza las comunas disponibles según la región seleccionada
      function actualizarComunas() {
        const regionSeleccionada = regionSelect.value;
        const comunas = data.regiones.find(
          (region) => region.region === regionSeleccionada
        ).comunas;

        // Limpiar opciones anteriores del select de comunas

        comunaSelect.innerHTML =
          '<option value="">Seleccione una comuna</option>';
        comunaSelect.disabled = false;

        // Agregar opciones al select de comunas
        comunas.forEach((comuna) => {
          const option = document.createElement("option");
          option.value = comuna;
          option.text = comuna;
          comunaSelect.appendChild(option);
        });
      }

      // Actualizar comunas al cambiar la región seleccionada
      regionSelect.addEventListener("change", actualizarComunas);
    })
    .catch((error) => console.error(error));
}


addEventListener('DOMContentLoaded',obtener_comunas_regiones);