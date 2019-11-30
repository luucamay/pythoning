'''
Top K frequent elements - Leetcode #347

Given a non-empty array of integers, return the k most frequent elements.

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''

# Time complexity of this approach is O(n) + O(klog(n))
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        h = []
        for num in d:
            h.append([-1*d[num], num])
        heapq.heapify(h)
        ans = [0]*k
        for i in range(k):
            pair = heapq.heappop(h)
            ans[i] = pair[1]
        return ans

