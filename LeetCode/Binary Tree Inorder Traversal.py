from collections import deque

class Solution(object):
    def _in_order_iter(self, root):
        stack = deque()
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                yield root.val
                root = root.right

    def inorderTraversal(self, root):
        return list(self._in_order_iter(root))
