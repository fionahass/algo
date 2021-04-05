class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        
        if len(envelopes)<1:
            return 0

        # sort envelops by ascending order ix x[0] but descending order in x[1]
        # time complexity O(nlog(n))
        envelopes = sorted(envelopes,key = lambda x:(x[0],-x[1]))
        size = 0
        dp = [0]*len(envelopes)

        # time complexity O(nlog(n))
        for w,h in envelopes:
            i,j=0,size
            while i < j:
                mid = (i+j)/2
                if dp[mid] < h:
                    i = mid+1
                else:
                    j = mid
            dp[i] = h
            size = max(i+1, size)

        return size
    


envelopes = [[5,4],[6,4],[6,7],[2,3]]     
my_sol = Solution()
result = my_sol.maxEnvelopes(envelopes)
print(result)