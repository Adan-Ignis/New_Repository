function agregarTarea() {
    let cajaTexto = document.getElementById("tarea");
    let texto = cajaTexto.value;
    if(texto == "") {
        return;
    }

    let li = document.createElement("li");

    let check = document.createElement("input");
    check.type = "checkbox";
    check.onclick = function() {
        cambiaCheck(this);
    }

    let span = document.createElement('span');
    span.innerHTML = texto;

    let boton = document.createElement("button");
    boton.innerHTML = "Eliminar";
    boton.onclick = function() {
        eliminarTarea(this);
    }

    li.appendChild(check);
    li.appendChild(span);
    li.appendChild(boton);

    let lista = document.getElementById("padre");
    lista.appendChild(li);
    cajaTexto.value = "";
}

function eliminarTarea(boton) {
    let li = boton.parentNode;
    li.parentNode.removeChild(li);
}

function cambiaCheck() {
    let a = 0;
    let li = check.parentNode;
    if (check.checked) {
        li.className = "tachado";
    } else {
        li.className = "";
    }
}