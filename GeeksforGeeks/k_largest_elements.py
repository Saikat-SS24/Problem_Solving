""" Given an array arr[] of positive integers and an integer k, Your task is to return k largest elements in 
decreasing order. 

Examples:

Input: arr[] = [12, 5, 787, 1, 23], k = 2
Output: [787, 23]
Explanation: 1st largest element in the array is 787 and second largest is 23.

Input: arr[] = [1, 23, 12, 9, 30, 2, 50], k = 3 
Output: [50, 30, 23]
Explanation: Three Largest elements in the array are 50, 30 and 23.

Input: arr[] = [12, 23], k = 1
Output: [23]
Explanation: 1st Largest element in the array is 23.

Constraints:
1 ≤ k ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106 """

 
class Solution:
    def kLargest(self, arr, k):
        # Your code here
        cnt, i = 0, 0
        res = []
        arr.sort(reverse = True)
        while(cnt != k):
            ele = arr[i]
            res.append(ele)
            i += 1
            cnt += 1
            
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.kLargest(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends