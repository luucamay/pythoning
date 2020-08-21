'''
Telefono - Juez patito
https://jv.umsa.bo/problem.php?cid=1927&pid=1

Maybe use: list.count()
'''
def format_num(string):
    n = len(string)
    num_norm = ''
    for c in string:
        if c == '-':
            continue
        elif c in ['A', 'B', 'C']:
            num_norm += '2'
        elif c in ['D', 'E', 'F']:
            num_norm += '3'
        elif c in ['G', 'H', 'I']:
            num_norm += '4'
        elif c in ['J', 'K', 'L']:
            num_norm += '5'
        elif c in ['M', 'N', 'O']:
            num_norm += '6'
        elif c in ['P', 'R', 'S']:
            num_norm += '7'
        elif c in ['T', 'U', 'V']:
            num_norm += '8'
        elif c in ['W', 'X', 'Y']:
            num_norm += '9'
        else:
            num_norm += c
    return num_norm

n = input()
print(format_num(n))


