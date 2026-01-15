"""
leetcode 142: Linked List Cycle II

Question:
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return the node where the cycle begins. If there is no cycle, return null.
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
        if head is None:
            print("No cycle detected (None)")
        else:
            print("Node value: ", head.val)
    
    def detectCycle(self, head):
        """
        Approach:
        - traverse the list 
        - add the visited node to a set
        - if the node is already in the set, return that node
        - else, move next
        - if no cycle, return None
        """

        # init
        curr = head
        visited = set()

        # traverse the list
        while curr:
            # if the node is already in the set, return that node
            if curr in visited:
                return curr
            else:
                visited.add(curr)
                curr = curr.next
        return None

if __name__ == "__main__":
    # Example 1: No cycle
    print("Example 1: No cycle")
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.printList(head)
    node = head.detectCycle(head)
    head.printNode(node)
    
    # Example 2: With cycle (5 -> 2, creating cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 2 -> ...)
    print("\nExample 2: With cycle")
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    head2.next.next.next.next = ListNode(5)
    head2.next.next.next.next.next = head2.next  # Create cycle: 5 points back to 2
    print("List: 1 -> 2 -> 3 -> 4 -> 5 -> 2 (cycle starts at node 2)")
    node2 = head2.detectCycle(head2)
    head2.printNode(node2)