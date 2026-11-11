# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        visited={}
        node=head
        #go through each node, note if not visited
        # if in visited already, return False

        while node is not None:
            if node not in visited:
                visited[node]=True
            else:
                return True
            node=node.next 
        return False 

        

        