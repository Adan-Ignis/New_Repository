let tabs = document.querySelectorAll(".tab");
let contenidos = document.querySelectorAll(".tab-content");

window.addEventListener("scroll",function() {
    let scrolled = window.scrollY;
    console.log(scrolled);
    let altura = document.body.scrollHeight - window.innerHeight;
    document.getElementById("scrollbar").style.width = (scrolled/altura) * 100 + "%";
    document.getElementById("gris").style.width = scrolled? "100%" : "0"; // "scrolled?" cuando tiene de valor 0 se considera "false"

    //Mostrar flecha
    let flecha = document.querySelector(".flecha");
    if (porcentaje > 0.2) {
        flecha.style.display = "block";
    } else {
        flecha.style.display = "none";
    }
});

const boton = document.getElementById("btn_tema");
boton.addEventListener("click", function() {
    document.body.classList.toggle("oscuro");
    boton.textContent = document.body.classList.contains("oscuro") ? "Tema Claro" : "Tema Oscuro";
});

let cuadroTexto = document.getElementById("cuadro");
let cuentaTexto = document.getElementById("cuenta");
let historial = [];

cuadroTexto.addEventListener("input", function () {
    cuentaTexto.innerHTML = cuadroTexto.value.length;
    // Deshacer
    historial.push(cuadroTexto.value);
});

let btn_desh = document.getElementById("btnDeshacer");
btn_desh.addEventListener("click", function () {
    historial.pop();
    //cuadroTexto.value = historial[historial.lenght -1] || "";
    cuadroTexto.value = historial.slice(-1) || "";
    cuentaTexto.innerHTML = cuadroTexto.value.length;
});