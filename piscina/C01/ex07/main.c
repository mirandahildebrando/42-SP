#include <stdio.h>

void	ft_rev_int_tab(int *tab, int size);

void	imprimir_array(int *tab, int size)
{
	int i;

	i = 0;
	while (i < size)
	{
		printf("%d", tab[i]);
		if (i < size - 1)
			printf(", ");
		i++;
	}
}

int	main(void)
{
	int array_par[] = {1, 2, 3, 4};
	int tamanho_par = 4;

	int array_impar[] = {10, 20, 30, 40, 50};
	int tamanho_impar = 5;

	printf("--- Teste 1: Array Par ---\n");
	printf("Antes:  ");
	imprimir_array(array_par, tamanho_par);

	ft_rev_int_tab(array_par, tamanho_par);

	printf("Depois: ");
	imprimir_array(array_par, tamanho_par);
	printf("\n");

	printf("--- Teste 2: Array Impar ---\n");
	printf("Antes:  ");
	imprimir_array(array_impar, tamanho_impar);

	ft_rev_int_tab(array_impar, tamanho_impar);

	printf("Depois: ");
	imprimir_array(array_impar, tamanho_impar);

	return (0);
}
