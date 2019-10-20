
def find_max_k(n, elements, m):
    k = 0
    suma = sum(elements)
    if(suma > m):
        return -1
    while suma <= m:
        k += 1
        new_suma = 0
        for i in range(n):
            new_suma += (elements[i]^k)
        suma = new_suma
    return k-1
'''
N = 3
M = 27
numbers = [8,2,4]
print find_max_k(N,numbers,M)
'''