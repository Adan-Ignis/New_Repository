// Sobresaliente 9-10
// Notable 7-8
// Bien 6
// Suficiente 5
// Suspenso 1-4

var nota

switch (nota) {
    case 1:
    case 2:
    case 3:
    case 4:
        console.log("Suspenso")
    break;

    case 5:
        console.log("Suficiente")
    break;

    case 6:
        console.log("Bien")
    break;

    case 7:
    case 8:
        console.log("Notable")
    break;

    case 9:
    case 10:
        console.log("Sobresaliente")
    break;

    default:
        console.log("Dato de entrada no valido")
    break;
}

if (nota < 5) {
    console.log("Suspenso");
} else if (nota < 6) {
    console.log("Suficiente");
} else if (nota < 7) {
    console.log("Bien");
} else if (nota < 9) {
    console.log("Notable");
} else if (nota <= 10) {
    console.log("Sobresaliente");
} else {
    console.log("Dato de entrada no valido")
}