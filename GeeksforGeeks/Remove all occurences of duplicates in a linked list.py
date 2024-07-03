""" Given a sorted linked list, delete all nodes that have duplicate numbers (all occurrences), leaving only numbers 
that appear once in the original list, and return the head of the modified linked list. 

Examples:

Input: Linked List = 23->28->28->35->49->49->53->53
Output: 23 35
Explanation: The duplicate numbers are 28, 49 and 53 which are removed from the list.

Input: Linked List = 11->11->11->11->75->75
Output: Empty list
Explanation: All the nodes in the linked list have duplicates. Hence the resultant list would be empty.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ size(list) ≤ 105 """

#User function Template for python3

"""
# Linked list Node class

    class Node :
        def __init__(self, val):
            self.data = val
            self.next = None

"""

class Solution:
    def removeAllDuplicates(self, head):
        #code here
        # Create a temp node that points to the head of the list
        temp = Node(0)
        temp.next = head
        # Initialize current node to temp
        curr = temp
        while curr.next and curr.next.next:
            # If the current node's next two nodes have the same data, we have duplicates
            if curr.next.data == curr.next.next.data:
                # Store the duplicate value
                duplicate_value = curr.next.data
                # Skip all nodes with the duplicate value
                while curr.next and curr.next.data == duplicate_value:
                    curr.next = curr.next.next
            else:
                # Move to the next node
                curr = curr.next
        
        return temp.next

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# Node Class
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # prints the elements of linked list starting with head
    def printList(self, head):
        if head is None:
            print(' ')
            return
        curr_node = head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print(' ')


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        N = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        ob = Solution()
        head = ob.removeAllDuplicates(a.head)
        a.printList(head)

# } Driver Code Ends