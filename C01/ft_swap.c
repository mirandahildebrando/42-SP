/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hvanique <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/04 16:37:14 by hvanique          #+#    #+#             */
/*   Updated: 2026/03/04 17:21:57 by hvanique         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

void	ft_swap(int *a, int *b);

void	ft_swap(int *a, int *b)
{
	int	temp;

	temp = *a;
	*a = *b;
	*b = temp;
}

/* int main()
{
	int x = 10;
	int y = 20;

	printf("Antes: x%d y=%d\n", x, y);

	ft_swap(&x, &y);

	printf("Depois: x=%d y=%d\n", x, y);

	return 0;
} */
