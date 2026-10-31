# ex05 — Can you create it?

**Lista:** [Shell 01](../README.md)  •  **Nível:** 2/3  •  **Arquivos:** `MaRViN`

**Funções permitidas:** nenhuma

---

## Objetivo

Criar um arquivo com conteúdo exato e nome difícil.

## Tarefa

O subject original pede um nome com `?`, `*`, `"` e `\`, que o NTFS do Windows não aceita. **Adaptação local:** crie um arquivo chamado `MaRViN` contendo exatamente os dois caracteres `42`, sem quebra de linha. Na piscina oficial, você fará o nome completo com quoting.

## Protótipo

```c
MaRViN (arquivo)
```

## Exemplo

```text
printf 42 > MaRViN
wc -c MaRViN
2 MaRViN
```

## Dica

`printf 42 > MaRViN` grava dois bytes. Confira com `xxd` ou `wc -c`.

## Erros comuns

- Usar `echo 42`, que acrescenta uma quebra de linha.
- Criar `marvin` minúsculo.
- Deixar um espaço ou newline no conteúdo.

## Checklist antes de testar

- [ ] O arquivo tem exatamente o nome pedido.
- [ ] O cabeçalho 42 está preenchido (rode `42header arquivo.c`).
- [ ] Compila com `gcc -Wall -Wextra -Werror`.
- [ ] `norminette` passa sem erros.
- [ ] Testei com `moulinette Shell01/ex05`.

---

*Treine sem copiar. Se travar por mais de 30 minutos, leia a dica, desenhe no papel e pergunte a um colega — na piscina, pedir ajuda faz parte do jogo.*
