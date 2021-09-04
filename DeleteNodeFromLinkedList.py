import unittest
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class DeleteNodeFromLinkedList(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/553/
        """
        while node.next != None:
            node.val = node.next.val
            node = node.next

class DeleteNodeFromLinkedListTest(unittest.TestCase):
    def test_case1(self):

