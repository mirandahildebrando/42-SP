/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_alphabet.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hvanique <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/28 16:08:39 by hvanique          #+#    #+#             */
/*   Updated: 2026/03/07 11:25:35 by hvanique         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h> 

void	ft_print_alphabet(void);

void	ft_print_alphabet(void)
{
	char	letter;
	char	*ptr;

	letter = 'a';
	ptr = &letter;
	while (letter <= 'z')
	{
		write(1, ptr, 1);
		letter++;
	}
}
/*
int	main(void)
{
	ft_print_alphabet();
	return (0);
}*/
