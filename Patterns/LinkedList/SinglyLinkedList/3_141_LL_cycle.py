"""
Leetcode 141: Linked List Cycle

Question:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
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
    
    def hasCycle(self, head):
        """
        1 -> 2 -> 3 -> 4 
             |----------| 
        slow = 1; fast = 1
        slow = 2; fast = 3
        slow = 3; fast = 2
        slow = 4; fast = 4 (cycle detected)
        return True
        """
        # init 
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True # return True if there is a cycle, False otherwise
        return False # return False if there is no cycle

if __name__ == "__main__":
    # Example 1: No cycle
    print("Example 1: No cycle")
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.printList(head)
    print(f"Has cycle: {head.hasCycle(head)}")
    
    # Example 2: With cycle (5 -> 2, creating cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 2 -> ...)
    print("\nExample 2: With cycle")
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    head2.next.next.next.next = ListNode(5)
    head2.next.next.next.next.next = head2.next  # Create cycle: 5 points back to 2
    # Note: Can't print this list as it would loop infinitely
    print("List: 1 -> 2 -> 3 -> 4 -> 5 -> 2 (cycle)")
    print(f"Has cycle: {head2.hasCycle(head2)}")