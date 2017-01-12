# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head :
            nodeA = head
            nodeB = head
            while nodeB :
                if nodeA.next :
                    nodeA = nodeA.next
                else:
                    return False
                if nodeB.next and nodeB.next.next :
                    nodeB = nodeB.next.next
                else:
                    return False
                if nodeA.val == nodeB.val :
                    return True
            return False
        else:
            return False
        