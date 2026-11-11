import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=[]
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        #keep only k biggest elements everytime a num is appended
        if len(self.heap)<self.k:    #not full yet, can add element
            heapq.heappush(self.heap, val)
        elif val >self.heap[0]:   #root of heap
            heapq.heapreplace(self.heap,val)
        return self.heap[0]   #return new root, that's the smallest of k largest values (min-heap)
