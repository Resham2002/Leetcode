# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        curr = root
        res = []
        queue = [root]  

        while len(queue) > 0:
            temp = []
            qLen = len(queue)
            for _ in range(qLen):
                curr = queue.pop(0)
                temp.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            res.append(temp)
        return res
