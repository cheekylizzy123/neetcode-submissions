class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #need a dictionary to keep track of frequency of elements in the array, O(n)
        seen = {}
        for item in nums:
            if item in seen:
                seen[item] += 1
            else:
                seen[item] = 1
        
        maxi = []

        freq_lst = list(seen.values())   #list of frequencies 
        freq_lst.sort(reverse=True)   # sort in descending order 
        freq_lst = freq_lst[:k]    # only want the k most frequent elements

        for key,value in seen.items():   #.items() returns a list of key-value tuples [(k1,v1)]
            if value in freq_lst:
                maxi.append(key)
        
        return maxi






        