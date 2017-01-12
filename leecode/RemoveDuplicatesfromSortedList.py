# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = head
        if start == None:
            return start
        while start.next != None:
            if start.val == start.next.val:
                start.next = start.next.next
            else:
                start = start.next
        return head