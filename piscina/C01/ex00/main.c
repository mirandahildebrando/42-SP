#include <stdio.h>

void ft_ft(int *nbr);

int main(void)
{

	int numero;
	numero = 0;

	printf("Antes da funcao: %d\n", numero);

	ft_ft(&numero);

	printf("Depois da funcao: %d\n", numero);

	return(0);
}
