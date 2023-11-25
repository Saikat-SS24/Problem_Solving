""" Given an array arr of n elements in the following format {a1, a2, a3, a4, ... , an/2, b1, b2, b3, b4, ... , bn/2}, 
the task is shuffle the array to {a1, b1, a2, b2, a3, b3, ... , an/2, bn/2} without using extra space.
Note that n is even.

Example 1:

Input: 
n = 4, arr = {1, 2, 9, 15}
Output:  
1 9 2 15
Explanation: 
a1=1, a2=2, b1=9, b2=15. So the final array will be: a1, b1, a2, b2 = {1,9,2,15}.

Example 2:

Input: 
n = 6 arr = {1, 2, 3, 4, 5, 6} 
Output: 
1 4 2 5 3 6
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You 
just need to complete the function shuffleArray() that takes array arr, and an integer n as parameters and modifies 
the given array according to the above-given pattern.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ n ≤ 105
1 ≤ arri ≤ 103 """


class Solution:
    def shuffleArray(self, arr, n):
        # Your code goes here
        mid = n // 2
        i = 1
        j = mid
        while j < n:
            arr.insert(i, arr[j])
            arr.pop(j+1)
            j += 1
            i += 2
            
        return arr


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ob.shuffleArray(a,n)
        print(*a)

# } Driver Code Ends