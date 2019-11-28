'''
Top K frequent words - Daily Interview Pro

Given a non-empty list of words, return the k most frequent words.
The output should be sorted from highest to lowest frequency,
and if two words have the same frequency, the word with lower
alphabetical order comes first. Input will contain only lower-case letters.

Example:
Input: ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"], k = 2
Output: ["pro", "daily"]
'''
import heapq
def top_k_frequent(words, k):
    d = {}
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    heap = []
    for word in d:
        heapq.heappush(heap, [-d[word], word])
    answer = []
    for i in range(k):
        pair = heapq.heappop(heap)
        answer.append(pair[1])
    return answer

# Test
words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print top_k_frequent(words, k)
# ['pro', 'daily']

