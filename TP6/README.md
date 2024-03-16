# TPC6: GIC LL(1)

## 2024-03-16

## Autor

- A100705
- João Pedro Mota Baptista

## Resumo

Gramática Independente de Contexto LL(1) para:

- Prioridade dos operadores;
- Garantir que é LL(1);
- Calcular LA para todos os predicados.

EXEMPLO:

```bash
?a
b = a * 2/ (27-3)
!a+b
c = a*b / (a/b)
```

('?' = input e '!' = print)
