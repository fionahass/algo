class Solution:
    def productEqB(self,nums,target):

        if len(nums)<1:
            return 0

        nums = sorted(nums)

        def recurse(nums,steps,target):

            product = 1
            for num in nums:
                product = product*num


            if product==target:

                return steps
            elif product > target:
                 # product > target, 
                 if nums[-1]>0:
                     nums[-1] -=1
                     return recurse(nums,steps+1,target)
                 else:
                     return 0    
            else:
                # product < target  
                nums[0]+=1
                return recurse(nums,steps+1,target)
 
        steps = recurse(nums,0,target)
        
        return steps    


    def productDP(self,nums,target):
    
        n = len(nums)
        factor =[]

        for i in range(1,target+1):
            if ( target % i ==0):
                factor.append()

        m = len(factor)
        
        dp =[ sys.maxsize for i in range(m)]

        dp[0] = 0

        for i in range(n):
            tmp = [sys.maxsize for i in range(m)]
            for j in range(m):
                if dp[j]!=sys.maxsize:
                    for k in range(j,m):
                        if factor[k] % factor[j]==0:
                            tmp[k] = min(tmp[k],dp[j]+abs(factor[k]//factor[j])-nums[i])       
            dp = tmp
        
        return dp[m-1]                    

my_sol = Solution()
nums = [1,3,5]
target = 12
result = my_sol.productEqB(nums,target)
print(result)