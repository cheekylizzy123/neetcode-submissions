# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    #sort by key, then compile each iteration 
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        result=[pairs[:]]    #note that a copy of the list is added, rather than a reference 
        for i in range(1,len(pairs)):
            j = i-1
            while j >=0 and pairs[j].key>pairs[j+1].key:
                pairs[j],pairs[j+1]=pairs[j+1],pairs[j]
                j-=1
            result.append(pairs[:])
        return result 
        