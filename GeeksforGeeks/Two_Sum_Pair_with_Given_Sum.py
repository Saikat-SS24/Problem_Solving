""" Given an array arr[] of positive integers and another integer target. Determine if there exists two distinct 
indices such that the sum of there elements is equals to target.

Examples:

Input: arr[] = [1, 4, 45, 6, 10, 8], target = 16
Output: true
Explanation: arr[3] + arr[4] = 6 + 10 = 16.

Input: arr[] = [1, 2, 4, 3, 6], target = 11
Output: false
Explanation: None of the pair makes a sum of 11.

Input: arr[] = [11], target = 11
Output: false
Explanation: No pair is possible as only one element is present in arr[].

Constraints:
1 ≤ arr.size ≤ 105
1 ≤ arr[i] ≤ 105
1 ≤ target ≤ 2*105 """

#User function Template for python3
class Solution:
    def twoSum(self, arr, target):
        # code here
        # Create a set to store the elements
        s = set()
        # Iterate through each element in the array
        for num in arr:
            # Calculate the complement that added to
            # num, equals the target
            complement = target - num
            # Check if the complement exists in the set
            if complement in s:
                return True
            # Add the current element to the set
            s.add(num)
        # If no pair is found
        return False
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends