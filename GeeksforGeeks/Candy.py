""" There are N children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:

Each child must have atleast one candy.
Children with a higher rating than its neighbors get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute.

Example 1:

Input:
N = 3
ratings = [1, 0, 2]
Output: 
5
Explanation: 
You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input:
N = 3
ratings = [1, 2, 2]
Output: 
4
Explanation: 
You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it statisfies the above two conditions.
Your Task:
You don't need to read input or print anything. Your task is to complete the function minCandy() which takes the 
interger N and integer array ratings as parameters and returns the minimum number of candies you need to have to 
distribute.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 105
0 ≤ ratingsi ≤ 109 """


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minCandy(self, N, ratings):
        # Code here
        if N == 1:
            return 1
        candies  = [1 for i in range(N)]
        for i in range(1,N):
            if ratings[i] > ratings[i-1] :
                candies[i] = max(candies[i],candies[i-1] + 1)
        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1] :
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ratings = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCandy(N, ratings)
        print(res)
        
# } Driver Code Ends