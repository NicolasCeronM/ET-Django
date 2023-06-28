$(function () {
  
  $("#regRut").mask("99999999-9");
  $("#regFono").mask("(+56 9) 9999 9999");
});

var campos ={
  nombre: false,
  apellido: false,
  rut: false,
  fono: false,
  correo: false,
  pass1: false,
  pass2: false,
  comuna: false,
  region: false,
  numDirec: false,
  direc: false,
  numDirec: false
}

const nombre = document.getElementById("regNombre");
const apellido = document.getElementById("regApellido");
const rut = document.getElementById("regRut");
const fono = document.getElementById("regFono");
const correo = document.getElementById("regCorreo");
const pass1 = document.getElementById("regPass");
const pass2 = document.getElementById("regPassRep");
const comuna = document.getElementById("regComuna");
const region = document.getElementById("regRegion");
const nomDirec = document.getElementById("regDirecNom");
const direc = document.getElementById("regDirec");
const numDirec = document.getElementById("regNum");


const formulario = document.getElementById("form-registro");

const botonRegistrar = document.getElementById("regEnviar");



nombre.addEventListener('keyup',nombreVacio)
apellido.addEventListener('keyup',apellidoVacio)
rut.addEventListener('keyup',rutValidate)
fono.addEventListener('keyup',fonoValidate)
correo.addEventListener('keyup',validarCorreo)
pass1.addEventListener('keyup',validarPass)
pass2.addEventListener('keyup',validarPass2)
region.addEventListener('change',validarRegion)
comuna.addEventListener('change',validarComuna)
nomDirec.addEventListener('keyup',nomDirecVacio)
direc.addEventListener('keyup',DirecVacio)
numDirec.addEventListener('keyup',numDirecVacio)

botonRegistrar.addEventListener('click',Enviar);




function nombreVacio() {
  if (nombre.value.length > 3) {
    nombre.classList.remove("is-invalid");
    nombre.classList.add("is-valid");
    campos.nombre = true
  } else {
    nombre.classList.add("is-invalid");
    nombre.classList.remove("is-valid");
    campos.nombre = false
  }
}

function apellidoVacio() {
  if (apellido.value.length > 3) {
    apellido.classList.remove("is-invalid");
    apellido.classList.add("is-valid");
    campos.apellido = true
  } else {
    apellido.classList.add("is-invalid");
    apellido.classList.remove("is-valid");
    campos.apellido = false
  }
}

function rutValidate(){


  if (rut.value.length ===10) {
    rut.classList.remove("is-invalid");
    rut.classList.add("is-valid");
    campos.rut = true
  } else {
    rut.classList.add("is-invalid");
    rut.classList.remove("is-valid");
    campos.rut = false
  }

}

function fonoValidate(){

  if (fono.value.length ===17) {
    fono.classList.remove("is-invalid");
    fono.classList.add("is-valid");
    campos.fono = true
  } else {
    fono.classList.add("is-invalid");
    fono.classList.remove("is-valid");
    campos.fono = false
  }

}

function validarCorreo () {
  var expR =
    /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;

  if (!expR.test(correo.value)) {
    correo.classList.add("is-invalid");
    var error = document.getElementById("fbCorreo");
    error.innerHTML = "Ingrese correo valido (ejemplo@ejemplo.com)";
    campos.correo = false
  } else {
    correo.classList.remove("is-invalid");
    correo.classList.add("is-valid");
    campos.correo = true
  }
};

function validarPass  ()  {

  if (pass1.value.trim().length >= 5 && pass1.value.trim().length <= 12) {
    pass1.classList.remove("is-invalid");
    pass1.classList.add("is-valid");
    campos.pass1 = true
  } else {
    pass1.classList.add("is-invalid");
    campos.pass1 = false
  }
};

function validarPass2 ()  {

  if (pass1.value !== pass2.value) {
    pass2.classList.add("is-invalid");
    campos.pass2 = false
  } else {
    pass2.classList.remove("is-invalid");
    pass2.classList.add("is-valid");
    campos.pass2 = true
  }
};

//Validar terminos y condiciones
const ck = document.getElementById("chkTerminos");
const validarTerminos = () => {
  if (ck.checked) {
    ck.classList.add("is-valid");
    ck.classList.remove("is-invalid");
  } else {
    ck.classList.add("is-invalid");
  }
};

//Validar comuna
function validarComuna() {
  if (comuna.value.trim() == "") {
    comuna.classList.add("is-invalid");
    campos.comuna = false
  } else {
    comuna.classList.remove("is-invalid");
    comuna.classList.add("is-valid");
    campos.comuna = true
  }
}

//Vlidar region
function validarRegion() {
  if (region.value === "Seleccione...") {
    region.classList.add("is-invalid");
    campos.region = false
  } else {
    region.classList.remove("is-invalid");
    region.classList.add("is-valid");
    campos.region = true
  }
}

function nomDirecVacio() {
  if (nomDirec.value.length > 3) {
    nomDirec.classList.remove("is-invalid");
    nomDirec.classList.add("is-valid");
    campos.nomDirec = true
  } else {
    nomDirec.classList.add("is-invalid");
    nomDirec.classList.remove("is-valid");
    campos.nomDirec = false
  }
}

function numDirecVacio() {
  if (numDirec.value.length > 3) {
    numDirec.classList.remove("is-invalid");
    numDirec.classList.add("is-valid");
    campos.numDirec = true
  } else {
    numDirec.classList.add("is-invalid");
    numDirec.classList.remove("is-valid");
    campos.numDirec = false
  }
}

function DirecVacio() {
  if (direc.value.length > 3) {
    direc.classList.remove("is-invalid");
    direc.classList.add("is-valid");
    campos.direc = true
  } else {
    direc.classList.add("is-invalid");
    direc.classList.remove("is-valid");
    campos.direc = false
  }
}


function Enviar(evn){

  evn.preventDefault()

  //console.log(campos)

  if(campos.nombre,campos.apellido,campos.rut,campos.fono,campos.pass1,campos.pass2,campos.nomDirec, campos.direc, campos.numDirec, campos.region , campos.comuna){
    Swal.fire(
      'Good job!',
      'You clicked the button!',
      'success'
    )
    formulario.submit();

  }else{
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: 'Something went wrong!',
    })

  }
}


