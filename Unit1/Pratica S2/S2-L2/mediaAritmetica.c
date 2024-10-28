#include <stdio.h>

int main() {
    int numeri[10];
    int count=0;
    int media=0;
    printf("Inserisci i numeri e calcola la media aritmentica!\nIMPORTANTE! NON PUOI INSERIRE PIU DI 10 NUMERI!\n");
    while (count!=10)
    {
        printf("Inserisci il numero 0 per interrompere l'inserimento e calcolare la media\n");
        printf("Inserisci il numero: ");
        scanf("%d", &numeri[count]);
        if(numeri[count]==0){
            break;
        }
        count++;
        printf("I numeri inseriti fino ad ora sono: ");
        for (int i = 0; i < count; i++)
        {
            printf("%d  ", numeri[i]);
        }
        printf("\n");
    }
    printf("La media aritmetica di: ");
    for (int i = 0; i < count; i++)
    {
        printf("%d ", numeri[i]);
        media+=numeri[i];
    }
    printf("e' uguale a: %d", media/count);
    return 0;
}