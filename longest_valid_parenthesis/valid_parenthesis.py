from collections import Counter
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s)<=1:
            return 0
        unmatched_left = [False]*len(s)
        unmatched_right = [False]*len(s)
        max_matched = 0
        
        for i in range(len(s)):
            if s[i]==")":
                unmatched_right[i]=True
            elif s[i]=="(":
                unmatched_left[i]=True       

        for i in range(1,len(s)):
            if s[i]==")":
                k = i-1
                while k>=0 and unmatched_left[k]==False:
                    k-=1
                print(i,k,s[k])    
                if k>=0:    
                    # find a matching left
                    unmatched_left[k]  =  False
                    unmatched_right[i] = False
                else:
                    # can't find a matching left
                    unmatched_right[k]=True
        
        running = 0
        for i in range(len(s)):
            if s[i]=="(":
                matched  = True if unmatched_left[i]==False else False
            elif s[i]==")":
                matched = True if unmatched_right[i]==False else False

            if matched:
                running+=1
                max_matched = max(max_matched, running)
            else:
                running =0   
                        
        return max_matched               
               
my_sol = Solution()
s = ")()())"
result = my_sol.longestValidParentheses(s)    
print(result)  
# s = "(()"
# result = my_sol.longestValidParentheses(s)      
# print(result)