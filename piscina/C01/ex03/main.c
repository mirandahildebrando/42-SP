#include <stdio.h>

void	ft_div_mod(int a, int b, int *div, int *mod);

int main(void)
{
	int x = 42;
	int y = 5;
	int resultado_divisao;
	int resultado_resto;

	ft_div_mod(x, y, &resultado_divisao, &resultado_resto);

	printf("%d / %d -> div = %d, mod = %d\n", x, y, resultado_divisao, resultado_resto);

	return (0);
}
