# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        start = head
        halfList = head
        if start == None or start.next == None or start.next.next == None:
            return 
        while start.next != None:
            if start.next.next != None:
                start = start.next.next
                halfList = halfList.next
            else:
                break
        endNode = None
        if start.next == None:
            endNode = start
        else:
            endNode = start.next
            
        newStart = halfList.next
        halfList.next = None
        nextNode = newStart.next
        newStart.next = None
        while nextNode != None:
            tempNode = nextNode.next
            nextNode.next = newStart
            newStart = nextNode
            nextNode = tempNode
        start = head
        while endNode != None:
            nextStart = start.next
            nextEnd = endNode.next
            start.next = endNode
            endNode.next = nextStart
            start = nextStart
            endNode = nextEnd