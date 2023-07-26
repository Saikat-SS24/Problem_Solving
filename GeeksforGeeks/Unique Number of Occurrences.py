# Given an array arr of N integers, the task is to check whether the frequency of the elements in the array is unique or
# not. Or in other words, there are no two distinct numbers in array with equal frequency. If all the frequency is 
# unique then return true, else return false.

# Input:
# N = 5
# arr = [1, 1, 2, 5, 5]
# Output:
# false
# Explanation:
# The array contains 2 (1’s), 1 (2’s) and 2 (5’s), 
# since the number of frequency of 1 and 5 are the same i.e. 2 times. 
# Therefore, this array does not satisfy the condition.

# Input:
# N = 10
# arr = [2, 2, 5, 10, 1, 2, 10, 5, 10, 2]
# Output:
# true
# Explanation:
# Number of 1’s -> 1
# Number of 2’s -> 4
# Number of 5’s -> 2
# Number of 10’s -> 3.
# Since, the number of occurrences of elements present in the array is unique. 
#Therefore, this array satisfy the condition.



from typing import List


class Solution:
    def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        # code here
        freq = {}
        freqSet = set()
     
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
     
        for f in freq.values():
            freqSet.add(f)
     
        return len(freqSet) == len(freq)
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.isFrequencyUnique(n, arr)
        
        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends