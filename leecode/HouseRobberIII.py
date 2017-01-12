# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.robsub(root)
        return max(res[0],res[1])
        
    def robsub(self,node):
        if node == None:
            return [0,0]
        left = self.robsub(node.left)
        right = self.robsub(node.right)
        res = []
        res.append(max(left[0],left[1]) + max(right[0],right[1]))
        res.append(node.val + left[0] + right[0])
        return res