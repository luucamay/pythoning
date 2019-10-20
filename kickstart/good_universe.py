def find_max_k(n, elements, m):
    k = 0
    suma = sum(elements)
    print suma
    if(suma > m):
        return -1
    while suma <= m:
        k += 1
        new_suma = 0
        for i in range(n):
            new_suma += (elements[i]^k)
        suma = new_suma
    return k-1

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  elements = [int(s) for s in raw_input().split(" ")]
  k = find_max_k(n, elements, m)
  print "Case #{}: {}".format(i, k)