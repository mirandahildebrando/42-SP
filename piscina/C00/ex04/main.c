#include <unistd.h>

// Protótipo da sua função para que a main saiba que ela existe
void	ft_is_negative(int n);

int	main(void)
{
	// Teste com número negativo (deve mostrar N)
	ft_is_negative(-42);
	write(1, "\n", 1);

	// Teste com zero (deve mostrar P)
	ft_is_negative(0);
	write(1, "\n", 1);

	// Teste com número positivo (deve mostrar P)
	ft_is_negative(42);
	write(1, "\n", 1);

	return (0);
}
