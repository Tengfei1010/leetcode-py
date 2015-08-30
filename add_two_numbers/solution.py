# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum1 = 0
        sum2 = 0
        current = l1
        count = 0
        while current:
            sum1 += current.val * pow(10, count)
            count += 1
            current = current.next

        current = l2
        count = 0
        while current:
            sum2 += current.val * pow(10, count)
            count += 1
            current = current.next

        sum1 += sum2
        result = ListNode(0)
        if sum1 == 0:
            return result

        current_node = result
        while sum1:
            value = sum1 % 10
            sum1 /= 10
            current_node.next = ListNode(value)
            current_node = current_node.next

        return result.next
