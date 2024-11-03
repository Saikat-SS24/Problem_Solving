""" Given an 0-indexed array of integers arr[] of size n, find its peak element. An element is considered to be peak 
if it's value is greater than or equal to the values of its adjacent elements (if they exist). The array is guaranteed 
to be in ascending order before the peak element and in descending order after it.

Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.

Example 1:

Input: 
n = 3
arr[] = {1, 2, 3}
Peak Element's Index: 2
Output: 1
Explanation: 
If the index returned is 2, then the output printed will be 1. 
Since arr[2] = 3 is greater than its adjacent elements, and 
there is no element after it, we can consider it as a peak 
element. No other index satisfies the same property.

Example 2:

Input:
n = 3
arr[] = {3, 4, 2}
Peak Element's Index: 1
Output: 1
Explanation: 
If the index returned is 1, then the output printed will be 1.
Since arr[1] = 4 is greater than its adjacent elements, and
there is no element after it, we can consider it as a peak
element. No other index satisfies the same property.
Your Task:
You don't have to read input or print anything. Complete the function peakElement() which takes the array arr[] and 
its size n as input parameters and return the index of the peak element.

Expected Time Complexity: O( log(n) ).
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 105
1 ≤ arr[i] ≤ 106 """


# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        return arr.index(max(arr))


#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends