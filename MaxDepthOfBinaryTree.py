# Definition for a binary tree node.
# class TreeNode(object):
def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
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
            depthQueue.append(root)
            depthCount = 0
            while len(depthQueue) > 0:
                for i in depthQueue:
                    if i.left:
                        depthCount = depthCount + 1
                        depthQueue.append(i.left)
                    if i.right:
                        depthCount = depthCount + 1
                        depthQueue.append(i.right)
                    else:
                        depthQueue.pop(i)
            return depthCount

