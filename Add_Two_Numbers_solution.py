# 2. Add Two Numbers
#You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#Example:

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.

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
        num = []
        n = 0
        while(l1 and l2):
            sum = l1.val + l2.val + n
            if sum >= 10:
                num.append(sum-10)
                n = 1
            elif sum < 10:
                num.append(sum)
                n = 0 
            if l1.next and (not l2.next):
                l1 = l1.next
                l2.val = 0
            elif l2.next and (not l1.next):
                l2 = l2.next
                l1.val = 0
            else:
                l1 = l1.next
                l2 = l2.next
    
        if n == 1:
            num.append(1)
        return num