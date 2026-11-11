#include <stdio.h>

voidft_ultimate_div_mod(int *a, int *b);

int	main(void)
{
	int valor_a;
	int valor_b;

	valor_a = 42;
	valor_b = 5;

	printf("Antes da funcao:\n");
	printf("a = %d, b = %d\n\n", valor_a, valor_b);

	ft_ultimate_div_mod(&valor_a, &valor_b);

	printf("Depois da funcao:\n");
	printf("a = %d, b = %d\n", valor_a, valor_b);

	return(0);
}
