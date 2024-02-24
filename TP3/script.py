import sys
import re

def main(inp):
    if len(inp) != 2:
        print("Usage: python3 script.py <sequence.txt>")
        return
    
    somador = 0
    somadorLista = []
    somadorON = False

    with open(inp[1], 'r') as f:
        for line in f:
            line = line.strip()
            palavras = line.split(' ')
            for palavra in palavras:
                if re.search(r'on', palavra, re.IGNORECASE):
                    somadorON = True
                elif re.search(r'off', palavra, re.IGNORECASE):
                    somadorON = False
                elif somadorON and re.match(r'^[-+]{0,1}\d+$', palavra):
                    somador += int(palavra)
                    if palavra[0] == '-':
                        palavra = '(' + palavra + ')'
                    somadorLista.append(palavra)
                elif palavra == '=':
                    if somadorLista != []:
                        print(' + '.join(somadorLista), '=', somador)
        
if __name__ == '__main__':
    main(sys.argv)