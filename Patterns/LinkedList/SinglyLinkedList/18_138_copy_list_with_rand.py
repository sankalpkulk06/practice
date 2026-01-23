"""
Leetcode 138: Copy List with Random Pointer

Question:
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has a value equal to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
"""

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
    
    def printList(self, head):
        while head is not None:
            print(head.val, end=" ")
            head = head.next
        print()

    def copyRandomList(self, head):
        """
        Phase 1 (pass 1): copy the nodes and store the new nodes in a hashmap
        Phase 2 (pass 2): 
            - assign next and random using the hashmap
        return hashmap[head]
        """
        if not head:
            return None

        # Phase 1:
        """
        new_nodes = {
            "oldnode" : "newnode",
        }
        """
        new_nodes = {}
        curr = head
        while curr:
            new_nodes[curr] = ListNode(curr.val)
            curr = curr.next

        # Phase 2:
        curr = head
        while curr:
            new = new_nodes[curr]
            # returns the value of key curr.next
            new.next = new_nodes.get(curr.next) 
            new.random = new_nodes.get(curr.random)
            curr = curr.next
        
        return new_nodes[head]


if __name__ == "__main__":
    head = ListNode(7)
    head.next = ListNode(13)
    head.next.next = ListNode(11)
    head.next.next.next = ListNode(10)
    head.next.next.next.next = ListNode(1)
    print("Original list:")
    head.printList(head)
    print("Copied list:")
    head.printList(head.copyRandomList(head))