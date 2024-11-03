""" Given a singly linked list and a key, count the number of occurrences of the given key in the linked list.

Examples:

Input: Linked List: 1->2->1->2->1->3->1, key = 1
Output: 4
Explanation: 1 appears 4 times.

Input: Linked List: 1->2->1->2->1, key = 3
Output: 0
Explanation: 3 appears 0 times.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ number of nodes, key ≤ 105
1 ≤ data of node ≤ 105  """

"""  
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def count(self, head, key):
        # Code here
        cnt = 0
        tmp = head
        while tmp:
            if tmp.data == key:
                cnt += 1
            tmp = tmp.next
                
        return cnt

#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0])
    for i in range(1, t + 1):
        arr = list(map(int, data[2 * i - 1].split()))
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        key = int(data[2 * i])
        ob = Solution()
        print(ob.count(head, key))
        print("~")

# } Driver Code Ends