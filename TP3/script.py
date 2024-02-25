import sys
import re

def main(inp):
    somador = 0
    somadorLista = []
    somadorON = False

    pattern = re.compile(r'(?P<on>[Oo][Nn])|(?P<off>[Oo][Ff]{2})|(?P<show>=)|(?P<number>[+-]{0,1}\d+)')

    if (len(inp) == 1):
        for linha in sys.stdin:
            for match in pattern.finditer(linha):
                if match.group('on'):
                    somadorON = True
                elif match.group('off'):
                    somadorON = False
                elif match.group('show'):
                    print(' + '.join(str(number) for number in somadorLista) + ' = ' + str(somador))
                elif match.group('number'):
                    if somadorON:
                        somador += int(match.group('number'))
                        somadorLista.append(int(match.group('number')))

    elif (len(inp) == 2):
        with open(inp[1], 'r') as file:
            for linha in file:
                for match in pattern.finditer(linha):
                    if match.group('on'):
                        somadorON = True
                    elif match.group('off'):
                        somadorON = False
                    elif match.group('show'):
                        print(' + '.join(str(number) for number in somadorLista) + ' = ' + str(somador))
                    elif match.group('number'):
                        if somadorON:
                            somador += int(match.group('number'))
                            somadorLista.append(int(match.group('number')))

    else:
        print('Usage: python3 script.py [sequence.txt] or python3 script.py < sequence.txt')
        sys.exit(1)

        
if __name__ == '__main__':
    main(sys.argv)