// Solucion del profesor
function adivinar(e) {
    e.preventDefaul();

    let numero = document.getElementById("numero");
    let quedan = document.getElementById("quedan");
    let resultado = document.getElementById("resultado");

    NUM = parseInt(numero.value);
    console.log(num);
    quedan.innerHTML = max_intentos - intentos;
    intentos--

    if(intentos < max_intentos) {
        if(num == objetivo) {
            resultado.innerHTML = "ENHORABUENA has aceptado";
        } else if (num < objetivo) {
            resultado.innerHTML = "El numero es menor que el objetivo";
        } else {
            resultado.innerHTML = "El numero es mayor que el objetivo";
            // Tambien se puede poner "El numero ${numero} es mayor que el objetivo" para poner valores de una variable sin tener que usar "+". Se conoce como interpolación.
        }
    } else {
        resultado.innerHTML = "TERMINADO. el numero era $(objetivo)";
        btn_enviar.disable = true;
        numero.disabled = true;
    }

    numero.innerHTML = "";
    numero.focus();
}

function reiniciar() {
    window.location.reload();
}