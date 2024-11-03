""" Given elements as nodes of the two singly linked lists. The task is to multiply these two linked lists, say L1 
and L2.

Note: The output could be large take modulo 10^9+7.

Examples :

Input: LinkedList L1 : 3->2 , LinkedList L2 : 2
Output: 64
Explanation: 
Multiplication of 32 and 2 gives 64.

Input: LinkedList L1: 1->0->0 , LinkedList L2 : 1->0
Output: 1000
Explanation: 
Multiplication of 100 and 10 gives 1000.

Expected Time Complexity: O(max(n,m))
Expected Auxilliary Space: O(1)
where n is the size of L1 and m is the size of L2

Constraints:
1 <= number of nodes <= 105
1 <= node->data <= 103   """

# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        tmp1 = first
        tmp2 = second
        num1 = 0
        num2 = 0
        while tmp1:
            num1 = (num1 * 10 + tmp1.data)% (1000000007)
            tmp1 = tmp1.next
        while tmp2:
            num2 = (num2 * 10 + tmp2.data)% (1000000007)
            tmp2 = tmp2.next

        return (num1*num2) % (1000000007)


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def new_node(data):
    return Node(data)


def push(head_ref, new_data):
    new_Node = new_node(new_data)
    new_Node.next = head_ref[0]
    head_ref[0] = new_Node


def reverse(r):
    prev = None
    cur = r[0]
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    r[0] = prev


def free_list(Node):
    while Node:
        temp = Node
        Node = Node.next
        del temp


def print_list(Node):
    while Node:
        print(Node.data, end=" ")
        Node = Node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        first, second = [None], [None]
        arr = list(map(int, input().split()))
        for num in arr:
            push(first, num)

        brr = list(map(int, input().split()))
        for num in brr:
            push(second, num)

        reverse(first)
        reverse(second)

        ob = Solution()
        res = ob.multiply_two_lists(first[0], second[0])
        print(res)

# } Driver Code Ends