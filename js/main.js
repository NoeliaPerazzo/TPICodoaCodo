
document.getElementById("header").innerHTML= ` <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
<div class="container">
   
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <li class="nav-item"><a class="nav-link active" aria-current="page" href="index.html">Home</a></li>
            <li class="nav-item"><a class="nav-link" href="empleados.html">Empleados</a></li>
            <li class="nav-item"><a class="nav-link" href="login.html">Login</a></li>
            <li class="nav-item"><a class="nav-link" href="index.html" onclick = "cerrarSesion()">Cerrar sesión</a></li>
        </ul>
    </div>
</div>
</nav>
`


document.getElementById("footer").innerHTML= ` <footer class="py-5 bg-dark">
<div class="container"><p class="m-0 text-center text-white">Copyright &copy; VB Developers 2023</p></div>
</footer>
`

function login() {
    let user = document.getElementById("usuario").value;
    let pass = document.getElementById("password").value;
  
    if (user == "Noelia" && pass == "admin") {
      alert("Inicio de sesión exitoso");
      sessionStorage.setItem('usuarioAutenticado', true);
      
      console.log("Redirigiendo a empleados.html");
      window.location = "empleados.html";
      console.log("Después de la redirección");
      
    } else {
      console.error("Acceso denegado. Usuario o contraseña incorrectos.");
      alert("Acceso denegado");
    }
  }

  function cerrarSesion() {
    sessionStorage.setItem('usuarioAutenticado', false);
    alert("Sesión cerrada exitosamente");
    window.location = "index.html";  // Cambia "index.html" por la página a la que quieres redirigir al cerrar sesión
}
  
