'''
Equalize the Array - Hackerrank

Karl has an array of integers. He wants to reduce the array until all remaining elements are equal. Determine the minimum number of elements to delete to reach his goal.

For example, if his array is , we see that he can delete the  elements  and  leaving . He could also delete both twos and either the  or the , but that would take  deletions. The minimum number of deletions is .

Function Description

Complete the equalizeArray function in the editor below. It must return an integer that denotes the minimum number of deletions required.

equalizeArray has the following parameter(s):

arr: an array of integers
Input Format

The first line contains an integer , the number of elements in .
The next line contains  space-separated integers .

Constraints

Output Format

Print a single integer that denotes the minimum number of elements Karl must delete for all elements in the array to be equal.

Sample Input

5
3 3 2 1 3
Sample Output

2   
Explanation

Array . If we delete  and , all of the elements in the resulting array, , will be equal. Deleting these  elements is minimal. Our only other options would be to delete  elements to get an array of either  or .
'''
def equalizeArray(arr):
    size = len(arr)
    my_map = {}
    maxi = 0
    for number in arr:
        if number in my_map:
            my_map[number] += 1
        else:
            my_map[number] = 1
        maxi = max(maxi, my_map[number])
    return size - maxi
# Test
print equalizeArray([3, 3, 2, 1, 3])