# Gramática Independente de Contexto LL(1)

## Terminais

- **números**: `0 | 1 | 2 | ...`
- **variáveis**: `a | b | c | ...`
- **operadores aritméticos**: `+ | - | * | /`
- **parênteses**: `( | )`
- **igual**: `=`
- **símbolos de leitura e impressão**: `? | !`

## Não-Terminais

- **Programa**: `P`
- **Declaração**: `D`
- **Expressão**: `E`
- **Termo**: `T`
- **Fator**: `F`

## Produções

1. `P -> D P | ε`
2. `D -> ? var | var = E | ! E`
3. `E -> E + T | E - T | T`
4. `T -> T * F | T / F | F`
5. `F -> ( E ) | num | var`

## Lookahead Sets

- **LA(P → D P)**: `?`, `var`, `!`
- **LA(P → ε)**: `EOF` (fim do arquivo)
- **LA(D → ? var)**: `?`
- **LA(D → var = E)**: `var`
- **LA(D → ! E)**: `!`
- **LA(E → E + T)**: `+`, `-`, `(`, `num`, `var`
- **LA(E → E - T)**: `+`, `-`, `(`, `num`, `var`
- **LA(E → T)**: `(`, `num`, `var`
- **LA(T → T * F)**: `*`, `/`, `(`, `num`, `var`
- **LA(T → T / F)**: `*`, `/`, `(`, `num`, `var`
- **LA(T → F)**: `(`, `num`, `var`
- **LA(F → ( E ))**: `(`
- **LA(F → num)**: `num`
- **LA(F → var)**: `var`

Esta gramática respeita a prioridade dos operadores (multiplicação e divisão têm prioridade sobre adição e subtração) e garante que é LL(1), pois para qualquer símbolo de entrada, sempre há uma única produção aplicável, com base no conjunto lookahead.
