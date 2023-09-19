void funcion_c1(double *arreglo1, double *arreglo2, unsigned long long N)
{
    for (unsigned long long i; i<N;i++)
    {
        arreglo1[i] *=3;
    }
    for (unsigned long long i; i<N;i++)
    {
        arreglo2[i] *=3;
    }
}

void funcion_c2(double *arreglo1, double *arreglo2, unsigned long long N)
{
    for (unsigned long long i; i<N;i++)
    {
        arreglo1[i] *=3;
        arreglo2[i] *=3;
    }
}