#include <stdio.h>

int main () {

int vector [10], i, j, k;
int swap_var;

printf ("Inserire 10 interi:\n");

for ( i = 0 ; i < sizeof(vector) ; i++)
	{
	int c= i+1;
	printf("[%d]:", c);
	scanf ("%d", &vector[i]);
	}

printf ("Il vettore inserito e':\n");
for ( i = 0 ; i < sizeof(vector) ; i++)
        {
        int t= i+1;
        printf("[%d]: %d", t, vector[i]);
	printf("\n");
	}

for (j = 0 ; j < sizeof(vector) - 1; j++)
	{
	for (k = 0 ; k < sizeof(vector) - j - 1; k++)
		{
			if (vector[k] > vector[k+1])
			{
			swap_var=vector[k];
			vector[k]=vector[k+1];
			vector[k+1]=swap_var;
			}
		}
	}
printf("Il vettore ordinato e':\n");
for (j = 0; j < sizeof(vector); j++)
	{
	int g = j+1;
	printf("[%d]:", g);
	printf("%d\n", vector[j]);
	}

return 0;

}