"""
Leetcode 92: Reverse Linked List II

Question:
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def printList(self, head):
        while head is not None:
            print(head.val, end=" ")
            head = head.next
        print()
    
    def printNode(self, head):
        print("Node value: ", head.val)

    def reverseBetween(self, head, left, right):
        """
        Approach:
        Phase 1: find the node before the left position
        Phase 2: reverse the nodes between left and right
        Phase 3: connect the reversed nodes to the original list
        """

        # Phase 1: find the node before the left position
        dummy = ListNode(0)
        dummy.next = head
        prevLeft = dummy
        current = head

        for i in range(left - 1):
            prevLeft = prevLeft.next
            current = current.next
        # prevLeft is the node before the left position
        # current is the left position

        # Phase 2: reverse the nodes between left and right
        prev = None
        for i in range(right-left+1):
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        # prev is the new head of the reversed nodes
        # current is the node after the right position

        # Phase 3: connect the reversed nodes to the original list
        prevLeft.next.next = current
        prevLeft.next = prev
        
        return dummy.next

if __name__ == "__main__":
    # create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print("Original list:")
    head.printList(head)
    print("List after reversing between positions 2 and 4:")
    res = head.reverseBetween(head, 2, 4)
    head.printList(res)