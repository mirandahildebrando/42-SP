#include <stdio.h>

int ft_strlen(char *str);

int main(void)
{
	int tamanho;

	tamanho = ft_strlen("42SP");
	printf("Tamanho de '42SP': %d\n", tamanho);

	return(0);
}
