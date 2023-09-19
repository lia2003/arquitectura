import numpy as np
import ctypes
import time
import matplotlib.pyplot as plt
import statistics
if __name__ == '__main__':
    
    lib = ctypes.CDLL('./lib_funciones.so')
    lib.funcion1.argtypes = [ np.ctypeslib.ndpointer(dtype=np.int32),np.ctypeslib.ndpointer(dtype=np.int32),np.ctypeslib.ndpointer(dtype=np.int32), ctypes.c_ulonglong]
    lib.funcion2.argtypes = [ np.ctypeslib.ndpointer(dtype=np.int32),np.ctypeslib.ndpointer(dtype=np.int32),np.ctypeslib.ndpointer(dtype=np.int32), ctypes.c_ulonglong]
    
    tic_total = time.perf_counter()

    N = [1024, 1024*2, 1024*4, 1024*8, 1024*16, 1024*32]
    lista_funcion1_N = []
    lista_funcion2_N = []
    for n in N:
        arreglo_a1 = np.random.randint(0,10,size = n,dtype=np.int32)
        arreglo_b1 = np.random.randint(0,10,size = n,dtype=np.int32)
        arreglo_c1 = np.random.randint(0,10,size = n,dtype=np.int32)

        arreglo_a2 = np.random.randint(0,10,size = n,dtype=np.int32)
        arreglo_b2 = np.random.randint(0,10,size = n,dtype=np.int32)
        arreglo_c2 = np.random.randint(0,10,size = n,dtype=np.int32)
        
        iteraciones = 150
        lista_func1 = []
        lista_func2 = []
        for _ in range(iteraciones):
            tic1 = time.perf_counter()
            lib.funcion1(arreglo_a1,arreglo_b1,arreglo_c1,n)
            tic2 = time.perf_counter()
            lib.funcion2(arreglo_a2,arreglo_b2,arreglo_c2,n)
            toc = time.perf_counter()
            lista_func1.append(tic2-tic1)
            lista_func2.append(toc-tic2)

        lista_funcion1_N.append(statistics.median(lista_func1))
        lista_funcion2_N.append(statistics.median(lista_func2))
    toc_total = time.perf_counter()
    print("Tiempo total", 1e3*(toc_total-tic_total)," ms")

    res = [i / j for i, j in zip(lista_funcion1_N, lista_funcion2_N)]
    
    plt.plot(res,'r')
    plt.ylabel("SpeedUP")
    plt.grid()
    plt.savefig('test_cache_N_SpeedUP.png',dpi = 400)
