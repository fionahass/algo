class Solution:
    def calculate(self, s):

        if len(s)<3:
            return s

        ops =["(",")","+","-"]
        digits =[]
        stack = []

        for i in range(10):
            digits.append(str(i))

        nums = 0
        op ="+" 
        s=s+"+"

        for i in range(len(s)):
            if s[i] in digits:
                nums = nums*10+int(s[i])
            elif  i==len(s)-1 or s[i] in ops:
                if op =="+":
                    stack.append(nums)
                    sign = "+"
                elif op =='-':
                    stack.append("-")
                    if s[i]!="(":
                        stack.append(nums)
                elif op=='(':
                    stack.append("(")
                    stack.append(nums)
                elif op==")":
                    running = 0
                    while stack and stack[-1]!="(":
                        running += stack.pop()
                    stack.pop()
                    stack.append(running)        
                op = s[i]
                nums = 0   
                print(op,stack)           

        sum =0
        for num in stack:
            if num=="-":
                sign = -1
                print(sign,num)
                continue
            else:
                if sign == -1:
                    sum-=num    
                    sign = 1
                else:
                    sum+=num    


        return sum

s = "(1+(4+5+2)-3)+(6+8)"
my_sol = Solution()
# result = my_sol.calculate(s)
# print(result)

# s=" 2-1 + 2 "
# result = my_sol.calculate(s)
# print(result)

s ="- (3 + (4 + 5))"        
result = my_sol.calculate(s)
print(result)                



