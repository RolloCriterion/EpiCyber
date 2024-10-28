int main(int argc, char const *argv[])
{
    int num1;
    int num2;
    printf("Inserisci il primo numero della moltiplicazione che vuoi effettuare: ");
    scanf("%d", &num1);
    printf("Inserisci il secondo numero: ");
    scanf("%d", &num2);
    int risMolt = num1*num2;
    printf("Il risultato della moltiplicazione e':\n%d x %d = %d", num1, num2, risMolt);
    return 0;
}
