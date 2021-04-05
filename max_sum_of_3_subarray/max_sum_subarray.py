class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if len(nums)<k:
            return [0]

        running = 0
        n = len(nums)
        # running K element running sum ending at i, time complexity O(N)
        w = []
        for i, num in enumerate(nums):
            running+=nums[i]
            if i>=k:
                running -=nums[i-k]
                w.append(running)
            else:
                w.append(running)       

        # best k-sum position from left side
        left = [0] * n
        # best k-sum position from right side
        right = [0] * n

        best = 0
        for i in range(k-1,n):
            if w[i]>w[best]:
                left[i] = i
                best = i
            else:
                left[i] = best

        best = n-1
        for i in range(n-1,-1,-1):
            if w[i]>=w[best]:
                right[i] = i
                best = i
            else:
                right[i] = best
     
        ans = None
        best = float('-inf')      

        # walk through possible 3-subarray sum 
        for j in range(k, n-k):
            # left array, j-k+1 to j, right array
            left_sum = w[left[j-k]]
            mid_sum = w[j]
            right_sum = w[right[j+k]]

            if left_sum+mid_sum+right_sum > best:
                best = left_sum+mid_sum+right_sum
                # starting position for each array
                ans = left[j-k]-k+1, j-k+1, right[j+k]-k+1
                
        return ans        


my_sol = Solution()
nums = [1,2,1,2,6,7,5,1]
k=2
# result = my_sol.maxSumOfThreeSubarrays(nums,k)
# print(result)


nums= [1,2,1,2,1,2,1,2,1]
k=2
result = my_sol.maxSumOfThreeSubarrays(nums,k)
print(result)

            



