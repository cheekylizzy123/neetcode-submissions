class Solution:
    def countBits(self, n: int) -> List[int]:
        counts=[]
        for num in range(n+1):
            binary=str(bin(num))
            counts.append(binary.count("1"))
        return counts 


