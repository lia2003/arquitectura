
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int matriz_cua_1(int *arr, int N){
    int *elementos= (int *)calloc(N,sizeof(int));
    for(int i=1, i=<N, i++){
        elementos[i]= pow(arr[i],2);
    }
    return elementos;
}

int matriz_cua_2(int *arr, int N){
    int *elementos= (int *)calloc(N,sizeof(int));
    for(int i=1, i=<2, i++){
        for(int j=1, j=<N/2,j++){
            elementos[i,j]=pow(arr[j+i],2));
        }
    }
    return elementos;
}

int matriz_cua_3(int *arr, int N){
    int *elementos= (int *)calloc(N,sizeof(int));
    for(int i=a, i=<4, i++){
        for(int j=1, j=<N/4, j++){
            elementos[i,j]=pow(arr[j+i],2));
        }
    }
    return elementos;
}

int matriz_cua_4(int a, int b){
    int *elementos= (int *)calloc(N,sizeof(int));
    for(int i=1, i=<8, i++){
        for(int j=1, j=<N/8, j++){
            elementos[i,j]=pow(arr[j+i],2));
        }
    }
    return elementos;
}
