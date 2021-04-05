class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        if len(matrix)<=0 or len(matrix[0])<=0:
            return 0

        n,m = len(matrix),len(matrix[0])

        left  = [0] *m 
        right = [m] *m
        height = [0] *m
        max_area = 0
         
        for i in range(n):
            cur_left = 0
            cur_right = m
            for  j in range(m):
                if matrix[i][j]=="1":
                    height[j]+=1
                    left[j] = max(left[j],cur_left)
                else:
                    height[j] = 0
                    left[j] = 0
                    cur_left =j+1

            for j in range(m-1,-1,-1):
                if matrix[i][j]=="1":
                    right[j] = min(right[j],cur_right)   
                else:
                    right[j] = m
                    cur_right = j

            for j in range(m):        
                cur_area = (right[j]-left[j])*height[j]
                # keep trace of max area with ones 
                max_area = max(max_area, cur_area)


        return max_area                     


my_sol = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
result = my_sol.maximalRectangle(matrix)
print(result)

