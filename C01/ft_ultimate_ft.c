/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_ft.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hvanique <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/03 18:44:21 by hvanique          #+#    #+#             */
/*   Updated: 2026/03/11 11:32:24 by hvanique         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

void	ft_ultimate_ft(int *********nbr);

void	ft_ultimate_ft(int *********nbr)
{
	*********nbr = 42;
	printf("teste");
}
/*
	int main(void)
{
	int n = 0;
	int *p1 = &n;
	int **p2 = &p1;
	int ***p3 = &p2;
	int ****p4 = &p3;
	int *****p5 = &p4;
	int ******p6 = &p5;
	int *******p7 = &p6;
	int ********p8 = &p7;
	int *********p9 = &p8;
    printf("Antes: %d", n); // Vai imprimir 0 
    ft_ultimate_ft(p9);
    printf("Depois: %d", n); // Vai imprimir 42
    return 0;
} */
