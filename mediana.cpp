#include <stdio.h>
#include <stdlib.h>

// Función de comparación para la función de ordenación qsort
int comparar_enteros(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    int numeros[] = {5, 1, 3, 2, 4}; // Definir un arreglo de números

    int cantidad = sizeof(numeros) / sizeof(numeros[0]); // Calcular la cantidad de números

    // Ordenar los números en orden ascendente
    qsort(numeros, cantidad, sizeof(int), comparar_enteros);

    // Calcular la mediana
    float mediana;
    if (cantidad % 2 == 0) {
        // Si la cantidad de elementos es par, la mediana es el promedio de los dos elementos del medio
        mediana = (numeros[cantidad / 2 - 1] + numeros[cantidad / 2]) / 2.0;
    } else {
        // Si la cantidad de elementos es impar, la mediana es el elemento del medio
        mediana = numeros[cantidad / 2];
    }

    // Imprimir la mediana
    printf("La mediana es: %.2f\n", mediana);

    return 0;
}
