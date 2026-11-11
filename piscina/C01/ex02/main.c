#include <stdio.h>

void ft_swap(int *a, int *b);

int main(void)
{
    int x;
    int y;

    x = 42;
    y = 21;

    printf("Antes da troca: x = %d, y = %d\n", x, y);

    ft_swap(&x, &y);


    printf("Depois da troca: x = %d, y = %d\n", x, y);

    return (0);
}
