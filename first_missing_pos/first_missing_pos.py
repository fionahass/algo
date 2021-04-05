class Solution:
    def firstMissingPositive(self, nums):
        
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
         #use the index as the hash to record the frequency of each number        
        for i in range(len(nums)):
            nums[nums[i]%n]+=n
        # since missing number, the number in that position was not got added before    
        for i in range(1,len(nums)):
            if nums[i]//n==0:
                return i
        return n

my_sol = Solution()
nums=[2,2]
result = my_sol.firstMissingPositive(nums)   
print(result)     