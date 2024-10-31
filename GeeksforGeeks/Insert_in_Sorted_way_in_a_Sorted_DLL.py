""" Given a sorted doubly linked list and an element x, you need to insert the element x into the correct position in 
the sorted Doubly linked list(DLL).

Note: The DLL is sorted in ascending order

Example:

Input: LinkedList: 3->5->8->10->12 , x = 9
Output: 3->5->8->9->10->12
Explanation: Here node 9 is inserted in the Doubly Linked-List.

Input: LinkedList: 1->4->10->11 , x = 15
Output: 1->4->10->11->15

Constraints:
1 <= number of nodes <= 103
1 <= node -> data , x <= 104 """

#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        #code here
        new = Node(x)
        if x <= head.data:
            new.next = head
            return new
        temp = head
        while temp.next:
            if x >= temp.data and x <= temp.next.data:
                new.next = temp.next
                temp.next = new
                return  head
            temp = temp.next
        temp.next = new
        return head

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        values = list(map(int, input().strip().split()))
        head = None
        tail = None

        for value in values:
            if head is None:
                head = Node(value)
                tail = head
            else:
                tail.next = Node(value)
                tail.next.prev = tail
                tail = tail.next

        value_to_insert = int(input().strip())
        solution = Solution()
        head = solution.sortedInsert(head, value_to_insert)
        print_list(head)

        print("~")

# } Driver Code Ends