# Definition for singly-linked list.
from heapq import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = nex


class Solution:
    def mergeKLists(self, lists):

        
        if not lists:
            return None


        minHeap = []
        n = len(lists)
        tail = result = ListNode(0) 
        

        # push in head from each linked list
        for i in range(n):
            if lists[i]:
                heappush(minHeap,(lists[i].val, i, lists[i]))

        while minHeap:
            cur_val, cur_list,cur_node = heappop(minHeap)
            
            
            if cur_node.next:
                next_node = cur_node.next
                heappush(minHeap,(next_node.val,cur_list,next_node))
            
            tail.next = cur_node
            tail = tail.next
            cur_node.next = None
            

        return result.next


                


                



