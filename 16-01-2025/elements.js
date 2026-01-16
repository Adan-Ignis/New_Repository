// Ejercicio 1
function ej1 () {
    let btn = document.getElementById("ej1");
    let colorActual = btn.style.backgroundColor;
    //console.log(colorActual);
    if (colorActual == color1) {
        btn.style.backgroundColor = color2;
    } else {
        btn.style.backgroundColor = color1;
    }
}

// function ej2 () {
//     let a = document.getElementById("ej2");
//     parrafo.style.backgroundColor="yellow";

//     //console.log("Pisando el p");
// }

// Ejercicio 2
function mostrarMensaje () {
    let parrafo = document.getElementById("ej2");
    if (parrafo.style.backgroundColor == "yellow") {
        parrafo.style.backgroundColor = "";
    } else {
        parrafo.style.backgroundColor = "yellow";
    }
}

// Ejercicio 3
function ej3 () {
    let a = document.getElementById("ej3");

    a.addEventListener("mouseover",ponerAmarillo);
    a.addEventListener("mouseleave", quitarAmarillo);
}

function ponerAmarillo () {
    a.style.backgroundColor = "yellow";
}

function quitarAmarillo () {
    a.style.backgroundColor = "";
}

// Ejercicio 4 | En realidad es el 3
let contador = 0;
let texto = document.getElementById("ej3");
let total = document.getElementById("total");

total.addEventListener("keyup", cuentaTeclas);

function ej4 () {
    let a = 0;

    let b = document.getElementById("ej4");
}

// Ejercicio 5
function ej5 () {
    let a = document.getElementById("ej5");
}

// Ejercicio 6
function ej6 () {
    let a = document.getElementById("ej6");
}

// Ejercicio 7
function ej7_1 () {
    let a = document.getElementById("ej7.1");

    a.addEventListener("mouseover",);
    a.addEventListener("mouseleave",);
}

function ej7_2 () {
    let a = document.getElementById("ej7.2");

    a.addEventListener("mouseover",);
    a.addEventListener("mouseleave",);
}

function ej7_3 () {
    let a = document.getElementById("ej7.3");

    a.addEventListener("mouseover",);
    a.addEventListener("mouseleave",);
}


function ej3 () {
    let a = document.getElementById("ej3");

    a.addEventListener("mouseover",ponerAmarillo);
    a.addEventListener("mouseleave", quitarAmarillo);
}

function ponerAmarillo () {
    a.style.backgroundColor = "yellow";
}

function quitarAmarillo () {
    a.style.backgroundColor = "";
}

// Ejercicio 8
function ej8 () {
    let a = document.getElementById("ej8");
}

// Ejercicio 9
function ej9 () {
    let a = document.getElementById("ej9");
}

function ponerBorder () {
    texto.style.border = "2px solid red";
}

function quitarBorder () {
    texto.style.border = "";
}