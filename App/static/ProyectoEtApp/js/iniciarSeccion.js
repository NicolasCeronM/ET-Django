const mail = document.getElementById("login-correo");
const pass = document.getElementById("login-contra");
const bIniciar = document.getElementById("login-enviar");

let estaLogeado = false;
let usarioLogiado = "";

var Campos ={
  mail: false,
  pass:false
}

mail.addEventListener("keyup", ValidarCorreo);
pass.addEventListener("keyup", ValidarPass);
ver.addEventListener("click", Mostrar);
bIniciar.addEventListener("click", login);


var ver = document.getElementById("ver-contraseña");
var verIcon = document.getElementById("ver-icon");

function ValidarCorreo() {
  var expR =
    /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
  //CAMPO CORREO
  if (expR.test(mail.value)) {
    mail.classList.remove("is-invalid");
    mail.classList.add("is-valid");
    campos.mail = true;
  } else {
    mail.classList.add("is-invalid");
    campos.mail = false;
  }
}

function ValidarPass() {
  //CAMPO CONTRASEÑA
  if (pass.value.length <= 12 && pass.value.length >= 5) {
    pass.classList.remove("is-invalid");
    pass.classList.add("is-valid");
    campos.pass = true;
  } else {
    pass.classList.add("is-invalid");
    campos.pass = false;
  }
}

function Mostrar(e) {
  e.preventDefault();

  if (pass.type === "password") {
    pass.type = "text";
    verIcon.classList.remove("fa-regular", "fa-eye");
    verIcon.classList.add("fa-regular", "fa-eye-slash");
  } else {
    pass.type = "password";
    verIcon.classList.remove("fa-regular", "fa-eye-slash");
    verIcon.classList.add("fa-regular", "fa-eye");
  }
}

