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
        if not root:
            return 0
        else:
            depthQueue = []
            depthQueue.append((root, 1))
            while len(depthQueue) > 0:
                if depthQueue[0][0].left != None:
                    depthQueue.append((depthQueue[0][0].left, depthQueue[0][1] + 1))
                if depthQueue[0][0].right != None:
                    depthQueue.append((depthQueue[0][0].right, depthQueue[0][1] + 1))
                elif depthQueue[0][0].left == None and depthQueue[0][0].right == None:
                    return depthQueue[0][1]
                depthQueue.pop(0)

