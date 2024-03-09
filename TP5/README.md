# TPC4: Máquina de Vending

## 2024-03-08

## Autor

- A100705
- João Pedro Mota Baptista

## Resumo

1. Carregar Lista de Produtos (Ficheiro ou Memória)

```bash
ID Nome Preco
01 Água 50c
02 Bolo 60c
(...)
```

```bash
>> LISTAR
< 01 Água 50c
< 02 Bolo 60c
.....
```

```bash
>> MOEDA 1e,10c,20c
< SALDO = 1e30c
>> SELECIONAR 2
< SALDO 70c
>> SAIR
< Troco valor
```
