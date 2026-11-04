#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_putnbr(int nb)
{
	long	numero_grande;

	numero_grande = nb;
	if (numero_grande < 0)
	{
		ft_putchar('-');
		numero_grande = -numero_grande;
	}
	if (numero_grande >= 10)
	{
		ft_putnbr(numero_grande / 10);
	}
	ft_putchar((numero_grande % 10) + '0');
}
