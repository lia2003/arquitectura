import numpy as np
import ctypes
import time
import matplotlib.pyplot as plt
import statistics
if __name__ == '__main__':
    
    lib = ctypes.CDLL('./lib_funciones2.so')
    lib.funcion_c1.argtypes = [ np.ctypeslib.ndpointer(dtype=np.double),np.ctypeslib.ndpointer(dtype=np.double), ctypes.c_ulonglong]
    lib.funcion_c2.argtypes = [ np.ctypeslib.ndpointer(dtype=np.double),np.ctypeslib.ndpointer(dtype=np.double), ctypes.c_ulonglong]
    iteraciones = 500
    tic_total = time.perf_counter()
    N = [1024, 1024*2, 1024*4, 1024*8, 1024*16, 1024*32, 1024*64,1024*128]
    lista_f1_N = []
    lista_f2_N = []

    for n in N:
        lista_f1 = []
        lista_f2 = []
        arreglo1 = np.random.rand(1,n).astype(np.float64)
        arreglo2 = np.random.rand(1,n).astype(np.float64)
    
        arreglo3 = np.random.rand(1,n).astype(np.float64)
        arreglo4 = np.random.rand(1,n).astype(np.float64)
    

        for i in range(iteraciones):
            tic1 = time.perf_counter()
            lib.funcion_c1(arreglo1,arreglo2,n)
            tic2 = time.perf_counter()
            lib.funcion_c2(arreglo3,arreglo4,n)
            toc = time.perf_counter()

            lista_f1.append(tic2-tic1)
            lista_f2.append(toc-tic2)
        lista_f1_N.append(statistics.median(lista_f1))
        lista_f2_N.append(statistics.median(lista_f2))

    toc_total = time.perf_counter()

    print("El tiempo de ejecución es de", (toc_total-tic_total), " segundos")

    plt.plot(N,lista_f1_N,'r')
    plt.plot(N,lista_f2_N,'b')
    plt.grid()
    plt.savefig("Test_cache2_N_tiempo.png",dpi = 400)
    plt.close()

    res = [i / j for i, j in zip(lista_f1_N, lista_f2_N)]
    plt.plot(N,res,'b')
    plt.ylabel("SpeedUP")
    plt.grid()
    plt.savefig("Test_cache2_N_SpeedUP.png",dpi = 400)
