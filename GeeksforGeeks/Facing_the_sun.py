""" Given an array height representing the heights of buildings. You have to count the buildings that will see the 
sunrise (Assume the sun rises on the side of the array starting point).

Note: The height of the building should be strictly greater than the height of the buildings left in order to see the 
sun.

Examples :

Input: height = [7, 4, 8, 2, 9]
Output: 3
Explanation: As 7 is the first element, it can see the sunrise. 4 can't see the sunrise as 7 is hiding it. 8 can see. 
2 can't see the sunrise. 9 also can see the sunrise.

Input: height = [2, 3, 4, 5]
Output: 4
Explanation: As 2 is the first element, it can see the sunrise.  3 can see the sunrise as 2 is not hiding it. Same for 
4 and 5, they also can see the sunrise.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1) 

Constraints:
1 ≤ height.size() ≤ 106
1 ≤ heighti ≤ 108   """

#User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        first = height[0]
        count = 1
        for i in height:
            if i > first:
                count = count+1
                first = i
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        height = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(height)
        print(ans)

# } Driver Code Ends