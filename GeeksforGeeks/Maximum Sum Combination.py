"""Given two integer array A and B of size N each.
A sum combination is made by adding one element from array A and another element of array B.
Return the maximum K valid sum combinations from all the possible sum combinations.

Note : Output array must be sorted in non-increasing order.

Example 1:

Input:
N = 2
K = 2
A [ ] = {3, 2}
B [ ] = {1, 4}
Output: {7, 6}
Explanation: 
7 -> (A : 3) + (B : 4)
6 -> (A : 2) + (B : 4)
Example 2:

Input:
N = 4
K = 3
A [ ] = {1, 4, 2, 3}
B [ ] = {2, 5, 1, 6}
Output: {10, 9, 9}
Explanation: 
10 -> (A : 4) + (B : 6)
9 -> (A : 4) + (B : 5)
9 -> (A : 3) + (B : 6)
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxCombinations() which 
takes the interger N,integer K and two integer arrays A [ ] and B [ ] as parameters and returns the maximum K valid 
distinct sum combinations .

Expected Time Complexity: O(Nlog(N))
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤  105
1 ≤ K ≤  N
1 ≤ A [ i ] , B [ i ] ≤ 104 """

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import heapq

class Solution:
    def maxCombinations(self, N, K, A, B):
        # Code here
        A.sort(reverse=True)
        B.sort(reverse=True)
        visited = [1]+[0]*(len(A) - 1)
        heap = [(-A[0]-B[0], 0, 0)]
        ans = []
        for _ in range(K):
            val, i, j = heapq.heappop(heap)
            ans.append(-val)
            if i+1 < len(A) and visited[i + 1] == j:
                heapq.heappush(heap, (-A[i+1] - B[j], i+1, j))
                visited[i + 1] += 1
            if j+1 < len(B) and visited[i] == j+1:
                heapq.heappush(heap, (-A[i]-B[j+1], i, j+1))
                visited[i] += 1
        return ans
#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxCombinations(N, K, A, B)
        for val in res:
            print(val, end =' ')
        print()
# } Driver Code Ends