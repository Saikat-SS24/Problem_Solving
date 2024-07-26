""" Given a string str and an integer k, return true if the string can be changed into a pangram after at most k 
operations, else return false.

A single operation consists of swapping an existing alphabetic character with any other alphabetic character.

Note - A pangram is a sentence containing every letter in the english alphabet.

Examples :

Input: str = "the quick brown fox jumps over the lazy dog", k = 0
Output: true
Explanation: the sentence contains all 26 characters and is already a pangram.

Input: str = "aaaaaaaaaaaaaaaaaaaaaaaaaa", k = 25 
Output: true
Explanation: The word contains 26 instances of 'a'. Since only 25 operations are allowed. We can keep 1 instance 
and change all others to make str a pangram.

Input: str = "a b c d e f g h i j k l m", k = 20
Output: false
Explaanation: Since there are only 25 charaacters only in this case, so no amount of swapping we can have complete 
alphabets here.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)  

Constraints:
1<= str.size() <= 105
0<= k <= 50
str may contain duplicate characters.
str contains only lowercase alphabets or spaces. """


#User function Template for python3
from collections import Counter

class Solution:
    def kPangram(self,string, k):
        # code here
        string = string.replace(' ', '')
        mp = Counter(string)
        cnt, total = len(mp.keys()), sum(mp.values())
        return k + cnt >= 26 and total >= 26

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends