""" There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) where S[i] is the start time 
of meeting i and F[i] is the finish time of meeting i. The task is to find the maximum number of meetings that can be 
accommodated in the meeting room. You can accommodate a meeting if the start time of the meeting is strictly greater 
than the finish time of the previous meeting. Print all meeting numbers.

Note: If two meetings can be chosen for the same slot then choose meeting with smaller index in the given array.

Example 1:

Input:
N = 6
S = {1,3,0,5,8,5}
F = {2,4,6,7,9,9} 
Output:
{1,2,4,5}
Explanation:
We can attend the 1st meeting from (1 to 2), then the 2nd meeting from (3 to 4), then the 4th meeting from (5 to 7), 
and the last meeting we can attend is the 5th from (8 to 9). It can be shown that this is the maximum number of meetings 
we can attend.

Example 2:

Input:
N = 1
S = {3}
F = {7}
Output:
{1}
Explanation:
Since there is only one meeting, we can attend the meeting.
Your Task:

You don't need to read input or print anything. Your task is to complete the function maxMeetings() which takes the 
arrays S, F, and its size N as inputs and returns the meeting numbers we can attend in sorted order.

Expected Time Complexity: O(N*log(N))
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 105
0 <= S[i] <= F[i] <= 109
Sum of N over all test cases doesn't exceeds 106 """


from typing import List


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        # code here
        meetings = sorted([(S[i], F[i], i+1) for i in range(N)], key=lambda x: (x[1], x[0]))
        res = [meetings[0][2]]
        last_finish = meetings[0][1]
        for s, f, i in meetings[1:]:
            if s > last_finish:
                res.append(i)
                last_finish = f
        return sorted(res)



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
        
        N = int(input())
        
        
        S=IntArray().Input(N)
        
        
        F=IntArray().Input(N)
        
        obj = Solution()
        res = obj.maxMeetings(N, S, F)
        
        IntArray().Print(res)
        

# } Driver Code Ends