"""
Leetcode 1721: Swap Nodes in a Linked List

Question:
You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
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

    def swapNodes(self, head, k):
        """
        Approach:
        - find the kth node from the beginning
        - find the kth node from the end
        - swap the values of the two nodes
        - return the head of the list
        """
        # Phase 1: find the kth node from the beginning
        left = head
        for i in range(k-1):
            left = left.next
        
        # Phase 2: find the kth node from the end
        fast = head
        for i in range(k):
            fast = fast.next
        
        right = head
        while fast:
            right = right.next
            fast = fast.next
        
        # Phase 3: swap the values of the two nodes
        left.val, right.val = right.val, left.val
        
        return head
    
    

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.swapNodes(head, 2)
    head.printList(head)