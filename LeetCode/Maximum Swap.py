""" You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.  
 
Constraints:
0 <= num <= 108  """


class Solution:
    def maximumSwap(self, num: int) -> int:
        num_to_str = list(str(num))
        temp = num_to_str[:]
    
        # swapping each digit and check for
        # the largest number
        for i in range(len(num_to_str)):
            for j in range(i + 1, len(num_to_str)):
    
                # Swapping current pair
                num_to_str[i], num_to_str[j] = num_to_str[j], num_to_str[i]
                if num_to_str > temp:
                    temp = num_to_str[:]
    
                # Reverting above change before next iteration 
                num_to_str[i], num_to_str[j] = num_to_str[j], num_to_str[i]
    
        # returning the largest number.
        return int("".join(temp))        