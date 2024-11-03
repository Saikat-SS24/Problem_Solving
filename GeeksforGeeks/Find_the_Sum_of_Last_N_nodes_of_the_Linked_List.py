""" Given a single linked list, calculate the sum of the last n nodes.

Note: It is guaranteed that n <= number of nodes.

Examples:

Input: Linked List: 5->9->6->3->4->10, n = 3
Output: 17
Explanation: The sum of the last three nodes in the linked list is 3 + 4 + 10 = 17.

Input: Linked List: 1->2, n = 2
Output: 3
Explanation: The sum of the last two nodes in the linked list is 2 + 1 = 3.

Constraints:
1 <= number of nodes, n <= 105
1 <= node->data <= 103

Method 
-> Calculate the length of the given Linked List. Let it be len.
-> First, traverse the (len – n) nodes from the beginning.
-> Then traverse the remaining n nodes and while traversing add them.
-> Return the added sum. """

#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        if n <= 0:
            return 0
        
        sum = 0
        len = 0
        tmp = head
        # calculating length of the list
        while tmp != None:
            len += 1
            tmp = tmp.next
        # counting first (len - n) nodes
        c = len - n
        tmp = head
        # traversing the 1st 'c' nodes
        while (tmp != None and c > 0):
            tmp = tmp.next
            c -= 1
        # now traversing the last 'n' nodes and adding them
        while tmp != None:
            sum += tmp.data
            tmp = tmp.next
            
        return sum

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
        n = int(data[2 * i])
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        ob = Solution()
        print(ob.sumOfLastN_Nodes(head, n))

# } Driver Code Ends