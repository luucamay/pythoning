'''
Group anagrams problem from Leetcode

Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note: 
- All inputs will be in lowercase.
- The order of your output does not matter.
'''
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strings):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictionary = defaultdict(list)
        for x in strings:
            aux = list(x)
            aux.sort()
            key = "".join(aux)
            if not dictionary[key]:
                dictionary[key] = [x]
            else:
                dictionary[key].append("".join(x))
        return dictionary.values()