'''
K-messed array sort - Pramp

Given an array of integers arr where each element is at most k places away
from its sorted position, code an efficient function sortMessedArray that
sorts arr. For instance, for an input array of size 10 and k = 2, an
element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

Example:
input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2
output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
import heapq
def sort_k_messed_array(arr, k):
    h = []
    n = len(arr)
    ans = []
    if k > n:
        k = k -1
    for i in range(k+1):
        heapq.heappush(h, arr[i])
    for i in range(k+1, n):
        ele = heapq.heappop(h)
        heapq.heappush(h, arr[i])
        ans.append(ele)
    for i in range(k+1):
        ele = heapq.heappop(h)
        ans.append(ele)
    return ans
# Test
arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2
print sort_k_messed_array(arr, k)
