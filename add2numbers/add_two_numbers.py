# https://leetcode.com/problems/add-two-numbers/#/description
# Definition for singly-linked list.
from itertools import zip_longest
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # You cant extend this class in Leet's IDE
    # so I added essentially the same implementation
    # to class Solution
    def to_int(self):
        int_string = str(self.val)
        current = self.next

        while current:
            int_string += str(current.val)
            current     = current.next

        return int(int_string[::-1])

    def nodes(self):
        current = self.next
        nodes = [current]
        while current:
            current = current.next
            nodes.append(current)

    def to_reverse_int(self):
        vals = [self.val]
        current = self.next
        while current:
            vals.append(current.val)
            current = current.next

        return vals

        # if self.next:
        #     return self.next.next
        # else:
        #     raise StopIteration
        #
        # return self.next




class Solution(object):
    # Running in Leet's IDE breaks if you snake case this.
    def addTwoNumbers(self, l1, l2):
        added = self.to_int(l1) + self.to_int(l2)
        nodes = []
        for num in str(added)[::-1]:
            nodes.append(int(num))
        return nodes
        # for num in str(added)[::-1]:
        #     node = ListNode(int(num))
        #     if len(nodes) == 0:
        #         nodes.append(node)
        #     else:
        #         nodes[-1].next = node
        #
        # return nodes

    def to_int(self, node):
        int_string = str(node.val)
        current = node.next

        while current:
            int_string += str(current.val)
            current     = current.next

        return int(int_string[::-1])

    def carry_two_numbers(self, l1, l2):
        zipped      = zip_longest(l1.to_reverse_int(), l2.to_reverse_int())
        reverse_sum = []
        carry       = 0
        for a,b in zipped:
            a = int(a or 0)
            b = int(b or 0)
            val = a + b + carry

            if val >= 10:
                carry = 1
                val   = 0
            else:
                carry = 0

            reverse_sum.append(val)
        return reverse_sum







a = ListNode(2)
a2 = ListNode(4)
a.next = a2
a3 = ListNode(3)
a2.next = a3
# print(a.to_int())

b = ListNode(5)
b2 = ListNode(6)
b.next = b2
b3 = ListNode(4)
b2.next = b3
# print(b.to_int())

# s = Solution()
# print(s.addTwoNumbers(a, b))

s = Solution()
# print(s.carry_two_numbers(a, b))

# Unequal length
s = Solution()
b3.next = ListNode(1)
print(s.carry_two_numbers(a, b))
