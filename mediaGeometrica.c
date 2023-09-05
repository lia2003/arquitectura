#include <stdio.h>
#include <math.h>

int main() {
    // Definir un arreglo de números
    double numeros[] = {1.0, 2.0, 3.0, 4.0, 5.0};

    // Calcular la cantidad de números en el arreglo
    int cantidad = sizeof(numeros) / sizeof(numeros[0]);

    // Inicializar una variable para el producto
    double producto = 1.0;

    // Calcular el producto de los números elevados a la 1/n
    for (int i = 0; i < cantidad; i++) {
        producto *= pow(numeros[i], 1.0 / cantidad);
    }

    // El resultado es la media geométrica
    double media_geometrica = producto;

    // Imprimir la media geométrica
    printf("La media geométrica es: %.2f\n", media_geometrica);

    return 0;
}