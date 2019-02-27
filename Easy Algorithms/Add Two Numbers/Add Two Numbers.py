# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        total1 = 0
        total2 = 0
        placeValue = 1
        while l1 != None:
            total1 += (l1.val * placeValue)
            placeValue *= 10
            l1 = l1.next
            
        placeValue = 1
        while l2 != None:
            total2 += (l2.val * placeValue)
            placeValue *= 10
            l2 = l2.next
            
        total = str(total1 + total2)
        
        result = list()
        for i in range(len(total)-1, -1, -1):
            result.append(int(total[i]))
        return result
