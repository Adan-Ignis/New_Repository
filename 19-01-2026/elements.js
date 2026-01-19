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
function mostrarFecha () {
    let fecha = new Date(); //Para obtener la fecha
    let hora = fecha.getHours();
    let minuto = fecha.getMinutes();
    let segundo = fecha.getSeconds();

    let spanHora = document.getElementById("horas");
    let spanMinuto = document.getElementById("minutos");
    let spanSegundo = document.getElementById("segundos");

    spanHora.innerHtml = hora;
    spanMinuto.innerHtml = minuto;
    spanSegundo.innerHTML = segundo;
}