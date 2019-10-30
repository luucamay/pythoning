'''
Input:
string que son letras no case-sensitive
output:
numero de veces que se repite una letra
a = 2
b = 3
Pseudoce:
poner todas en miniusculas
ordenar la cadena
contar las letras y cuando es diferente imprimir en pantalla la letra actual y contador
'''
from collections import defaultdict
def contar_repetidos(string):
    dictionary = defaultdict(int)
    for i in range(len(string)):
        dictionary[string[i]] += 1
    for x in dictionary:
        print x, ":", dictionary[x]

contar_repetidos('jalasoft')