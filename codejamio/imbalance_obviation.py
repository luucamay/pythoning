'''
Imbalance Obviation - CodeJamIO
'''
def imbalance_obviation(numbers, n):
    order = ''
    arr = [0]*n
    for i in range(n):
        pos = numbers[i] - 1
        if i % 2 == 0:
            arr[pos] = 'R'
        else:
            arr[pos] = 'L'
    order = order.join(arr)       
    return order

# Test
t = int(input())
for i in range(t):
    n = int(input())
    nums = [int(x) for x in input().split()]
    ans = imbalance_obviation(nums, n)
    print('Case #{}: {}'.format(i+1, ans))
    


