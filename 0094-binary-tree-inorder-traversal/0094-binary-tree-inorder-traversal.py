# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        elements = []
        #visit left tree
        if root == None:
            return elements
        if root.left:
            elements += self.inorderTraversal(root.left)
        #visit base node
        elements.append(root.val)
        #visit right tree
        if root.right:
            elements += self.inorderTraversal (root.right)
        return elements