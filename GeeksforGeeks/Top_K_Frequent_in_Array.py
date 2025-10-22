""" Given a non-empty integer array arr[]. Your task is to find and return the top k elements which have the highest 
frequency in the array.

Note: If two numbers have the same frequency, the larger number should be given the higher priority.

Examples:

Input: arr[] = [3, 1, 4, 4, 5, 2, 6, 1], k = 2
Output: [4, 1]
Explanation: Frequency of 4 is 2 and frequency of 1 is 2, these two have the maximum frequency and 4 is larger than 1.

Input: arr[] = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], k = 4
Output: [5, 11, 7, 10]
Explanation: Frequency of 5 is 3, frequency of 11 is 2, frequency of 7 is 2, frequency of 10 is 1.

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105
1 ≤ k ≤ no. of distinct elements """

from collections import Counter

def topKFreq(arr, k):
    n = len(arr)
    mp = Counter(arr)
    # Store the elements of 'mp' in the list 'freq'
    freq = list(mp.items())
    # Sort the list 'freq' on the basis of the
    # 'compare' function
    freq.sort(key=lambda x: (x[1], x[0]), reverse=True)
    res = []
    # Extract and store the top k frequent elements
    for i in range(k):
        res.append(freq[i][0])
            
    return res