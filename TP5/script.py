import ply.lex as lex

# Tokens
tokens = [
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'ID',
    'VALOR',
    'SAIR',
    'NUMERO'
]

t_LISTAR = r'LISTAR'
t_MOEDA = r'MOEDA'
t_SELECIONAR = r'SELECIONAR'
t_SAIR = r'SAIR'
t_ignore = ' \t,'

def t_VALOR(t):
    r'\d+e|\d+c'
    if 'e' in t.value:
        t.value = int(t.value.split('e')[0]) * 100
    else:
        t.value = int(t.value[:-1])
    return t

def t_ID(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

produtos = {1: {'nome': 'Água', 'preco': 50}, 2: {'nome': 'Bolo', 'preco': 60}}
saldo = 0

def adicionar_moeda(valor):
    global saldo
    saldo += valor
    print(f"< SALDO = {saldo//100}e{saldo%100}c")

def listar_produtos():
    for id, produto in produtos.items():
        print(f"< {id} {produto['nome']} {produto['preco']}c")

def selecionar_produto(id):
    global saldo
    if id in produtos and saldo >= produtos[id]["preco"]:
        saldo -= produtos[id]["preco"]
        print(f"< Compra realizada: {produtos[id]['nome']}. Saldo atual: {saldo//100}e{saldo%100}c")
    else:
        print("< Saldo insuficiente ou produto inexistente!")

def processar_entrada(entrada):
    lexer.input(entrada)
    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type == 'VALOR':
            adicionar_moeda(tok.value)
        elif tok.type == 'LISTAR':
            listar_produtos()
        elif tok.type == 'ID':
            selecionar_produto(tok.value)
        elif tok.type == 'SAIR':
            global saldo
            print(f"< Troco = {saldo//100}e{saldo%100}c")
            saldo = 0

while True:
    entrada = input('>> ')
    processar_entrada(entrada)
    if entrada == 'SAIR':
        break