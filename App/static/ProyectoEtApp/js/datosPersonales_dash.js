var userLogiado = JSON.parse(localStorage.getItem("userLogiado"));

console.log(userLogiado.direc);

const nombre = document.getElementById("regNombre");
const apellido = document.getElementById("regApellido");
const rut = document.getElementById("regRut");
const telefono = document.getElementById("regFono");

const correo = document.getElementById("regCorreo");
const contra = document.getElementById("regPass");

//Ingresar datos personales
nombre.value = userLogiado.nombre;
apellido.value = userLogiado.apellido;
rut.value = userLogiado.rut;
telefono.value = userLogiado.telefono;

//Ingresar datos de cuenta
correo.value = userLogiado.correo;
contra.value = userLogiado.contraseña;

addEventListener("DOMContentLoaded", function () {
  if (!localStorage.getItem("showAlert")) {
    const Toast = Swal.mixin({
      toast: true,
      position: "top-end",
      showConfirmButton: false,
      timer: 3000,
      timerProgressBar: true,
    });

    Toast.fire({
      icon: "success",
      title: `Bienvenido ${userLogiado.nombre}`,
    });
    localStorage.setItem('showAlert', true);
  }

});
