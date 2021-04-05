class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<1:
            return 0

        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        M = (10 ** 9 + 7)

        if s[0]=="*":
            dp[1] = 9
        elif s[0]=="0":
            dp[1] = 0
        else:
            dp[1] = 1

        # time complexity O(n), space complexity O(n)
        for i in range(1,n):
            if s[i]=='*':
                # baseline 9 possible ways for char at i
                 dp[i+1] = 9*dp[i]
                 if s[i-1]=="1":
                    # additional 9 possible ways if char at i-1 is 1
                    dp[i+1] = (dp[i+1]+9*dp[i-1])
                 elif s[i-1]=="2":
                    # additional 6 possible ways if char at i-1 is 2
                    dp[i+1] = (dp[i+1]+6*dp[i-1])
                 elif s[i-1]=='*':
                    # additional 15 possible ways if char at i-1 is *
                    dp[i+1] = (dp[i+1]+15*dp[i-1])            
            else:

                dp[i+1] = dp[i] if s[i]!="0" else 0
                if s[i-1]=="1":
                    dp[i+1] = (dp[i+1] + dp[i-1])
                elif s[i-1]=="2" and s[i]<="6":
                    dp[i+1] = (dp[i+1] + dp[i-1])
                elif s[i-1]=="*":
                    if s[i]<="6":
                        dp[i+1] = (dp[i+1] + 2*dp[i-1])
                    else:
                        dp[i+1] = (dp[i+1] + dp[i-1])
            dp[i+1] %= M          
        return dp[-1]
                    


my_sol = Solution()
s="7*9*3*6*3*0*5*4*9*7*3*7*1*8*3*2*0*0*6*"
result= my_sol.decode(s)   
print(result)  

s ="*1*1*0"
result= my_sol.numDecodings(s)   
print(result) 
