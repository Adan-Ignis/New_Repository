// while (true) {
//     for (let H = 0; H <= 24; H++) {
//         for (let M = 0; M <= 60; M++) {
//             for (let S = 0; S <= 60; S++) {
//                 console.log(H + ":" + M + ":" + S);
//             }
//         }
//     }
// }

// Repuesta del profesor
let manejador;

function mostrarFecha() {
    let fecha = new Date(); //Para obtener la fecha
    //Fecha
    let anio = fecha.getFullYear();
    let mes = fecha.getMonth() + 1;
    let dia = fecha.getDate();
    let hora = fecha.getHours();
    let minuto = fecha.getMinutes();
    let segundo = fecha.getSeconds();
    // Dia de la semana
    let diaSemana = fecha.getDay();

    //Día de la semana
    //let spanDiaSemana = document.getElementById("diaSemana");
    //Fecha
    let spanMes = document.getElementById("mes");
    let spanDia = document.getElementById("dia");
    let spanHora = document.getElementById("horas");
    let spanMinuto = document.getElementById("minutos");
    let spanSegundo = document.getElementById("segundos");

    //Día de la semana
    //spanDiaSemana.innerHTML ='';
    spanMes.innerHTML = mes.toString().padStart(2, "0");
    spanDia.innerHTML = dia.toString().padStart(2, "0");
    spanHora.innerHTML = hora.toString().padStart(2, "0");
    spanMinuto.innerHTML = minuto.toString().padStart(2, "0");
    spanSegundo.innerHTML = segundo.toString().padStart(2, "0");
    //Tambien puede utilizarse: String(segundo).padStart(2, "0");
}

function iniciar() {
    mostrarFecha();
    manejador = setInterval(mostrarFecha, 1000);
}

function parar() {
    clearInterval(manejador);
}

function diaSemana() {
    let semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"];
    return
}