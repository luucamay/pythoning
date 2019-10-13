def find_array_quadruplet(arr, s):
    n = len(arr)
    if n < 4:
        return []
    arr.sort()
    for i in range(n - 4):
        for j in range(i+1, n - 3):
            low = j + 1
            high = n - 1
            r = s - (arr[i] + arr[j])
            while low < high:
                aux = arr[low] + arr[high]
                if r > aux:
                    low += 1
                elif r < aux:
                    high -= 1
                else:
                    return [arr[i], arr[j], arr[low], arr[high]]
    return []

# Test
print find_array_quadruplet([2,7,4,0,9,5,1,3], 20)
