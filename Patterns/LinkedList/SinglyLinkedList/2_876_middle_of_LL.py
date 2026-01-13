"""
Leetcode 876: Middle of the Linked List

Question:
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
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

    def middleNode(self, head):
        """
        1 -> 2 -> 3 -> 4 -> 5
        slow = 1; fast = 1
        slow = 2; fast = 3
        slow = 3; fast = 5
        slow = 4; fast = None
        return slow = 4 (middle node)
        """
        # both pointers start at the head
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow # return the middle node

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.printList(head)
    node = head.middleNode(head)
    head.printNode(node)