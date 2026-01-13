function toString(lista){ //Devuelve una cadena con los elementos de la lista
    let salida = '';
    for(let i = 0; i < lista.length; i++) {
        salida += lista[i];
    }
    return salida;
}

// Curiosidades de los arrays
let uno = new Array(5); //Crear un array de 1 dimensión con 5 elementos

let dos = new Array(5,);

let tres = [,];

let cuatro = [,,];

let cinco = [undefined];