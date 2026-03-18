/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_div_mod.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hvanique <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 18:00:42 by hvanique          #+#    #+#             */
/*   Updated: 2026/03/11 11:42:12 by hvanique         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_ultimate_div_mod(int *a, int *b);

void	ft_ultimate_div_mod(int *a, int *b)

{
	int	div;
	int	mod;

	div = *a / *b;
	mod = *a % *b;
	*a = div;
	*b = mod;
}
/*
int main(void)
{
	int a = 7;
	int b = 2;

	ft_ultimate_div_mod(&a, &b);


	if (a == 3 && b == 1)
	{
		write(1, "Y\n", 2);
	}
	else
	{
		write(1, "N\n", 2);
	}
	return (0);
} */