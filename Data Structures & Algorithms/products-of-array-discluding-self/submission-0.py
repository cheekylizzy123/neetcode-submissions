class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #multiply all then just divide the one element nums[i]
        # but if nums got 0, then only return output for nums[i]==0
        product = 1 
        products = []
        if 0 not in nums: 
            for n in nums:
                product = n * product 
            products = [product//nums[i] for i in range(len(nums))]
        else:
            products = [0 for _ in range(len(nums))]
            j = nums.index(0)
            for n in range(len(nums)):
                if n == j:
                    continue 
                product *= nums[n] 
            products[j]=product

        
        return products 
        
        



        



            
            
                