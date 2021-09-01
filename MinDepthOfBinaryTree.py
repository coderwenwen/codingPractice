import unittest
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class MinDepthOfBinaryTree(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        https://leetcode.com/problems/minimum-depth-of-binary-tree/
        """
        childQueue = []
        childQueue.append(root)
        depthCount = 0
        if not root:
            return 0
        while len(childQueue) > 0:
            for i in childQueue:
                if i.left:
                    childQueue.append(i.left)
                    childQueue.pop(i)
                    depthCount = depthCount + 1
                if i.right:
                    childQueue.append(i.right)
                    childQueue.pop(i)
                    depthCount = depthCount + 1
                else:
                    return depthCount

class MinDepthOfBinaryTreeTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(MinDepthOfBinaryTree.minDepth(self, [3,9,20,null,null,15,7]), 1)

