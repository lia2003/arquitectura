void funcion1(int *a, int *b, int *c, unsigned long long N)
{
    for (unsigned long long i = 0;i<N;i++)
    {
        c[i] = a[i] + b[i];
    }
}

void funcion2(int *a, int *b, int *c, unsigned long long N)
{
    for (unsigned long long i = 0;i<N;i+=4)
    {
        c[i] = a[i] + b[i];
        c[i+1] = a[i+1] + b[i+1];
        c[i+2] = a[i+2] + b[i+2];
        c[i+3] = a[i+3] + b[i+3];

    }
}