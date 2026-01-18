"""
Leetcode 2: Add Two Numbers

Question:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def printList(head):
        while head is not None:
            print(head.val, end=" ")
            head = head.next
        print()
    
    def printNode(self, head):
        print("Node value: ", head.val)

    @staticmethod
    def addTwoNumbers(l1, l2):
        """
        Approach:
        - create a dummy node to store the result
        - create a pointer to the dummy node
        - traverse the lists and add the values of the nodes
        - return the dummy node's next node
        """
        # init pointers
        dummy = ListNode(0)
        current = dummy 
        carry = 0

        # traverse the lists
        while l1 or l2 or carry:
            # get the values of the nodes
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # add the values and the carry
            total = val1 + val2 + carry
            # update the carry
            carry = total // 10
            # create a new node with the sum

            current.next = ListNode(total % 10)
            current = current.next
            # move the pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    result = ListNode.addTwoNumbers(l1, l2)
    print("Result:", ListNode.printList(result))