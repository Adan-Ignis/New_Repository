let numero = Math.floor(Math.random() * 11);
let nPropuesto
let intento = 10;

do {
    if (numero == nPropuesto) {
        window.print("Lo has adivinado");
    } else {
        intento--;
        windows.print("te quedan " + intento + "intentos");
    }
} while (numero != a || intento >= 0);

// Solucion del profesor
function adivinar(e) {
    e.preventDefaul();

    let numero = document.getElementById("numero");
    let quedan = document.getElementById("quedan");
    let resultado = document.getElementById("resultado");

    NUM = parseInt(numero.value);
    console.log(num);

    if(intentos < max_intentos) {
        if(num == objetivo) {
            resultado.innerHTML = "ENHORABUENA has aceptado";
        } else if (num < objetivo) {
            resultado.innerHTML = "El numero es menor que el objetivo";
        } else {
            resultado.innerHTML = "El numero es mayor que el objetivo";
            // Tambien se puede poner "El numero ${numero} es mayor que el objetivo" para poner valores de una variable sin tener que usar "+". Se conoce como interpolación.
        }
    }
}

function reiniciar() {}