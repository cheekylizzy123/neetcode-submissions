class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def smash(x,y):
            if x < y:
                y = y-x
                return y
            return 0

        while len(stones) > 1:
            stones.sort()
            y = stones.pop()
            x=stones.pop()
            result = smash(x,y)
            if result != 0:
                stones.append(result)
        if stones==[]:
            return 0
        else:
            return stones.pop() 
        