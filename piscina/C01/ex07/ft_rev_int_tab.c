void ft_rev_int_tab(int *tab, int size)
{
	int inicio;
	int fim;
	int temp;

	inicio = 0;
	fim = size - 1;
	while (inicio < fim)
	{
		temp = tab[inicio];
		tab[inicio] = tab[fim];
		tab[fim] = temp;

		inicio++;
		fim--;
	}
}
