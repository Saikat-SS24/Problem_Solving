""" Given a linked list sorted in ascending order and an integer called data, insert data in the linked list such 
that the list remains sorted.

Example 1:

Input:
LinkedList: 25->36->47->58->69->80
data: 19
Output: 
19 25 36 47 58 69 80
Explanation:
After inserting 19 the sorted linked list will look like the one in the output.
Example 2:

Input:
LinkedList: 50->100
data: 75
Output: 
50 75 100
Explanation:
After inserting 75 the sorted linked list will look like the one in the output.
Your Task:
The task is to complete the function sortedInsert() which should insert the element in sorted Linked List and return 
the head of the linked list

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 104
-99999 <= A[i] <= 99999, for each valid i """


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.prev=self.head
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.prev = self.head
        else:
            self.prev.next = new_node
            self.prev = self.prev.next

def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


# } Driver Code Ends
#User function Template for python3

class Solution:
    def sortedInsert(self, head1,key):
        # code here
        # return head of edited linked list
        # If the linked list is empty, create a new node with the given key and return it as the new head.
        if head1 == None:
            return Node(key)

        # If the key is smaller than the value in the current head, insert a new node before the current head and update the head.
        if head1.data > key:
            temp = Node(key)
            temp.next = head1
            return temp

        # Initialize a 'curr' pointer to traverse the linked list.
        curr = head1

        # Traverse the linked list to find the appropriate position to insert the new node.
        while curr.next and curr.next.data <= key:
            curr = curr.next

        # Store the current next node in a temporary variable.
        temp = curr.next

        # Create a new node with the given key and insert it between 'curr' and 'temp'.
        curr.next = Node(key)

        # Connect the new node to the rest of the list.
        curr.next.next = temp

        # Return the updated head of the linked list.
        return head1

#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        
        key=int(input())
        h=Solution().sortedInsert(a.head,key)
        printList(h)

# } Driver Code Ends