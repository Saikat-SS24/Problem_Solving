""" Given a linked list, your task is to complete the function isLengthEven() which contains the head of the linked 
list, and check whether the length of the linked list is even or not. Return true if it is even, otherwise false.

Examples:

Input: Linked list: 12->52->10->47->95->0
Output: true
Explanation: The length of the linked list is 6 which is even, hence returned true.

Input: Linked list: 9->4->3
Output: false
Explanation: The length of the linked list is 3 which is odd, hence returned false.

Expected Time Complexity: O(n)
Expected Auxillary Space: O(1)

Constraints:
1 <= number of nodes <= 105
1 <= elements of the linked list <= 105  """


class Solution:
    # your task is to complete this function
    # function should return false if length is even
    # else return true
    def isLengthEven(self, head):
        # Code here
        le = 1
        tmp = head
        while tmp:
            if tmp.next is not None:
                le += 1
            tmp = tmp.next
            
        if le % 2 == 0:
            return True
        else:
            return False

#{ 
 # Driver Code Starts
#main


class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("")


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        values = input().strip().split()
        for i in reversed(values):
            llist.push(i)
        flag = Solution().isLengthEven(llist.head)
        if flag:
            print("true")
        else:
            print("false")
        print("~")
        t -= 1
# Contributed by: Harshit Sidhwa

# } Driver Code Ends