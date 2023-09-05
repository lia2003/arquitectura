# Definir una lista de números
numeros = [1, 2, 3, 4, 5]

# Calcular la media geométrica
producto = 1.0  # Inicializamos el producto como un número en punto flotante

for numero in numeros:
    producto *= numero  # Multiplicamos cada número en la lista

media_geometrica = producto**(1/len(numeros))

# Imprimir la media geométrica
print("La media geométrica es:", media_geometrica)
