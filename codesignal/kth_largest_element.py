'''
Kth Largest Element - CodeSignal

Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order, not the kth distinct element.

source: https://app.codesignal.com/interview-practice/task/BG94ZFECSNo6Kv7XW/description

'''
# Sorting and picking the element
def kthLargestElement(nums, k):
    # k <= nums.length
    # sort, then go to the k position
    nums.sort(reverse=True)
    return nums[k-1]
# test
numbers = [7,6,5,4,3,2,1]
k = 2
print(kthLargestElement(numbers, k))

# Solution using heaps
import heapq


def kthLargestElement2(nums, k):
    # use a heap
    h = []
    for num in nums:
        heapq.heappush(h, -1 * num)
    for i in range(k):
        ans = heapq.heappop(h)
    return -1 * ans

print(kthLargestElement2(numbers, k))

