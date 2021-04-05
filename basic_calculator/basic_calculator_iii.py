class Solution:
    def calculate(self, s):

        if len(S)<1:
            return 0

        digits = []
        for i in range(10):
            digits.append(int(i))
        operation ="+"    
        my_stack=[]

        for i in range(len(s)):
            currentChar = s[i]

            if currentChar in digits:
                currentNumber +=currentNumber*10 +int(currentChar)
            if not currentChar in digits and currentChar!=" " or i==len(s)-1:
                if operation =="+":
                    my_stack.append(currentNumber)
                elif operation =='-':
                    my_stack.append(-currentNumber)
                elif operation=='('        





