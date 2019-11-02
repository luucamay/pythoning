'''
Smallest Substring of All Characters

Given an array of unique characters arr and a string str.
Implement a function getShortestUniqueSubstring that finds
the smallest substring of str containing all the characters in arr.
Return "" (empty string) if such a substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:
input:  arr = ['x','y','z'], str = "xyyzyzyx"
output: "zyx
'''
def get_shortest_unique_substring(arr, str):
    head_index = 0
    result = ""
    unique_counter = 0
    count_map = {}
    for c in arr:
        count_map[c] = 0
    for tail_index in range(len(str)):
        tail_char = str[tail_index]
        if tail_char in count_map:
            tail_count = count_map[tail_char]
            if tail_count == 0:
                unique_counter += 1
            count_map[tail_char] = tail_count + 1
            # Push head forward
            while unique_counter == len(arr):
                temp_len = tail_index - head_index + 1
                if temp_len == len(arr):
                    return str[head_index:tail_index + 1]
                if result == "" or temp_len < len(result):
                    result = str[head_index:tail_index + 1]
                head_char = str[head_index]
                if head_char in count_map:
                    head_count = count_map[head_char] - 1
                    if head_count == 0:
                        unique_counter -= 1
                    count_map[head_char] = head_count
                head_index += 1
    return result
# Test cases
print get_shortest_unique_substring(['x', 'y', 'z'],'xyyzyzyx')
