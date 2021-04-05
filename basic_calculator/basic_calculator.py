class Solution:
    def calculate(self, s):

        length = len(s)
        
        if (length==0):
            return 0 
        
        my_stack =[]
        currentNumber = 0
        operation='+'
        digits =[]
        for i in range(10):
            digits.append(str(i))
            
        for i in range(length):
            currentChar = s[i]
            print("currentChar={0},operation={1}".format(currentChar,operation))
            if currentChar in digits:
                currentNumber = currentNumber*10 + int(currentChar)
                print("currentNumber=",currentNumber)
            if not currentChar in digits and currentChar !=" " or i == length-1:
                print("operating")
                if (operation =='-'):
                    my_stack.append(-currentNumber)
                elif (operation=='+'):
                    my_stack.append(currentNumber)
                elif (operation=='*'):
                    stackTop = my_stack.pop()
                    print('*',stackTop,currentNumber)
                    my_stack.append(stackTop*currentNumber)
                elif (operation=='/'):
                    stackTop = my_stack.pop()
                    
                    my_stack.append(int(stackTop/currentNumber))
                    print('/',stackTop,currentNumber,int(stackTop/currentNumber))
                operation = currentChar;
                currentNumber = 0
            print(i,s[i],currentNumber,my_stack,operation)    
        
        result = 0
        print(my_stack)
        while (my_stack):
            result+=my_stack.pop()
        return result    

my_sol = Solution()
s = "3+2*2"  
result = my_sol.calculate(s)
print(result)

# s = "3/2"  
# result = my_sol.calculate(s)
# print(result)

s = "14-3/2"
result = my_sol.calculate(s)
print(result)
#   		