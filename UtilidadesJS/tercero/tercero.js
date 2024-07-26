function compararNumeros() {
    // Obtener los valores de los inputs
    let numero1 = parseFloat(document.getElementById("numero1").value);
    let numero2 = parseFloat(document.getElementById("numero2").value);

    // Comparar y ordenar
    let mayor, menor;
    if (numero1 > numero2) {
        mayor = numero1;
        menor = numero2;
    } else {
        mayor = numero2;
        menor = numero1;
    }

    // Mostrar el resultado
    document.getElementById("resultado").textContent = "Números ordenados de mayor a menor: " + mayor + ", " + menor;
}
