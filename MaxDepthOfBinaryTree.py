import unittest
# Definition for a binary tree node.
# class TreeNode(object):
def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class MaxDepthOfBinaryTree(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/555/
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

                if len(depthQueue) == 1:
                    break
                else:
                    depthQueue.pop(0)
            return depthQueue[0][1]



