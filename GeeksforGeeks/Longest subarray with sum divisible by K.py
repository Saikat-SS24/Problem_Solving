""" Given an array arr containing N integers and a positive integer K, find the length of the longest sub array with 
sum of the elements divisible by the given value K.

Example 1:

Input:
N = 6, K = 3
arr[] = {2, 7, 6, 1, 4, 5}
Output: 
4
Explanation:
The subarray is {7, 6, 1, 4} with sum 18, which is divisible by 3.

Example 2:

Input:
N = 7, K = 3
arr[] = {-2, 2, -5, 12, -11, -1, 7}
Output: 
5
Explanation:
The subarray is {2,-5,12,-11,-1} with sum -3, which is divisible by 3.
Your Task:
The input is already taken care of by the driver code. You only need to complete the function longSubarrWthSumDivByK() 
that takes an array arr, sizeOfArray n and a  positive integer K, and returns the length of the longest subarray which 
has sum divisible by K. 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 105
1 <= K <= 109
-109 <= A[i] <= 109  """

#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) : 
		#Complete the function
        # unordered map 'um' implemented as hash table
        um = {}
     
        max_len = 0
        curr_sum = 0
     
        for i in range(n):
     
            curr_sum += arr[i]
            mod = ((curr_sum % K) + K) % K
            # if true then sum(0..i) is divisible by k
     
            if mod == 0:
                # update 'max_len'
                max_len = i + 1
     
            # if value 'mod_arr[i]' not present in 'um'
            # then store it in 'um' with index of its
            # first occurrence
            elif mod in um.keys():
                if max_len < (i - um[mod]):
                    max_len = i - um[mod]
     
            else:
                um[mod] = i
     
        # return the required length of longest subarray with
        # sum divisible by 'k'
        return max_len



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends