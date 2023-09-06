Para importar una función de C a Python, puedes utilizar la biblioteca estándar de Python llamada ctypes. ctypes 
permite cargar bibliotecas dinámicas de C en Python y llamar a funciones definidas en esas bibliotecas.
Aquí hay un ejemplo simple de cómo hacerlo:import ctypes
# Carga la biblioteca compartidami_biblioteca = ctypes.CDLL('./mi_biblioteca.so')  
# # Reemplaza con la ruta de tu archivo# Llama a la función de C desde Pythonresultado = mi_biblioteca.mi_funcion()
# # Imprime el resultadoprint(resultado)Este es un ejemplo básico, y las configuraciones pueden variar según la plataforma y las opciones de 
# compilación utilizadas para crear la biblioteca compartida en C. También debes asegurarte de que la función C sea compatible con la forma en que se llaman las f
# unciones desde Python.

